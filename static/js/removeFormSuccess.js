// code validated through JSHint: https://jshint.com/
// jshint esversion: 'template literal syntax' is only available in ES6 (use 'esversion: 6').
// removes contact form and displays success message on sneding a message
function removeFormSuccess() {
    var el1 = document.getElementById("contact-div");
    el1.parentNode.removeChild(el1);
    var el = "";
    el += `<p class="sm-text center-align">Thanks! We've received your message and will be in touch shortly.</p>
        <div class="row all-events-button">
      <div class="col s12 center-align">
        <a href="{{ url_for('get_events') }}" class="btn-large light-green accent-2 all-events-button">
          Back to all Events<i class="fas fa-calendar-alt right"></i>
        </a>
      </div>
    </div>`;
      document.getElementById("email-success").innerHTML = el;
}