# DineMate

This is a website for a high-end restaurant in Miami, South Beach. It consist of a homepage with a section about the restaurant and a map feature with address and opening times. The website act as a booking platform for the restaurant as well, where customers can book tables at specific dates and times after registering. Customers are also allowed to keep track of their reservations, updating and deleting them as they please.

[The live site can be found here.](https://totes7-dinemate.herokuapp.com/)

![Site Mockup](readme_docs/SiteResponsive.jpg)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

### User Stories

* ### As a customer:

    * As a Site User I want a easy to access navigation bar so that I can easily traverse the website.
    * As a Site User I can create an account so that I can access the website's services.
    * As a SiteUser I can log in/log out with my credentials so that I can securely access my account information and bookings.
    * As a Site User I can view restaurant menu with items prices so that I can see food offered by restaurant prior to my reservation.
    * As a Site User I can view the restaurant's location on a map so that I can easily plan my route.
    * As a Site User I want an intuitive user interface with clear visual cues when entering data into fields on the booking form so that it is easy for me understand and use correctly without confusion or frustration.
    * As a Site User I can select the time and date of my reservation so that I can book a table at the restaurant.
    * As a Site User I can enter the number of guests in my party so that the restaurant knows how many people are coming.
    * As a Site User I can make special requests along with my reservation so that I can make my experience unique and inform the restaurant about possible special occasion like birthdays, anniversaries, etc.
    * As a Site User I can view, change or delete upcoming reservations so that I can easily manage them without contacting the restaurant directly.
    * As a Site User I can read about the Chef so that I can better understand their philosophy and what it's behind the creation of their menu.
    * As a Site User I can contact the reservation website customer service so that I can suggest improvements or report issues and bug with the website itself.

* ### As a restaurant owner:

    * As a Site Admin I can access an admin page so that I can easily see and manage reservations.
    * As a Site Admin I can view existing reservations so that I can inform the customers about any possible issues with their bookings.

---

## Design

* ### Colour Scheme

  For this project I started by choosing a vibrant green as the main color, called Caribbean Green 
  (#11e084).
  Then I used [imagecolorpicker.com](https://imagecolorpicker.com/) to find two complementary colors. The result gave me a nice monochromatic triad, in which the two secondary colors are Dark Green (#043620) and Spanish Green (#0b8b52).

![Color Palette](readme_docs/ColorPalette.jpg)

* ### Typography

  The fonts used in this project are Roboto and Nunito, taken from [Google Fonts](https://fonts.google. 
  com/)

![Fonts Samples](readme_docs/FontsSamples.jpg)

* ### Imagery

  The only two images included in the project are the background image of the homepage, which is just a restaurant main floor, and the chef profile image. The rest of the pages all have the same main bacground wavey pattern using the main color and white.

* ### Wireframes

  The site design is quite simple, allowing the users to easily access the booking form, their existing reservations and the restaurant menu. The wireframes created to help with the layout are as follows:

  * Homepage 

  ![Homepage Wireframe](readme_docs/WireframeHomepage.jpg)

  * Sign Up

  ![SignUp Wireframe](readme_docs/WireframeSignUp.jpg)

  * Log In

  ![LogIn Wireframe](readme_docs/WireframeLogIn.jpg)

  * Make Booking

  ![MakeBooking Wireframe](readme_docs/WireframeMakeReservation.jpg)

  * Manage Bookings

  ![ManageBookings Wireframe](readme_docs/WireframeManageReservation.jpg)

  * Contact Us Page

  ![ContactUs Wireframe](readme_docs/WireframeContactPage.jpg)

  ### Differences to Design

  The final design is slightly different from the wireframes. The function to log in and sign up using Google accounts was not implemented, so that button is not present in the final design. The option to choose from different locations for the restaurant was not implemented, so in the booking form and in the manage bookings cards the location slot is not present. The manage your bookings page is also different from the wireframe in the web implementation, with the table design being substituted by the cards like in the mobile wireframe. The conact page is also slightly different in the final design, with the message replaced by a name and email slots.

  ### Database Schema

  The site database schema is based around two models, booking and table. The booking model includes all the required information that the user has to provide in order to make a booking, with the primary key being the booking id. The table model is quite simple, consisting of a table id, table number (primary key) and a table capacity. The two models are connected via the table number, which is reflected in the booking informations once the booking is successfully placed, with the system making sure that the same table is not booked twice at the same time and date.

  ![Database Models Wireframe](readme_docs/DatabaseModelsWireframe.jpg)