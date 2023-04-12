document.addEventListener('DOMContentLoaded', function() {
   // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // selector initialization
    let selector = document.querySelectorAll('select');
    M.FormSelect.init(selector);

    // messages timeout
    let messages = document.getElementById('msg');
    if(messages){
        setTimeout(function() {
            messages.style.display = "none";
        }, 3000);
    }
});