document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // selector initialization
    let selector = document.querySelectorAll('select');
    M.FormSelect.init(selector);
});