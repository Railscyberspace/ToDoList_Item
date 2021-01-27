# Django_Project

#From the command line, cd into a directory where you’d like to store your code, then run the #following command:

#django-admin startproject mysite

#Note

#You’ll need to avoid naming projects after built-in Python or Django components. In particular, #this means you should avoid using names like django (which will conflict with Django itself) or #test (which conflicts with a built-in Python package).

#Let’s look at what startproject created:

#mysite/
#manage.py

# mysite/

# **init**.py

    #    urls.py
     #   asgi.py
      #  wsgi.py




       # The development server¶


        #Let’s verify your Django project works. Change into the outer mysite directory, if you #haven’t already, and run the following commands:
        #python manage.py runserver

        #You’ll see the following output on the command line:

        #Performing system checks...

#System check identified no issues (0 silenced).

#You have unapplied migrations; your app may not work properly until they are applied.
#Run 'python manage.py migrate' to apply them.

#January 22, 2021 - 15:50:53
#Django version 3.1, using settings 'mysite.settings'
#Starting development server at http://127.0.0.1:8000/
#Quit the server with CONTROL-C.

#Note:

#Ignore the warning about unapplied database migrations for now; we’ll deal with the database #shortly.

#Changing the port

#By default, the runserver command starts the development server on the internal IP at port 8000.

#If you want to change the server’s port, pass it as a command-line argument. For instance, this #command starts the server on port 8080:

python manage.py runserver 8080

#Adding items in the database run this command:
python manage.py shell.
t1 = ToDoList(name = "first List")
t1.save()

t2 = ToDoList(name = "second List")
t1.save()

#filtering items in the database
t.filter(name_startwith = "sunday")
t.filter(id = 2)

#Deleting items on the ToDoList
del_object = t.get(id =1)
del_object.delete()

#creating Admin login
run this command:
python manage.py createsuperuser
1.on the browser paste the the local address/admin

#follow steps by creating a password
