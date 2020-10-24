/*jshint esversion: 6 */
function removeFormSuccess() {
    var el1 = document.getElementById("contact-div");
    el1.parentNode.removeChild(el1);
    var el = "";
    el += `<p class="sm-text center-align">Thanks! We've received your message and will be in touch shortly.</p>`;
      document.getElementById("email-success").innerHTML = el;
}