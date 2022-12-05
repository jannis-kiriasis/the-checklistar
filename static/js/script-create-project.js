// let approverForm = document.querySelectorAll(".approver-form");
// let container = document.querySelector("#form-container");
// let addButton = document.querySelector("#add-approver");

// // Get input with total number of forms
// let totalForms = document.querySelector("#id_approvals-TOTAL_FORMS")

// // Get the number of the last form on the page with zero-based indexing
// let formNum = approverForm.length-1 

// addButton.addEventListener('click', addForm)

// // The following function to add dynamic form fields comes from
// // https://www.brennantymrak.com/articles/django-dynamic-formsets-javascript
// // and it has been edited to suit this project


// function addForm(e) {
//     e.preventDefault()

//     //Clone the approver form
//     let newForm = approverForm[0].cloneNode(true) 

//     //Regex to find all instances of the form number
//     let formRegex = RegExp(`approvals-(\\d){1}-`,'g') 

//     //Increment the form number
//     formNum++ 

//     //Update the new form to have the correct form number
//     newForm.innerHTML = newForm.innerHTML.replace(formRegex, `approvals-${formNum}-`) 
    
//     //Insert the new form at the end of the list of forms
//     container.appendChild(newForm) 

//     //Increment the number of total forms in the management form
//     totalForms.setAttribute('value', `${formNum+1}`) 
// }
