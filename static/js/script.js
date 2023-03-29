document.addEventListener('DOMContentLoaded', function() {
    // dropdown initialization
    let dropdown = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(dropdown);

    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // selector initialization
    let selector = document.querySelectorAll('select');
    M.FormSelect.init(selector);
});