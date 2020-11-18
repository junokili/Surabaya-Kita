
# Surabaya Kita

## Introduction

This project is a full-stack site, Surabaya Kita, that allows a database of registered users
 to manage a common dataset, which comprises a variety of community events. 
 It can be accessed here http://surabaya-kita.herokuapp.com/

The site is based around an independent cafe, set up by a foreigner who moved to a new city in Indonesia and 
wanted to meet new people and find some fun acitvities to do within their community. The site also provides some brief information 
about the café and its story, including a map and contact functions. Users are able to view and search all the events avaialble and also 
 create, edit and delete their own events, while the site owner maintains admin control over the
 database. By basing the events site around the cafe, the site owner 
can add value to their community and increase their customer base and sales by hosting user events within the cafe. 


## UX

### Project Goals

The primary goal of Surabaya Kita is to provide a site where users can browse local community-generated events
and also create and share their own events. 
The secondary goal is to attract additional customers to Surabaya Kita Cafe by organizing and hosting social events.  

### User Goals

- To be able to meet new people in a safe enironment in their city 
- Find out about and attend fun and interesting local events

### Developer / Business Goals

- Increase the volume of customers to the cafe by offering something extra
- Make a site that looks professional, that users want to use and come back to
- Consolidate and expand knowledge of multiple programming languages


### User Stories

Details of how the site fulfills these user stories can be found in the Testing section. 

New and existing users:
1. As a new user I want to browse the site to quickly see what's going on
2. As a new user I want to find out about the cafe and decide if it's the sort of place I want to go to
3. As a new user I want to be a part of the community and share in local events 
4. As a new or existing user I want to find a local event to meet new people, and feel safe doing so
5. As a new or existing user I want to be able to search the events to find things I am interested in
6. As an existing user I want to create, edit and delete my own events with appropriate feedback 

Site owner:
1. As the site owner I want to enhance my community and widen my social network
2. As the site owner I want to promote my cafe by offering something extra
3. As the site owner I want to create, edit and delete my own events and highlight them
4. As the site owner I want to retain admin controls over user-generated content
5. As the site owner I want to make it easy for users to ask questions and make requests for improving 
their options when creating events
6. As the site owner I want to be a part of the community and share in local events 

### Design Choices

**Overall Design**
The site has a clear identity, with a consistent and predictable theme and style throughout. 
The site layout is simple with a navbar at the top right, which collapses to a hamburger menu 
on smaller screen sizes, the site name as a home page link and
 and a standard footer with contact information and links to social media pages (not active). 
 All clickable links have clear actions and responses. The site is designed over 
multiple pages and each page's content is clear. It is easy to know where you are, 
or how to get where you want to be. There are additional buttons 
 on pages such as My Events, My Profile to direct the user. 

The elements and features are clear and legible. 
The key elements are easy to recognise and disclosed progressively over different pages. The features currently offered provide the user 
and owner with what they need, and they are simple 
to implement and use. Future releases can add value in bite-size increments, such as displaying events in caledar 
or map format, using profile information to tailor suggested events to users (e.g. Events Near You / Events You May Like), 
and allowing users to express interest in a particular event. 

**Font**
The google font, Khumb Sans, was chosen for the site, as it is clear, simple, easy to read
 and doesn't detract from any content.

