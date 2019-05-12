<p align="center">
    <a href="https://extremewall.herokuapp.com"><img src="https://github.com/britsja/Full-Stack-Frameworks-with-Django-Milestone-Project/blob/master/Extremewall.png" title="Extremewall" alt ="Extremewall"></a>
</p>

# Extremewall Support Site - Full Stack Frameworks with Django Milestone Project  

The Extremewall support site intends to provide support to users of the Extremewall Firewall. The site also offers the opportunity to request features that users would like implemented
and the option to purchase upvotes in order to boost feature development priority.

To provide transparency, the stats page shows the tickets completed in the previous month and the feature currently being worked on based on the votes it received.

The deployed project can be accessed on heroku at the following link: <a href="https://extremewall.herokuapp.com">https://extremewall.herokuapp.com</a>

#

### **Table of Contents**

[User Experience](#user-experience)

[Features](#features)

[Features Left to Implement](#features-left-to-implement)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Deployment](#deployment)

#
 
### User Experience
 
As users of Extremewall, they need to be able to report any faults or errors with the Extremewall software and deployment thereof.

Extremewall company would like their users to have the following experience on the website:
- A user, without being logged in, needs to be able to see open tickets and feature requests.
- Users that aren't logged in, shouldn't be able to create new support tickets or feature requests
- You need to be able to register and log in as a user to access some features on the site.
- Once logged in, the user will be displayed a profile page containing information about their activity on the website
- A logged in user needs to be able to create support tickets and request new features.
- Logged in users should additionally be able to purchase upvotes for features to prioritise it's development
- A stats page will give the user the ability to see about tickets and features that are open or completed.

#

### Features

- Home Page - Users get a general overview of the product and the option to download it.
- Tickets - Pages for showing open and closed tickets and creating a support ticket. This is the method that users get support for Extremewall
- Features - Also has pages for open and closed feature requests and the ability to create feature requests. Users can pay to boost the upvotes of a feature to boost its development.
- Stats - Displays the previous months' statistics showing averages and daily tickets closed and open feature votes.
- Register, Login and Logout - Users are able to register on the site and login in and out once registered. Registration required to create support tickets and feature requests.
- Profile - Page displays user specific activity on the website relating to tickets and feature requests. 
- Cart - Purchased upvotes of features are added to the cart prior to checking out and paying.
- Checkout - All items in cart can be purchased and purchased votes will be added to the respective features on completion of the transaction through Stripe

#

### Features Left to Implement
- On the home page - Provide a working link to download the Extremewall ISO file for product installation.
- On Tickets pages - Determine if users prefer uploading screenshots when logging support tickets and implement S3 storage for images.
- Stats Page - give users the option to display stats based on previous months too
- Social media icons in the footer of all pages need to be linked to correct social media pages

#

### Technologies Used

- [HTML](https://www.w3.org/html/)
    - DOCTYPE of **HTML** is used for the markup of this project
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    - **CSS** used to style the project
- [JQuery](https://jquery.com)
    - The project uses **JQuery Version 3.3.1** to simplify DOM manipulation.
- [Bootstrap](https://bootswatch.com/darkly/)
    - **Bootstrap 4.2.1** with Bootswatch Darkly theme used for theme and styling of project
- [Django](https://www.djangoproject.com/)
    - Python web framework used is **Django 2.0.13**
- [PostgreSQL](https://www.postgresql.org/)
    - During development SQLite was used but for deployment, we use **PostgreSQL** on Heroku
- [gunicorn](https://gunicorn.org/)
    - **gunicorn** is used on the hosting platform (Heroku) as the HTTP server
- [Stripe](https://stripe.com)
    - To accept payments for feature upvotes, the project uses **Stripe** as the payment gateway
- [Fusion Charts](https://www.fusioncharts.com/)
    - To provide charts on the stats page ** Fusion Charts 3.13.4** is used.
- [countUp](https://inorganik.github.io/countUp.js/)
    - **countUp** slowly counts from 0 to the totals on the stats page

#

### Testing

Manual website testing was conducted to ensure the functionality of the site and the features are working as required. 

Testing conducted were as follows:

1. Home Page:
    - Page opened, scrolled to bottom and tested on different screen sizes using Chrome Dev Tools 

2. Tickets:
    -  Tested if user isn't logged in, menu item to create a new support ticket is greyed out with message that login is required
    -  On "Show Open Tickets" page, tested if user isn't logged in, text is displayed below tickets that login is required to create a ticket
    -  On the "Show Open Tickets" page, ensures that only open tickets are displayed and only closed tickets on the "Show Closed Tickets" page
    -  Entering the page of an open ticket, tested that no option is there to add a comment for users that are not logged in
    -  Tested that if user is logged in, a user can create a ticket from the top dropdown menu or from the "Show Open Tickets" page.
    -  Created a ticket as a logged in user and it displays in the "Show Open Tickets" Page
    -  Tested being able to create a comment on an open ticket as a logged in user
    -  Checked that "Close Ticket" option is available as user that created the ticket and that it closes the ticket and displays it in the 
         "Show Closed Tickets" page.
    -  Tested that as original ticket creator, a closed ticket can be reopened if users' problem hasn't been resolved
    -  As a logged in user that didn't create the ticket, they can't close the open ticket and can't reopen the closed ticket.
    -  Any logged in user can comment on a ticket regardless if they created the ticket or not, as long as the ticket is open.
    -  Logged in user or guest users can't comment on closed tickets
    
3. Features:
    -  Tested if user isn't logged in, menu item to create a new feature request is greyed out with message that login is required
    -  On "Show Feature Request" page, tested if user isn't logged in, text is displayed below tickets that login is required to create a feature request
    -  On the Show Feature Request" page, ensures that only open feature requests are displayed and only closed requests show on the "Show Closed Requests" page
    -  Entering the page of an open feature request, tested that no option is there to add a comment for users that are not logged in
    -  Tested that if user is logged in, a user can create a ticket from the top dropdown menu or from the "Show Feature Request" page.
    -  Created a feature request as a logged in user and ensured that it displays in the "Show Feature Request" page and shows 0 upvotes
    -  Tested being able to create a comment on an open feature request as a logged in user
    -  Checked that "Close Feature Request" option is available as user that created the request and that it closes the feature request and displays it in the 
          "Show Closed Requests" page.
    -  Tested that as original feature request creator, a closed request can be reopened if required.
    -  As a logged in user that didn't create the feature request, they can't close the open request and can't reopen the closed feature request.
    -  Any logged in user can comment on a feature request regardless if they created the request or not, as long as the request is not closed.
    -  Logged in user or guest users can't comment on closed tickets
    -  Open Feature Requests should give the option to Upvote a feature for logged in users. Once clicked, the button should not show anymore for user until logged out again.
    -  Open Feature Requests also gives the option to logged in users to purchase an upvote boost and add them to the cart. 
    -  Open Feature Requests - if no quantity for upvotes are entered and the "Add votes" button is clicked, show error message that value is required.
    -  Open Feature Requests - If upvote quantity is entered and the "Add votes" button clicked, the page redirects to cart and shows all selected upvotes in the cart.

4. Stats:
    -  Stats from the previous month shows as three columns of numbers: "Average Tickets Closed Per Day", "Average Tickets Closed Per Week" and
          "Tickets Closed for Month"
    -  Chart will display the total amount of tickets closed daily for the previous month
    -  The feature with the most upvotes displays as a clickable link that takes the user to the specified feature request
    -  A chart displays the total votes each of the open feature requests has.

5.  Register
    -  The Registration page is accessible from the top right menu
    -  If either of the fields aren't entered, a error message displays
    -  Test that the two password fields need to match to proceed with registration or display an error
    -  If user registers successfully, the page is directed to the new users' profile page

6.  Login
    -  The login page is accessible from the top right menu or from pages that require users to be logged in, like the open tickets and features pages
    -  On the login page, leaving a field empty display an error message
    -  Entering the incorrect information on the page results in an error message "The username or password is incorrect"
    -  If user can't log in or forgot their details, information is provided to assist in contacting the company to assist.
    -  Once the user successfully logs in, they are directed to the profile page.

7. Profile:
    -  Once logged in using the login page, a user is directed to their profile page. The page is also accessible from the menu once logged in.
    -  The username should show next to the welcome message and the last login time of the user must show below it in date and time format.
    -  The three number columns should show the total Open Tickets, Open Feature Requests and Total Comments that belong to the logged in user.
    -  The Tickets tables should show the open and closed tickets belonging to the user. The tickets should be clickable and open the specific ticket.
    -  The Features tables must show the features initiated by the user that are open and closed. Features should be clickable to open them.

8. Cart:
    -  The Cart page is accessible for logged in users from the top right menu or when upvotes are purchased from the feature page.
    -  If no items are in the shopping cart, the Cart page should display a message indicating that.
    -  If there is an item in the cart and the user navigates away from the cart page, the contents of the cart is stored in the session and the user will find
          all items added to the cart when returning to it.
    -  Each item in the cart should have a button to remove that item from the cart. Once the remove item button is clicked, user should return to the updated cart.
    -  Multiple items can be added to the cart and the cards on the page will change the number of items in the row based on that amount
    -  Once the user clicks on the "Purchase Now" button, they should be directed to the checkout page.

9. Checkout:
    -  The checkout page is displayed when a user selects the "Purchase Now" button from the cart page.
    -  Checkout page will display each feature in the cart and the total votes being purchased for each.
    -  Below the features and their votes, the total amount of all the upvotes being purchased should be displayed in dollar currency ($)
    -  The Payment Details on the Checkout page must consist of 2 forms: The payee's details and the card information used for the payment.
    -  If a field is left blank, a message should be displayed that the information is required.
    -  If the card details aren't entered as required, the Submit Payment button will not function.
    -  If the payment from the card details is successful, user is directed to a Payment Successful page with a link back to the open features page.
    -  If the payment fails a message should be displayed indicating the error. This was found not to be working during testing and corrected.
            After the payment fails, user is directed back to the checkout page, displayed the error and given the opportunity to attempt it again.
    -  Tested that purchased upvotes is added to successful payment from checkout and not on failure of payment

10. Browsers:
    - Tested site on both Chrome and Firefox web browsers

11. Responsiveness
    -   Used chrome developer tools to test site responsiveness in various display sizes

12. Bugs discovered during testing:
    - The console was printing out a print statement from the checkout views which was removed
    - The checkout page gave an error when a rejected test card was used. Card error was also not displaying. Corrected as above in checkout section.
    - Debug mode was still enabled in the settings.py which was changed to False after testing the checkout page
    - The stats page displayed a static month (March) instead of previous month
    - The tickets stats chart also displayed the incorrect information. Code was adding up ticket by month instead of by day of month.
    - On the stats page, the hyperlink and description of feature currently worked on, is displaying a feature with the most votes whether the feature
        request is open or closed. It should only show the feature request with the most votes that are still open
    - After changes above, when closing a feature request, error on stats page: NoneType object is not subscriptable
    - Stats page - The ticket closed chart displayed all closed tickets regardless of month.

#

### Deployment


To desploy the project to Heroku, the following steps were taken:

- Created the application on Heroku and called it: extremewall
- On the heroku app page under Resources, added Postgres under the Add-ons section
- Copied the DATABASE_URL from the heroku Config Vars to use in the settings.py
- On the development platform (C9), used the following command to use the Heroku PostgreSQL:
    - ```pip install dj-database-url```
    - ```pip install psycopg2```
- Install the webserver that is required by Heroku
    - ```pip install gunicorn```
- Create a Procfile file in the root of the project and add the following line to the file:
    - ```web: gunicorn extremewall.wsgi:application```
- Capture all the installed applications into the requirements.txt file:
    - ```pip freeze > requirements.txt```
- In the settings.py, added the import entry near the top of the file:
    - ```import dj_database_url```
- Changed the DATABASES entry in the settings.py to display the following:
    ```
    if "DATABASE_URL" in os.environ:
        DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
    else:
        print("DB not found in os environ, using SQLite instead")
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```
- Removed the following entry in the settings.py:
    - ```import env```
- Changed the Debug setting for deployment:
    - ```DEBUG = False```
- Added the heroku app URL to the allowed hosts in the settings.py:
    - ```ALLOWED_HOSTS = ['extremewall.herokuapp.com']```
- The following entries were taken from the env.py and inserted into the Config Vars of the project on Heroku:
    -   SECRET_KEY
    -   STRIPE_PUBLISHABLE
    -   STRIPE_SECRET
- Created the database tables etc on Heroku with the following commands in the terminal on the development platform:
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
- Created the superuser once the database migrations are complete on the Heroku PostgreSQL:
    - ```python manage.py createsuperuser```
- In order to test on the local development environment, added the following entries and their values to the .bashrc file:
    - DATABASE_URL
    - SECRET_KEY
    - STRIPE_PUBLISHABLE
    - STRIPE_SECRET
- Run the server and test if project is connected to Heroku's PostgreSQL which on Cloud 9 is:
    - ```python manage.py runserver $IP:$PORT```
- Once tested and working, start moving the project files to Heroku
- Sync the changed files to GitHub before being deployed to Heroku:
    - ```git add .```
    - ```git commit -m "Changes made for Heroku deployment"```
- On the heroku app dashboard, opened the 'Deploy' tab and selected GitHub under Deployment Method
- In the 'Connect to GitHub' area underneath the Deployment Method, search for the github repository matching the project
- Click the connect button on the correct project
- In the 'Manual Deployment' section, clicked on the 'Deploy Branch' button

To clone this project before following the steps above to deploy it to Heroku, you can use the following command:
    - ```git clone https://github.com/britsja/Full-Stack-Frameworks-with-Django-Milestone-Project.git```
    
In the admin panel:
- Once project is created, usergroup needs to be created with the name of SupportUsers
- Create support categories as required but the support website

On the website - create dummy account and do the following:
- Dummy tickets and features need to be generated for the stats page to work

### Credits

**Media** 
- Google Image Search for images used in this project with reuse rights.

**Code**
- InfoSoft Global Private Limited for the Fusion Charts code used for creating the charts in this project.
- Jamie Perkins from inorganik Produce for the countup code used in numeric counting display of stats.

**Inspiration**
- Code Institute for providing the knowledge and challenge in creating this project.