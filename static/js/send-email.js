/*jshint esversion: 6 */
function sendMail(contact) {
    emailjs.send("gmail", "sby_email", {
        "name": contact.name.value,
        "email": contact.email.value,
        "help": contact.help.value
    })
    .then(
        function(response) {
            console.log("sent", response);
            removeFormSuccess();
        },
        function(error) {
            console.log("fail", error);
        }
    );
    return false;  // To block from loading a new page
}