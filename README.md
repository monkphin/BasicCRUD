Project Brief

To create a web application that integrates with a database across two tables and demonstrates CRUD functionality.- To utilise containers to host and deploy your application.- To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application

Technologies:

Python
Pytest
Flask
Docker/Docker Compose
MySQL
NginX
Linux

The MVP for this project is a website that allows create read update delete functionality on a basic book logging page. This must include SQL, Python, HTML, Docker, Flask.

Project management

Initial planning took place over several days, outlining such things as user story’s, (As a, I want, so that), user Journeys, showing process flow of the users experience from accessing the site, through to adding and updating content. These allowed me to assess and determine what the MVP would require via MoSCoW Prioritisation (must haves/should haves/could haves and wont haves.)

Tools such as Miro and Jira were used to facilitate the planning of the project, with screen grabs from the planning phase shown below. 

![Miro Board for User Journeys, MoSCoW, etc. ](https://github.com/monkphin/BasicCrud/blob/main/readme_img/miro.png?raw=true)
![Jira for KANBAN and Sprint planning, showing sprint 1.](https://github.com/monkphin/BasicCrud/blob/main/readme_img/Jira_planning.png?raw=true)
![Jira for KANBAN and Sprint planning, showing sprint 2.](https://github.com/monkphin/BasicCrud/blob/main/readme_img/jira_basic_function.png?raw=true)
![Jira for KANBAN and Sprint planning, showing sprint 3.](https://github.com/monkphin/BasicCrud/blob/main/readme_img/Jira_core_function.png?raw=true)
![Jira for KANBAN and Sprint planning, showing sprint 4.](https://github.com/monkphin/BasicCrud/blob/main/readme_img/Jira_enhanced_core.png?raw=true)
![Jira for KANBAN and Sprint planning, showing sprint 5.](https://github.com/monkphin/BasicCrud/blob/main/readme_img/Jira_post.png?raw=true)

Once the initial planning was done with, I could start to design the core functionality of the app - based off the priorities and needs outlined by the user stories and MoSCoW, I was able to design the below SQL DB, where I would have user credentials, for login information, User data, for less sensitive data such as names, etc. Then two tables for the specific user data content, specifically the Collection list and the table used to segment content by game system, publisher etc. 

![SQL Table relationships. ](https://github.com/monkphin/BasicCrud/blob/main/readme_img/SQL_relationship_tables.png?raw=true)

As I Was working on the project, it gradually became apparent that I had perhaps bitten off more than I could chew, in terms of the amount of time we had available to us due to various disruptions caused by missing tutors, having no less than 7 tutors on a 9 week course each with their own learning styles and often no real information as to what we had covered previously, as well as periodic disruptions caused by a tutor having to often given 1:1 help, sometimes running into an hour or two of time each day, which overall ate around a weeks’ worth of time over the 9 weeks the course ran for. The  final project was also something that the class had to take the lead on starting due to the tutor not really being informed of this aspect prior to taking us (Not something I can blame him for, so much as just information not being disseminated by management.) - combine this with working a full time job alongside the course and it becomes apparent why I was having issues with completing my own project in the time allotted. So would unlikely be able to complete this in time for the end of the course. (At this stage we were looking at around 1 week left to the cut-off date.) Rather than completely abandon it, it is going to continue to be worked on as a long-term project, allowing me to take my skills development further with no time constraints in terms of a completion date. This project can be found here: https://github.com/monkphin/FlaskAPP



As a class it was decided that we'd spend the remaining time left on the course working towards completing our various projects - with support from our tutor - as a group we started to create a simple news stand application, allowing for news sites to be viewed by reading a MySQL DB, with addition, edit and removal of data being performed in PhpMyAdmin. Being smaller in scope than my own plans, I decided that the best approach would be to take the basic framework this provided and expand on it to implement full front end CRUD functionality, allowing the DB to not only be read, but added to, edited and have content removed from via the site itself. This would allow me to test my skills, while not working on something overly complex and likely to take more time than I had available to me. It also serves as a good way to reflect on what areas I need to improve on in terms of writing Python so I can either revisit recordings from the class or seek further learning materials on the Cloud Academy site, or other learning resources. 

My Application. 
In order to develop the application, I have been running an Ubuntu Server VM on a BareMetal Hypervisor (ESXi) running on a physical machine I host at home, I then used Visual Studio Code as an IDE to edit content via SSH connectivity. 

The application is written in a mix of Python and HTML, utilising JINJA as a method of passing data between the front end and back end, in order to have the content read or written from a MySQL DB. The WebApp, MySQL DB and an Instance of PhpMyAdmin are all running on their own Docker containers, which are spun up using a docker-compose file and a dockerbuild file. To ensure the MySQL DB data is not lost when stopping the DB container, a Docker Volume is created to give permanence to the data stored to the DB. 

![Simple SQL Table relationships. ](https://github.com/monkphin/BasicCrud/blob/main/readme_img/simple_db.png?raw=true)

Stripping back the number of tables in use allowed for a much simpler design overall, which sped up my ability to get core functionality in place. 

Testing

As it stands, the app still has some issues, which I am ironing out, specifically a redirect when trying to edit content, which is failing to load content as the information no longer exists in system memory at this stage. As such testing is quite limited, as I am unable to fully unit test the application. 

As such Jenkins is showing expected failures on stage 3, where unit testing is to be performed, which prevents it starting stage 4, where the containers would be torn down. This being said, since Jenkins and Unit testing was rushed on the course, it’s not something I have enough insight to, to be able to pick up and work with, with minimal time left available to me, so suspect I would have potentially had failures from the Unit testing phase anyway. 

![Jenkins Stage View. ](https://github.com/monkphin/BasicCrud/blob/main/readme_img/Jenkins.png?raw=true)

The app is currently live and running on containers hosted in the previously mentioned Ubuntu Server VM on a BareMetal Hypervisor and can be accessed using NginX Reverse Proxying at the following URL: https://news.dasburros.co.uk where functionality can be tested on a live and working platform - please be aware that there is a known issue with the edit function, which I intend to resolve soon. 

A video demo of the current build of the app can be found here. 
https://youtu.be/kDdtcI4HiRY



Going forwards, I have longer term plans for my own application, where I plan to add additional functionality, such as tracking a paint collection, creating painting recipes - both for colour mixing and actual miniature painting. An army builder, for various tabletop games, combined with rules for each unit, pulled form a third-party source (Wahapedia), in the form of Excel Files, which will be pulled when a change to the content is detected. I also intend to add a picture library for completed miniatures as well as a potential blog facility and methods to allow users to interact with each other - something I anticipate to be an ongoing endeavour where development is concerned.
