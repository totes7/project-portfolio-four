## Testing

### Table of Contents

* [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Site Testing](#site-testing)

* [Validator Testing](#automated-testing)

* [Bugs](#bugs)
  * [Known Bugs](#known-bugs)
  * [Solved Bugs](#solved-bugs)


## Manual Testing

### Testing User Stories

* **As a customer:**

    * I can create an account so that I can access the website's services.
        * Account creation has been added as a feature of the site.
    * I can log in/log out with my credentials so that I can securely access my account information and bookings.
        * Users can easily log in and out of their accounts.
    * I want an intuitive user interface with clear visual cues when entering data into fields on the booking form so that it is easy for me understand and use correctly without confusion or frustration.
        * Reservation Form is easily accessed and intuitive and contains datepicker and dropdown menus to reduce user inputs to minimum.
    * I can select the time and date of my reservation so that I can book a table at the restaurant.
        * Booking form contains date and time inputs.
    * I can enter the number of guests in my party so that the restaurant knows how many people are coming.
        * Booking form contains a number of guests input.
    * I can make special requests along with my reservation so that I can make my experience unique and inform the restaurant about possible special occasion like birthdays, anniversaries, etc.
        * Booking form contains a special requests input.
    * I can view, change or delete upcoming reservations so that I can easily manage them without contacting the restaurant directly.
        * MyBookings page contains edit and delete buttons to easily update or cancel reservations.
    * I can view restaurant menu with items prices so that I can see food offered by restaurant prior to my reservation.
        * Menu page with all items and prices is an easily accessible feature of the site.
    * I can read about the Chef so that I can better understand their philosophy and what it's behind the creation of their menu.
        * Chef profile card present on menu page.
    * I can view the restaurant's location on a map so that I can easily plan my route.
        * Location section in homepage contains a live map with restaurant address card.
    * I can contact the reservation website customer service so that I can suggest improvements or report issues and bug with the website itself.
        * Contact page created with link on the footer.
    
* **As a restaurant owner:**

    * I can access an admin page so that I can easily see and manage reservations.
        * Admin panel has been added as a feature of the site, where owner can see and manage reservations.
    * I can add and remove tables from the restaurant plan so that I can easily manage restaurant availability.
        * In the admin panel the owner has the option of creating and deleting tables.


### Site Testing

Manual testing of the website was carried out along with the development process. 
Details of these manual tests are listed below:

* **NavBar:**

    * Nav Bar is reactive to screen size and collapses into an hamburger toggle on smaller screen sizes.
    * All the links work correctly, redirecting the user to the correct page.
    * When the user is not registered yet, only the Home, Sign Up and Log In buttons are displayed.
    * The logo redirect users to the homepage when clicked.

* **Account Pages:**

    * Both Sign Up and Log In pages work correctly.
    * Forms on these pages work as expected, were users must input username, password and confirm password to register, and username and password to log in.
    * Log Out page asks the user to confirm if they want to log out befor doing so.

* **Homepage:**

    * Homepage displays Sign Up and Log In buttons when user is not logged in, and Make a Reservaton and Check out the Menu when user is logged in.
    * All the buttons work correctly, redirecting user to correct pages.
    * The map feature works correctly, being interactive and showing correct address and location.

* **Make a Booking Page:**

    * Make a booking page is only available to registered and logged in users.
    * The booking form works correctly, where users must input all details apart from special requests, which can be left blank.
    * A form error is displayed if any of the required fields is left blank.
    * The date and time widgets work correctly, with the time widget only displaying the time slots specified in the Booking model.
    * A success alert message is displayed when the user succesfully places a booking.
    * Once the user places a booking, he/she gets redirected to the My Bookings page.

* **My Bookings Page:**

    * My Bookings page is only available to registered and logged in users.
    * The page correctly displays all booking made by specific user.
    * All booking details are shown properly for each reservation.
    * Each reservation card contains an Edit and a Delete buttons.
    * Both Edit and Delete buttons redirect the user to the correct page.

* **Edit Booking Page:**

    * The Edit Bookiong page appears once the user clicks on Edit button in My Booking card.
    * The page contains a booking form prefilled with the exsisting booking details.
    * Once the confirmation button is clicked, the user is redirected to My Bookings page where the booking edited is now displayed with correct edited details.

* **Delete Booking Page:**

    * The Delete Bookiong page appears once the user clicks on Delete button in My Booking card.
    * The page displays the details of the selected booking, asking the user for deletion confirmation.
    * A Back button is present to give the user the option to go back to My Booking page if the user decides not to go through with the booking cancellation.
    * A success message is displayed once the booking is successfully deleted.
    * Upon deletion, the user is redirected to My Bookings page.

* **Menu Page:**

    * The Menu page is only available to registered and logged in users.
    * The page correctly displays all menu items with their prices.
    * The page also contains a brief Chef Profile card.

* **Footer:**

    * The social media links in the footer all work correctly, redirectin user to the selected social media homepage.
    * The Contact Us link in the footer works correctly, redirecting users to the Contact Us page.

* **Contact Us Page:**

    * The page opens correctly after user clicks the link in the footer.
    * The page consist of a contact form, where user must input name, email and message.
    * A form error is displayed if any of the fields is left blank.
    * After the message is submitted, the user is redirected to the Homepage.

* **Admin Panel:**

    * The Admin Panel is available only after Owner logs in with superuser credentials.
    * The Owner can view and manage Users, Bookings and Tables.


## Validator Testing

* **HTML**
    * All HTML pages have been checked using the [W3C Markup Validator](https://validator.w3.org/). No errors have been found.
* **CSS**
    * The style.css page has been checked using the [W3C CSS Validator](https://jigsaw.w3.org/). No errors have been found.
* **JavaScript**
    * The script.js page has been checked using the [Beautify Tools](https://beautifytools.com/) Validator. No errors have been found.
* **Python**
    * All Python pages have been checked using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/). No errors have been found.


## Bugs

### Known Bugs

* The success alert message when updating a booking is not showing. I tried every solution I could find online, but the bug persist.

### Solved Bugs

* Initially the NavBar used to have a single button named Booking that opened a dropdown containing the Make a Booking and My Bookings buttons, but at some point during development the dropdown stopped working on larger screens and was only working on smaller screens inside the SideNav. I had to remove the dropdown and create the two separate buttons in order to fix the issue.
* During development it was discovered that once a booking was edited, it created a new instance of the booking without removing the previous instance. This was fixed modifying the python code ensuring that the existing instance was being modified instead of creating a brand new one.
* Initially in the My Booking page the booking cards showed the time of reservation as the number 1 through 4 of the 'BOOKING_TIME' tuple present in the Booking model. The issue was fixed replacing {{ booking.time }} with {{ booking.get_time_display }} in the HTML form.