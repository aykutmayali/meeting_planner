# meeting_planner
## #Django #Python Project

# Starting Django Project
-----------------------------------------------------------------------------------[step-1]

- python -m pip install django

- django-admin startproject meetingRoom

- cd meetingRoom

- python manage.py runserver

(winerror 10013) : close firewall | cmd : ipconfig /flushdns + netsh winsock reset


# Setting up Basic Web Page
-----------------------------------------------------------------------------------[step-2]

- python manage.py startapp website  //must be in the same directory og manage.py
// include website folder , __init.py and views.py stays others removed
// each app is a package which has their own views,url mapping, models, templates

- add urls.py website.views welcome function

--> mark the outer folder as a source root 

http://127.0.0.1:8000/welcome.html
--> modifications in views.py(website) ,urls.py(meeting_planner), setting.py(meeting_planner)
- ctrl+c stops server


# Setting up Data Model
-----------------------------------------------------------------------------------[step-3]

- python manage.py showmigrations
- python manage.py migrate
- python manage.py dbshell   	--> sqlite> .tables--> this will show tables created at db. 
			     	--> select *  from django_migrations;
				-->.exit

--> create a new app for data models
- python manage.py startapp meetings
--> folder meeting_planner --> settings.py --> INSTALLED_APPS add 'meetings'
--> apps.py , tests.py removed in the folder of meetings
--> modifications in models.py(meetings)

- python manage.py makemigrations  # create Meetings in migrations
-->Migrations for 'meetings':
  	meetings\migrations\0001_initial.py
    	- Create model Meeting
- python manage.py sqlmigrate meetings 0001  #(for creating table for new migrations) sqlmigrate + name of app + name of migration
(migration script is not written in sql , it is independent from actual backend)
--> 	BEGIN;
--
--	Create model Meeting
--
	CREATE TABLE "meetings_meeting" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "date" date NOT NULL);
	COMMIT;

- python manage.py migrate
- python manage.py dbshell
--> sqlite--> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            meetings_meeting (appname _ class name) # added 
auth_user_user_permissions
--> sqlite> .exit

-->model classes are mapped to tables, fields are mapped to columns

--> Migration Workflow
#1 change model code
#2 generate migration script (python manage.py makemigrations)
#2.1 show migrations (python manage.py showmigrations) (optional)
#3 run migraitons (python manage.py migrate)

-->adding new columns to models.py
- python manage.py makemigrations

### for migration problems, remove all in meetings-->migrations-->0001,0002 ,..(not __init__.py) and db db.sqlite
- python manage.py makemigrations
- python manage.py migrate  //all models in same migration file(0001_initial.py)


### Admin Interface
--> meetings --> admin.py -->modificaitons for models registering by admin
- python manage.py createsuperuser 	//(lenovo,lenovo@django.com, lenovo123*)



# Setting up Model View Template
-----------------------------------------------------------------------------------[step-4]

- adding html (template) file 
--> create files in website --> templates -->website --> new html5 file welcome.html
--> make modifications in --> website -->views.py

-->Templates : components that display data to the user , should be in folder /templates inside app
-->render : pass request and name of template file
-->third argument : dict with data passed to the template

--> create folder in -->meetings-->templates-->meetings-->detail.html
--> modifications on -->meetings-->views.py & -->meeting_planner-->urls.py


-->Retrieving Model Data 
--> model classes have a .objects attribute --> meetings = Meeting.objects.all() //get all objects
						meetingFive = Meeting.objects.get(pk=5)


--> for loop in html file  {% for meeting in meetings %} {{meeting.id}} {% endfor %}

--> <a href="{% url 'detail' meeting.id %}"> {{ meeting.title }} </a>   url tag generates dynamic urls

--> add a new page : for viewing rooms
	-view
	-template
	-url mapping

	--> meetings/views.py : def rooms_list(request): --> pass request with Room object 
	--> meetings/templates/meetings add rooms_list.html
	--> meeting_planner/urls.py : path('rooms', rooms_list, name='rooms')

--> add a new python file to meetings: urls.py for list of url mappings



# Styling
-----------------------------------------------------------------------------------[step-5]

- adding css styling
#1 create a css stylesheet
#2 apply css to html
#3 template inheritance

--> website/ add 'static' folder --> add 'website' folder --> style.css
--> in welcome.html add <img src="{% static 'website/calender.png' %}" width="100px">
--> for html template (for applying css to all html files) --> website-->templates--> base.html
  --> modify welcome.html with deleting header part and using {% extends "base.html" %}
{% block title %} Welcome {% endblock %}
{% block content %} rest of welcome.html body {% endblock %}
	

# User Interaction
-----------------------------------------------------------------------------------[step-6]

- Adding meetings
- form template
- modelform
- view for processing form data - validate - save - redirect

--> add meetings-->templates--> meetings--> new.html -->def new(request): in views.py
### meetingform is a class modelform_factoryhelps create new class called ModelForm
 -->it creates and process html forms, based on Meeting class
 -->url mapping --> path('new', views.new, name="new")
