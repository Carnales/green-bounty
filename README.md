# green-bounty
Environmental bounty program for the ThetaHacks hackathon.

The world is at a state of peril. On one side COVID-19 is shattering lives and relationship alike, and on the other hand 
our environment is decaying to the point of no return. We thought to ourselves, how do we make the best of this? Or as 
Rohan Bansal would say, how can we, ThetaHackers, impact our world? What better way to do just that than foster local
change with an environment bounty platform! Join us to see more...

## Guide
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/wwTFL5zMVSs/0.jpg)](https://www.youtube.com/watch?v=wwTFL5zMVSs)

## Setup

* Download the project either as a zip or through GitHub Desktop.
* In your terminal, "cd" into the root directory.
* Now, download the dependencies with:
```
pip install -r requirements.txt
```
* Now, "cd" into the Green Bounty folder and run the django server through:
```
python manage.py runserver
```
Note: If you get windows socket errors, run 'python manage.py runserver 8080' instead to run it on a different port.
* It should be all ready, now just open your favourite browser (it better not be IE) and open: "localhost:8000" or "127.0.0.1:8000".

## Functionality
* Login & register your account to our SQLite3 database as a first time user!
* Search for your city to find current bounties! (Current ones in database: San Francisco, Mexico City, Shanhai)
* Claim your bounty by clicking on it and sending your submission (to be reviewed for fraud!!)
* Create a bounty with either the "plus" button or from the sidebar!
* Navigate the sidebar, with different options, including an account page.
* Lastly, if you really want to leave, you can log out form the sidebar.

## Post ThetaHack
-  Add Organization Support
-  Add Organization and User Page Backend Support
-  Add PayPal Integration
-  Add a dynamic search feature
-  Add a map feature

## Bootstrap codebases adapted from:

- "Help with flow.py" - https://github.com/django/django/blob/master/django/contrib/auth/forms.py

- "Wikipedia Viewer[freecodecamp]" - https://codepen.io/arshdkhn1/pen/pymzWz

- "SideNav" - https://codepen.io/miguel96/pen/oxddqb

- "Bootstrap 4 Animated Login Form" - https://bbbootstrap.com/snippets/animated-login-form-95290954

- "Bootstrap snippet. user profile bio graph and total sales" - https://www.bootdey.com/snippets/view/user-profile-bio-graph-and-total-sales#html
