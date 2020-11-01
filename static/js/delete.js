function archiveFunction() {
event.preventDefault(); // prevent form submit
var form = event.target.form; // storing the form
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
    form.submit();          // submitting the form when user press yes
  } 
});
}