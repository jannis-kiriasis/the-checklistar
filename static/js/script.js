let approverForm = document.querySelectorAll(".approver-form");
let container = document.querySelector("#form-container");
let addButton = document.querySelector("#add-approver");

const deleteButton = document.getElementById("delete");
const approveButton = document.getElementById("approve");
const confirmButton = document.getElementById("confirm");
const editButton = document.getElementById("edit");

// Get message box
const message = document.getElementById("message");

// Make message box disappear after 5 seconds
setTimeout(function(){ 
  message.style.display = "none"; 
}, 5000);

// Get input with total number of forms
let totalForms = document.querySelector("#id_approvals-TOTAL_FORMS")

// Get the number of the last form on the page with zero-based indexing
let formNum = approverForm.length-1 

addButton.addEventListener('click', addForm)

// Event listeners for SweetAlerts defensive design
deleteButton.addEventListener('click', confirmDelete);
approveButton.addEventListener('click', confirmApprove);
completeButton.addEventListener('click', confirmComplete);
editButton.addEventListener('click', confirmEdit);

// On DOM content loaded initialize sidenav
document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
})

// The following function to add dynamic form fields comes from
// https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript
// and it has been edited to suit this project


function addForm(e) {
    e.preventDefault()

    //Clone the approver form
    let newForm = approverForm[0].cloneNode(true) 

    //Regex to find all instances of the form number
    let formRegex = RegExp(`approvals-(\\d){1}-`,'g') 

    //Increment the form number
    formNum++ 

    //Update the new form to have the correct form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `approvals-${formNum}-`) 
    
    //Insert the new form at the end of the list of forms
    container.appendChild(newForm) 

    //Increment the number of total forms in the management form
    totalForms.setAttribute('value', `${formNum+1}`) 
}


// Delete project defensive design with SweetAlerts2
// Get href url, prevent button click, fire SweetAlerts2, 
// after defensive design redirect to /delete/{{ project.id }}

function goToDeleteUrl() {
    let href = document.getElementById('delete').getAttribute('href')
    window.location.href = `${href}`;
}

function confirmDelete(event){
    event.preventDefault()
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
      })
    }


// Approve project defensive design with SweetAlerts2
// Get href url, prevent button click, fire SweetAlerts2, 
// after defensive design redirect to /delete/{{ project.id }}

function goToApproveUrl() {
    let href = document.getElementById('approve').getAttribute('href')
    window.location.href = `${href}`;
}

function confirmApprove(event){
    event.preventDefault()
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
      })
    }


// Complete project defensive design with SweetAlerts2
// Get href url, prevent button click, fire SweetAlerts2, 
// after defensive design redirect to /complete/{{ project.id }}

function goToCompleteUrl() {
    let href = document.getElementById('complete').getAttribute('href')
    window.location.href = `${href}`;
}

function confirmComplete(event){
    event.preventDefault()
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
      })
    }


// Edit project defensive design with SweetAlerts2
// Get href url, prevent button click, fire SweetAlerts2, 


function confirmEdit(){
  Swal.fire({
    position: 'center',
    icon: 'success',
    iconColor: 'var(--verdigris)',
    title: 'Your project has been updated!',
    showConfirmButton: false,
    timer: 1500
  })
  }


