// code validated through JSHint: https://jshint.com/
function sendMail(contact) {
    emailjs.send("gmail", "sby_email", {
        "name": contact.name.value,
        "email": contact.email.value,
        "help": contact.help.value
    })
    .then(
        function(response) {
            console.log("sent", response);
            removeFormSuccess(); // Success confirmation message and form removal 
        },
        function(error) {
            console.log("fail", error);
        }
    );
    return false;  // To block from loading a new page
}