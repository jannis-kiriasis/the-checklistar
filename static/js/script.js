const add = document.getElementById("addApprover");

document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
})

add.addEventListener("click", function() {
    // First create a DIV element.
	var txtNewInputBox = document.createElement('div');

    // Then add the content (a new input box) of the element.
    txtNewInputBox.setAttribute('class', 'row')
	txtNewInputBox.innerHTML = '<div class="col s6">{{ approver_form.as_p }}</div>';

    // Finally put it where it is supposed to appear.
	document.getElementById("newElement").appendChild(txtNewInputBox);
});