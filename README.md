#Building an API in Flask

The point of this tutorial is to show how to create a RESTful API using
Python Flask.

###Flask Installation Process

(1) Create a new directory and change into it.

(2) Install Pip

- Download https://bootstrap.pypa.io/get-pip.py
- Run ``python get-pip.py`` (sudo, if you aren't on Windows)

(3) Install virtualenv

- ``pip install virtualenv``
- Within your project directory, run ``virtualenv flask-demo``
- Activate the virtual environment by running 
  - Mac/Linux: ``source flask-demo/bin/activate``
  - Windows: ``\flask-demo\bin\activate``

(4) Install flask and sqlalchemy

- ``pip install flask`` (dependencies included, yay!)
- ``pip install sqlalchemy``

(5) (Windows only) Install sqlite3, if you haven't already

  - [Instructions](http://www.tutorialspoint.com/sqlite/sqlite_installation.htm)

Eventually, to leave the virtualenv, run ``deactivate``

###Resources

Miguel Grinberg is a god of Flask tutorials:

- [Designing a RESTful API with python and flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask). Touches on error handling, authentication, and best practices.

- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). An 18-part Flask tutorial that walks through the construction of an entire blogging site.

For (very) quick-and-dirty deployments, you can forward localhost to a public
URL using ngrok:

- [ngrok.com](https://ngrok.com/)

I have no idea if this is a "good example" or not. I don't think Flask leads
to as much dogmatism in structure as large MVC frameworks like Django and Rails.
 Clearly you want to write readable, useful code, and make it clean, but the
 Flask use-case really shines when you would rather be spending your time
 doing something else, like clustering _everyone on Github_:

- [The Open Source Report Card](http://osrc.dfm.io/) ([source](https://github.com/dfm/osrc))
