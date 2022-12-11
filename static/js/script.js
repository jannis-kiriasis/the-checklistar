const approverForm = document.querySelectorAll('.approver-form');
const container = document.querySelector('#form-container');
const addButton = document.querySelector('#add-approver');
const removeButton = document.querySelector('#remove-approver');
const notification = document.getElementById('notification-count');
const notificationM = document.getElementById('notification-count-m');

const deleteButton = document.getElementById('delete');
const approveButton = document.getElementById('approve');
const completeButton = document.getElementById('complete');

// Get delete input field and label by xpath
let delete_input_xpath = "//input [contains (@id, '-DELETE')]";
let delete_input = document.evaluate(delete_input_xpath, document,
        null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    .singleNodeValue;
let delete_label_xpath = "//label [contains (@for, '-DELETE')]";
let delete_label = document.evaluate(delete_label_xpath, document,
        null, XPathResult.FIRST_ORDERED_NODE_TYPE, null)
    .singleNodeValue;

// Get message box
const message = document.getElementById('message');

// Make message box disappear after 5 seconds
setTimeout(function() {
    message.style.display = 'none';
}, 5000);

// Get input with total number of forms
let totalForms = document.querySelector('#id_approvals-TOTAL_FORMS');

// Get the number of the last form on the page with zero-based indexing
let formNum = approverForm.length - 1;

if (addButton) {
    addButton.addEventListener('click', addForm);
}

if (removeButton) {
    removeButton.addEventListener('click', removeForm);
}

// Event listeners for SweetAlerts defensive design

if (deleteButton) {
    deleteButton.addEventListener('click', confirmDelete);
}

if (approveButton) {
    approveButton.addEventListener('click', confirmApprove);
}

if (completeButton) {
    completeButton.addEventListener('click', confirmComplete);
}

// On DOM content loaded initialize sidenav
document.addEventListener('DOMContentLoaded', function() {

    let collapsible = document.querySelectorAll(
        '.collapsible');
    M.Collapsible.init(collapsible);

    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
});

// The following function to add dynamic form fields comes from
// https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript
// and it has been edited to suit this project

/**
 * Add dynamic fields to Create form to add as many approvers as needed.
 */
function addForm(e) {
    e.preventDefault();

    //Clone the approver form
    let newForm = approverForm[0].cloneNode(true);

    //Regex to find all instances of the form number
    let formRegex = RegExp(`approvals-(\\d){1}-`, 'g');

    //Increment the form number
    formNum++;

    //Update the new form to have the correct form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex,
        `approvals-${formNum}-`);

    //Insert the new form at the end of the list of forms
    container.appendChild(newForm);

    //Increment the number of total forms in the management form
    totalForms.setAttribute('value', `${formNum+1}`);
}

/**
 * Remove dynamic forms from when creating and updating projects.
 */
function removeForm(e) {
    e.preventDefault();

    formNum--;
    container.removeChild(container.lastChild);
    totalForms.setAttribute('value', `${formNum-1}`);
}

/** Get href url of button delete.
*/
function goToDeleteUrl() {
    let href = document.getElementById('delete').getAttribute('href');
    window.location.href = `${href}`;
}

/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect to /delete/{{ project.id }}
*/
function confirmDelete(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--fuzzy-wuzzy)',
        cancelButtonColor: 'var(--liberty)',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToDeleteUrl();
        }
    });
}

/** Get href url of button approve.
*/
function goToApproveUrl() {
    let href = document.getElementById('approve').getAttribute(
        'href');
    window.location.href = `${href}`;
}

/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect to /approve/{{ project.id }}
*/
function confirmApprove(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you are ready to approve this project?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, approve it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToApproveUrl();
        }
    });
}

/** Get href url of button complete.
*/
function goToCompleteUrl() {
    let href = document.getElementById('complete').getAttribute(
        'href');
    window.location.href = `${href}`;
}

/** Prevent button click, fire SweetAlerts2, 
* after defensive design redirect to /complete/{{ project.id }}
*/
function confirmComplete(event) {
    event.preventDefault();
    Swal.fire({
        title: 'Are you sure you are ready to complete and close this project?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        iconColor: 'var(--tan)',
        showCancelButton: true,
        confirmButtonColor: 'var(--verdigris)',
        cancelButtonColor: 'var(--fuzzy-wuzzy)',
        confirmButtonText: 'Yes, approve it!'
    }).then((result) => {
        if (result.isConfirmed) {
            goToCompleteUrl();
        }
    });
}

// On /create-project remove delete approver buttons
if (window.location.pathname === '/create-project') {
    if (delete_input) {
        delete_input.remove();
        delete_label.remove();
    }
}

// Hide notification count if innerText = 0
if (notification.innerText === '0') {
    notification.remove();
}

if (notificationM.innerText === '0') {
    notificationM.remove();
}