**Colours**
The colour scheme for the site is based on three main colours, bright cyan, light green and white. 
These colours represent Surabaya to the site owner / developer - the cyan of the sky and the sea (it's a coastal city) and the green of 
the fields and jungle surround the city (it's tropical) - and give a fresh, vibrant but grown up look, which reflects 
the ethos of the cafe and the site owner and represents the target broad age range adult user. The typography is a medium-dark grey 
or cyan for links, and for headers and flashed messages it is white on cyan or light green banners respectively. 

The colour scheme is also carried through the site, including create, edit, cancel and delete buttons, 
within the forms and e.g. dropdown menus and time and date pickers. 

**Card images**
The images used on the site were chosen as they visually represent the categories of the events.
They are all bright, vibrant images, making the events more attractive to the users. Where the images
are they developer's own, they have a similar colour palette to the theme of the site. 

**Styling** 
 The events are 
 displayed as individual cards with the event name (user-generated), category name and photo (admin-generated) 
 for easy visual filtering, and a short description of the event. There is a "reveal" function, 
 evident by the plus icon, that on click displays the detailed event information, such as date, time,
 location, etc. By hiding this information it keeps the site cleaner. 
 On loading the Home page, only the events organized by Surabaya Kita are displayed 
 with a button to the Events page. On the Events page only the events happening in the current month are displayed initially, with an 
 expandable div for All Events, to keep the pages cleaner.
 
 The forms for creating and editing events, signing up and editing the user profile are clear and simple with 
 a defensive design shown by warning signs and a red underline that turns green when validated. 
 All buttons have text and icons to make their actions clear. Forms also use card styling. 
 
**Icons**
 Icons are used to reduce text, in the events cards, and all the forms.
They have been chosen for their obvious meaning, but some have been tooltipped for the user's assistance. 

### Wireframes

A series of wireframes have been generated for desktop, tablet and mobile views. The idea of the site was 
smaller when the wireframes were first created, however, the general colour scheme (but not the specific colours),
 and the overall layout (e.g. using cards for the events and categories, the footer) has remained the same. 
 Wireframes can be found here https://github.com/junokili/Surabaya-Kita/tree/master/static/images/mock_ups


## Features

Features include:
- **About Us** - information about the Surabaya Kita Cafe, including a brief, personal story, 
map and a carousel of photos 
- **Monthly Events** - highlighting what's on in or around the cafe organized by the business owners. 
As these are events organized by the site, users can feel confident and safe in joining them.
- **Events: Events this Month** - a card display of events within the current month. The cards give a visual representation of the 
event so users can quickly scan for those of interest
- **Events: All Events** - a collapsible card display of all of the available events to reduce clutter on the screen
- **Search Bar** - so users can search by category or keyword
- **Sign Up / Login / Log Out** - a signing up feature as only registered members can create events. 
New users are automatically logged in and redirected to the My Profile page. Users can easily log out at the
end of a session
- **My Profile** - basic information about the user. This allows events to be attached to a username
so other users can search events based on a username. Additional future features.
- **My Events** - a apage where users can view, edit or delete their own events
- **Create Event / Edit Event** - simple forms for users to create and edit their own new events
- **Contact Us Form** - a simple form so users can easily ask queries to the site owners or ask for additional 
categories / locations to be added to the database. 
- **Manage Categories** - a simple page for the site owner to read, create, edit and delete categories. 

Future features:
- **Calendar of Events** - a graphical way of showing the upcoming events 
- **Map of Events** - use event location to display events on a map
- **Advanced Search** - combining queries e.g. category and location
- **Automatic Delete of Expired Events** - to reduce admin time and not frustrate users by having out of date events
-**Register Interest in an Event** - action buttons associated to events to allows users to register interest, 
so the event host has an idea of numbers
- **My Profile** - by increasing the functionality of the profile information 
users will be able to automatically see events near them (using the location they chose when signing up)
 and add their interests to get more focused events that may be relevant. User profile photos can be uploaded, 
 to replace the current placeholder. 
 - **Cafe info** - additional information about the cafe, eg address, opening hours, menus etc
 - **Manage locations** - similar to the Manage Categories features, there will be a manage locations feature
 where the admin can view, create, edit and delete locations. 
 - **Additional confirmation for Workshops** - this will initially be monitored by admin for use of the workshop area and users contacted by email.
Admin would need to be able to confirm the use of the workshop space
 and arrange a deal with food and drink discounts for users. 

## Technologies used

- HTML: layout and content 
- CSS: styling
- JavaScript: google maps API, contact us/email and delete confirmation 
- Python and Flask: connecting to MongoDB and performing CRUD operations
- MongoDB: for the database with events, locations, users, and categories https://mongodb.com
- Font Awesome: icons that visually represent the form criteria and info display https://fontawesome.com
- Google Fonts: a back-up font family that represents the style and design of the site https://fonts.google.com
- Materialize (CSS, JavaScript/JQuery) for the functionality of the navbar, hamburger menu, photo carousel, 
forms, basic card and card reveal styling, dropdown menus, date and time pickers
    and the grid structuring of the site https://materialize.com


## Testing 

- **Links**

All internal and external links have been tested. 
The links to external sites (e.g. facebook, instagram) display a "coming soon" image as the social media for the site
has not yet been created. 
Internal links, such as button clicks, menu links, links to sections, 
have all been verified that they perform as requested. 

- **Contact us form**

On submission the form comes up with an error if it hasn't been filled in correctly (e.g. email address), 
or if required information (name, email address and details in the text box) is missing. 
The form data is sent as an email to the site owner. The email received contains all the submitted data 
(name, email and the message). Email receipt has been verified in the associated account. 
A success message is shown only when the form is successfully submitted. 

- **Responsiveness**

At every stage of the development process the responsiveness of the site has been checked through chrome 
developer tools for all available device formats.
The grid structuring uses responsive parameters for display effectiveness in e.g. displaying parallel event cards 
(4 on large screens, 3 on medium screens and 1 on small screens) and also for the navbar collapsing below medium 
 screen widths. There are also font size changes for display effectiveness in e.g. the headers and the search boxes. 
The site has also been tested successfully on different browsers e.g. Chrome, Firefox, Edge.  

- **Language Validation**

The HTML was validated through W3C HTML Validation Service (https://validator.w3.org/nu/). 
A significant number of errors appear, however these are due to the curly brackets used with the python/flask app. 
One warning is noted, which is due to a repeated id value in the Edit Event form, however, this results from a switch in a meterilize form
repeated in an if / else function.

The CSS was validated with no reported errors through W3C CSS Validation Service (https://jigsaw.w3.org/css-validator/).

The JavaScript files were validated through JSHint (https://jshint.com/) with the only errors being 
the use of functionality only with ES6 (for which a comment was added) 
and apparent unused functions, however these are all invoked within other functions 
or button clicks, likewise the apparent undefined variables are all defined and utilised.

The Python code was validated with no reported errors through PEP8 Online (http://pep8online.com/).

- **Testing of CRUD functions with MongoDB**

All CRUD functions have been manually tested. 

#### Event Read

1. Expected: Site is expected to display events from the database when user loads home / events / my events pages
2. Testing: Tested the site by displaying events on pages
3. Results: Site acted as expected

#### Event Create
1. Expected: Site is expected to create a new event and insert it into the database when user submits Create Event form
2. Testing: Tested the site by creating numerous events and displaying new events
3. Results: Site acted as expected

#### Event Update
1. Expected: Site is expected to allow user to make updates to their events and update the database when user submits edits
2. Testing: Tested the site by editing various events
3. Results: Site acted as expected

#### Event Delete
1. Expected: Site is expected to delete events from the database when user submits delete
2. Testing: Tested the site by deleting various events
3. Results: Site acted as expected

#### Category Read
1. Expected: Site is expected to display categories from the database when admin user loads Categories page
2. Testing: Tested the site by displaying categories on page
3. Results: Site acted as expected

#### Category Create
1. Expected: Site is expected to create a new category and insert it into the database when user submits Add Category form
2. Testing: Tested the site by creating numerous categories and displaying them
3. Results: Site acted as expected

#### Category Update
1. Expected: Site is expected to allow admin user to edit categories and update the database when user submits edits
2. Testing: Tested the site by editing various categories
3. Results: Site acted as expected

#### Category Delete
1. Expected: Site is expected to delete categories from the database when user submits delete
2. Testing: Tested the site by deleting various categories
3. Results: Site acted as expected

#### User Create
1. Expected: Site is expected to create a new user and insert it into the database when user submits Sign Up form
2. Testing: Tested the site by creating numerous users and checking the database / logging out-in
3. Results: Site acted as expected

#### User Read
1. Expected: Site is expected to display user information from the database when logged in
2. Testing: Tested the site by logging in various users, checking My Profile and My Events pages, and special functions
only available to the admin user
3. Results: Site acted as expected, once an issue over using .lower() for the username when signing up,
 but not when reading was removed. 

#### User Update
1. Expected: Site is expected to allow user to edit user information and update the database when user submits edits
2. Testing: Tested the site by editing e.g. user name and location
3. Results: Site acted as expected once correct use of session username/user_id had been resolved

- **Testing of User Stories**

New and existing users:
1. As a new user I want to browse the site to quickly see what's going on
    - The home page displays some of the monthly events, with a clear button directing the user to additional events
    - The navigation bar or hamburger menu is predictable and easily available on every page 
    - There are additional in text and button links to the main pages
    - The site has a simple, usable layout with a consistent theme, recognisable icons and progressive disclosure

2. As a new user I want to find out about the cafe and decide if it's the sort of place I want to go to
    - The cafe information is clearly displayed on the home page and is linked to in text at the top of the page
    - Users can find some info about the cafe background, a map of the location and photos of what kind of things
    are avaialable
    - Cafe contact details can be found in the footer

3. As a new user I want to be a part of the community and share in local events 
    - The site uses positive language to encourage the user to join in and be a part of the community
    - It is only currently necessary to sign up if the user wants to create their own events
    - The link to sign up can be easily found in the navigation bar
    - There is a simple sign form up with the minimum of details and new users are automatically logged in
    - A confirmation message of new user added is flashed and the user is redirected to the My Profile page. 
    - My Profile contains a button to My Events, where there is an in text link to create an event
    - The navigation bar contains a Create Event link, and there is an in text link on the home page.
    - Sign Up and Edit Profile forms are designed defensively so users cannot input incorrect information and are given a 
    warning when any required input has not been filled in

4. As a new or existing user I want to find a local event to meet new people, and feel safe doing so
    - Users can browse the events easily with visual clues
    - Users can then find all the additional details of events that are of interest to them e.g. where, what, when 
    by using the reveal function, and just turn up
    - Users can see the planned meet point for an event in the card reveal so they know whether it will be held somewhere public
    and safe. 
    - The site recommends the use of the site cafe for social events, as this is a safe and friendly
    environment

5. As a new or existing user I want to be able to search the events to find things I am interested in
    - There is a search function based on category and a search function based on keywords,
    both are simple and straightforward. 
    - The searches successfully queries the event database, and users can search on
    category name, event name, meet point, location and username created by. 
    - Results are displayed in the standard card format, with a button to take the user back to the main Events page. 

6. As an existing user I want to create, edit and delete my own events with appropriate feedback 
    - Users can find the Create Event link easily in the navigation bar, or use an in text link to Create Event
    - The Create Event form is simple and the required information is indicated with icons and text 
    - New event created confirmation message is flashed and users are redirected to My Events, so they
    can see that their event has been created 
    - Users can easily navigate to My Events page from anywhere on the site to
    edit or delete their own events, with clear action buttons visible for each event
    - The Edit Event form is filled-in replica of the Create Event form so simple and the required information is indicated with icons and text 
    - When an event is updated a confirmation message is flashed. 
    - The delete button has an additional confirmation modal so the user does not delete things by accident
    - A delete confirmation message is flashed
    - Create and Edit Event forms are designed defensively so users cannot input incorrect information and are given a 
    warning when any required input has not been filled in 

Site Owner:
1. As the site owner I want to enhance my community and widen my social network
    - Providing users with the ability to create their own events through the site will increase positive feelings
    within the community
    - By offering a place to host user social events the site owner creates a community hub
    - The site owner is able to use the site in the same way as a user and can meet people through thir events

2. As the site owner I want to promote my cafe by offering something extra
    - The site is primarily aimed at sharing and promoting local events, giving the cafe something different to it's competitors
    - By suggesting the use of the cafe as a venue for events, the site owner can increase the number of customers visting the cafe

3. As the site owner I want to create, edit and delete my own events and highlight them
    - The site owner events are displayed on the home page and on the events page; user events are found on the events page
    - The site owner creates an event in the same way as a user and can find the Create Event link easily in the navigation bar, 
    or use an in text link to Create Event
    - The Create Event form is simple and the required information is indicated with icons and text
    - New event created confirmation message is flashed and the site owner is redirected to My Events, so they
    can see that their event has been created 
    - The site owner can easily navigate to My Events page from anywhere on the site to
    edit or delete their own events, with clear action buttons visible for each event
    - The Edit Event form is filled-in replica of the Create Event form so simple and the required information is indicated with icons and text
    - When an event is updated a confirmation message is flashed. 
    - The delete button has an additional confirmation modal so the site owner does not delete things by accident
    - A delete confirmation message is flashed
    - Create and Edit Event forms are designed defensively so the site owner cannot input incorrect information and are given a 
    warning when any required input has not been filled in 

4. As the site owner I want to retain admin controls over user-generated content
    - The site owner can edit and delete any user created events. These are visible on the My Events page
    - The site owner can manage the category list for events, and can create, edit and delete these using simple forms that 
    are designed defensively and follow the same style and the event forms, including a delete confirmation modal

5. As the site owner I want to make it easy for users to ask questions and make requests for improving 
their options when creating events
    - The site provides a Contact Us form, which is linked to from multiple locations
    - The meta data for creating an event offers the ability, and a link for the user, that if a user wants additional options they can contact the site
    - Emails are sent to the site owner's account (verified), which include the user email to allow a response

6. As the site owner I want to be a part of the community and share in local events 
    - The site owner can view and search events in the same way as a user

## Deployment

This project was developed using Gitpod and deployed through Heroku. 
It can be accessed here: http://surabaya-kita.herokuapp.com/

The steps taken to set up the project and to deploy it to Heroku were as follows:
1. Create a git repository
2. Create an env.py file, which was added to a .gitnore file for the hidden variables
3. Create a requirements.txt file (terminal command - pip3 freeze –-local > requirements.txt)
4. Create a Procfile file (terminal command - echo web: python app.py > Procfile)
5. Add the new files to the staging area in the terminal (git add)
6. Commit the files to the repository with an appropriate message (git commit -m "message")
7. Push the files to the repository (git push)
Login to Heroku (https://heroku.com) and create a new app, following the prompts to name 
the project and select a region
8. Within the app go to the Deploy tab
9. Select Deployment method: GitHub - Connect to GitHub
10. Check your username, enter the repository name, click Search. 
11. When the repository has been found, click Connect
12. Go to the Settings tab and click Reveal Config vars
13. Enter the Key-Value pairs for the Config Vars (IP (0.0.0.0), PORT (5000), SECRET_KEY (hidden variable),
 MONGO_URI (from MongoDB) and MONGO_DBNAME (from MongoDB))
14. Go to the Deploy tab select Deploy and Enable Automatic Deployment
15. Confirm that app was succesfully deployed. 

To run the app locally in GitHub:
1. Login to GitHub 
2. Navigate to the project repository (https://github.com/junokili/Surabaya-Kita)
3. Click on the Gitpod button and a new, local workspace will be created within Gitpod


## Credits

- **Content:** the content and code is the developer's own except where otherwise attributed.  
(and commented accordingly in the file):
Confirmation before delete with SWAL modal modified from Ankit Chaudary, Stack Overflow:
 https://stackoverflow.com/questions/46034634/sweet-alert-confirmation-before-delete

- **Media:** the images used in this site are the developer’s own excluding:
    - Book Club image from Marie Bostwick
https://mariebostwick.com/starting-or-joining-a-book-club/
    - Language Class image from earth.com
https://www.earth.com/news/young-adults-friends/
    - Workshop image from Pintrest Newsroom
https://newsroom.pinterest.com/en/post/introducing-the-workshop-a-creative-studio-for-bringing-pinterest-ideas-to-life
        - Social image from wallhere
https://wallhere.com/en/wallpaper/1326739
    -	Coming Soon image from Vectorstock
https://www.vectorstock.com/royalty-free-vector/coming-soon-neon-sign-coming-soon-badge-in-vector-21133321
    -	Profile image monkey face placeholder from Pintrest
https://www.pinterest.com/pin/237564949067037097/

- **Acknowledgments:** the inspiration for this project has come from the life of the developer moving 
to Indonesia to start a new life. I’d like to thank my mentor, Sebastian Immel, 
for his suggestions to add to the site. 

