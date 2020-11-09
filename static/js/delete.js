function deleteFunction() {
event.preventDefault(); // prevent default delete
var form = event.target.form;
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
    form.submit();          // delete when user press yes
  } 
});
}