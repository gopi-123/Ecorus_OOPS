# Ecorus_OOPS
Project to learn OOPs concept


### Assessment

The first assignment is a small assignment to create some basic Objects and show that you understand the OOP. Feel free to add more functionalities to amaze us! This are the requirements:

1- Create a class "Person" in Python, that has 2 attributes (name and age). Also has 2 methods, (apart from the constructors):
  - happyBirthday, that adds one year to the age
  - changeName, changes the name with the new name provided
  
2 - Create the class "Office", 2 attributes (name and peopleWorking), 2 methods and a constructor:
  - contructor, based on the name, and initialize the peopleWorking as empty
  - startWorkingFor, receiving one object of the class "Person" and add it to the peopleWorking
  - finishedWorkingFor, receiving "Person", remove it from peopleWorking
3- Create an object of the class "Office", named Ecorus
4- Create 2 objects of that class (Eduardo and <dev_name>)
5- Make Eduardo and <dev_name> start working for Ecorus
6- Make Eduardo finish working from Ecorus

We would like to see the code developed for each exercise, and a console screenshot showing the result (printing the objects) after every exercise.

The idea of the second assignment is to know a little bit more about your skills, in this case the systems design. The goal is not to have a perfect design, but to show that you are able to design, set up, and have a working system within a reasonable timeframe. Also it is interesting which design guidelines do you follow. So for this purpose, the test is a case to be designed and implemented, and some follow up questions.

The case:
- Using the classes you developed in the Part 1 (People, Office), build an API to encapsulate the access to this entities to interact with them, via an application webserver.

Techs:
- Use a python framework to handle the requests (Django, Flask, Tornado..)
- Use a DB

Where:
- Your choice. Can be your personal computer, or a cloud system (aws, heroku, digitalocean..), or whatever system you find appropriate as long as it is accessible from my PC.

Extras:
- Make RESTful the API
- Add a component to improve the requests handling
- Show the data in the front end

Questions:
- What has been the more difficult part?
- What part of the system could be improved?
- How would you scale it, to be able to handle 1K calls per sec? and to handle 1M?
- How would you automate the testing?
- How would you implement a continuous development system (pipelines) for this particular case?


#### ToDo

Assumed name and age are attributes of class

It was difficult to understand whether name and age  are Class attributes or Instance Attributes