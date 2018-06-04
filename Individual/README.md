Readme for Single Project

Steps:
1> Copy this whole project to a specific place in your computer.

2> Run this using "python manage.py runserver".

3>Open two windows.
Window1:In your google chrome browser type url: "http://127.0.0.1:8000/login/"  .  
Window2:After that open your google chrome in Incognito mode, enter same url there .

This opens up login Window on both the browsers tabs.

4>Login usernames and Passwords:
For SuperUser:
	Username: cdac
	password: cdac@123
Other User:
	Username:client1
	password: cdac@123
You can create new users also using "http://127.0.0.1:8000/admin/" url. For login here use superuser credentials.

5>Use step 4 login credentials with different users in these two, window1 and window2.

6> This opens up send message page. Now both of these different users can communicate with each other .


Steps For embedding it inside other Project:
1>Copy this messenger directory to your own project, where you want to run it.
2>Add 'messenger' app name to INSTALLED_APPS of settings.py. 
3>Apply this below code to your HTML page, where you want to embed this messenger app/widget.
            <script src="{% static 'widget.js' %}"></script>
4>Append your "ownApp/urls" file. Add this one line .
	path(' ',include('messenger.urls'))

