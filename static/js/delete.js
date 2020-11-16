// Code modified from and credited to:
// https://stackoverflow.com/questions/46034634/sweet-alert-confirmation-before-delete/46035103
// code validated through JSHint: https://jshint.com/

function deleteFunction() {
event.preventDefault(); // prevent default delete
var form = event.target.form;
// sweet alert confirmation modal
        swal({
  title: "Are you sure?",
  text: "You won't be able to undo the action.",
  showCancelButton: true,
  confirmButtonColor: "#EB1F12",
  confirmButtonText: "Delete",
  cancelButtonText: "Cancel",
  closeOnConfirm: false,
  closeOnCancel: true
},
function(isConfirm){
  if (isConfirm) {
    form.submit();  // delete when user presses yes
  } 
});
}