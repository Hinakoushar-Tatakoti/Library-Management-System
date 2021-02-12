# Library-Management-System
**Introduction**

Library Management System built using python language, which is console based application using text files to store the book and users information.
Which has different features like authentication,authorization,registartion.Librarian(Admin) wants to perform the basic actions such as 
adding a book, remove a book and display a books. Even students and staff can also login and perform actions like disaplay book, search a book, borrow book,
return book and pay a fine.


**Advance Software Engineering**

Hinakoushar Tatakoti

Matriculation no:915584

Data science 1st semester

#### Contents
**1) UML Diagrams.**

Unified Modeling Language is a general-purpose, developmental, modeling language in the field of software engineering that is intended to provide a standard way to visualize the design of a system.

Following are the UML diagrams for Library-Management-System.

[Use case Diagram](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Use_case.png)
The purpose of use case diagram is to capture the dynamic aspect of a system.
Items involved are 1)Functionalities to be represented as use case 2)Actors 3)Relationships among the use cases and actors.

[Activity Diagram](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Activity_Diagram.png)
Activity diagram is basically a flowchart to represent the flow from one activity to another activity. The activity can be described as an operation of the system.
The control flow is drawn from one operation to another. This flow can be sequential, branched, or concurrent. Activity diagrams deal with all type of flow control by using different elements such as fork, join, etc
      
[Class Diagram](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Class_Diagram.PNG)
 It represents the static view of an application. Class diagram is not only used for visualizing, describing, and documenting different aspects of a system but also for constructing executable code of the software application.
 Class diagram shows a collection of classes, interfaces, associations, collaborations, and constraints. It is also known as a structural diagram.

**2) DDD Of LMS**

**3) SonarCloud Metrics.**

SonarCloud is the online service to catch Bugs,Security Vulnerabilities,Code smells in the Pull Requests and throughout code repositories so developer can enhance workflow with continuous code quality.

[Sonarcloud-URL](https://sonarcloud.io/dashboard?id=Hinakoushar-Tatakoti_Library-Management-System)

[SonarCloud-Metrics1](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics1.PNG)

[SonarCloud-Metrics2](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics2.PNG)

[SonarCloud-Metrics3](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics3.PNG)

[SonarCloud-Metrics4](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics4.PNG)

**4) Clean Code Development(5 points  + 10 points of cheat sheet)**



**5) Build Management using Pybuilder.**
I have used PyBuilder to build the LMS project using command called **pyb** and below are the files and image contains the information.

[Build-File](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/master/build.py)

[SetUp-File](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/master/setup.py)

[PyBuilder](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Build_Result.PNG)

**6) Unit-Tests using uinitest.**

I could see the build is successful and individual unittest running with coverage in percentage.

[PyBuilder](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Build_Result.PNG)

**7) Continuous Delivery Travis-CI**

I have used Travis-CI for CI/CD pipeline,for every push new build is triggered, which build the project and publish the code quality to sonarcloud automatically.

[Travis-CI Pipeline-Link](https://travis-ci.org/github/Hinakoushar-Tatakoti/Library-Management-System)

[Travis-CI-Pipeline-Result](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Travis_ci_1.PNG)

[Travis-CI-Pipeline-Logs](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/Travis-CI-logs.txt)

**8) Pycharm IDE**

Previously i worked with jetbrains Intellij already knew shortcut keys which i really liked to use or used, and i'm comfortable with jetbrains IDE's,it has many in-build features, so i decided to use Pycharm for Python development.
   * ctrl+shift+k to push the code git through Pycharm IDE it's so handy.
   * ctrl+E to open recently opened files from the list
   * ctrl+/ add or remove line or block comment

**9) DSL snippet.**

**10) Functional Programming used.**