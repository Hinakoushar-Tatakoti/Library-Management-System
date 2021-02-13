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

The domain driven design approach is used for complex needs, connecting the implementation to an evolving model of the core business concepts. It puts the focus on the problem domain and basically helps identify the architecture and inform about the mechanics that the software needs to replicate.To create a Library Management System,I have a good understanding of what library is all about, and the domain of library.

**3) SonarCloud Metrics.**

SonarCloud is the online service to catch Bugs,Security Vulnerabilities,Code smells in the Pull Requests and throughout code repositories so developer can enhance workflow with continuous code quality.

[Sonarcloud-URL](https://sonarcloud.io/dashboard?id=Hinakoushar-Tatakoti_Library-Management-System)

**1. Reliability Metrics:**

Reliability metric analyze new bugs(number of news bugs issues in source code.

[Reliability](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics1.PNG)

**2. Security Metrics:**

Security metrics find vulnerabilities and new vulnerabilities in source code.

[Security](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics2.PNG)

**3. Duplication Metrics:**

There are no duplication(line duplication, files duplication, blocks duplication) in the LMS project code.

[Duplications](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Sonar_metrics3.PNG)


**4) Clean Code Development(5 points  + 10 points of cheat sheet)**

Clean code means code should be as efficient, readable, and maintainable as possible, and instead of only solving the problem or focus on the design of your code, on architecture. Easy to understand the flow of entire application, easy to understand role and responsibility of each class, easy to understand what each method does , what is the purpose of expression and variable and easy to fix bugs.It makes easy to maintain,test,save som extra cost etc.

[CheatSheet](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/task/CheatSheet.pdf)

**1.Use of meaningful and pronounceable variable names**

[Meaningful_name](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_Naming_convetions.JPG)

**2. Custom Exception Handling for better eadable and code maintainance**

[Exception_Handling](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_Exception_Handling.JPG)


**3. Use of constant File or Constant variables**

[Constant File](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_CostantFile.JPG)

[Constant variables_usage](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_constant_usage.JPG)

**4. one def serves one purpose**

[One_pupose](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_One_purpose.JPG)

**5. use of decorators**

[Decorators](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_Decorators.JPG)
	

**5) Build Management using Pybuilder.**
I have used PyBuilder to build the LMS project using command called **pyb** and below are the files and image contains the information.	

[Build-File](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/master/build.py)

[SetUp-File](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/master/setup.py)

[PyBuilder](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Build_Result.PNG)

**6) Unit-Tests using uinitest.**

I could see the build is successful and individual unittest running with coverage in percentage.

[Unittests](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Build_Result.PNG)

**7) Continuous Delivery Travis-CI**

I have used Travis-CI for CI/CD pipeline,for every push new build is triggered, which build the project and publish the code quality to sonarcloud automatically.

[Travis-CI Pipeline-Link](https://travis-ci.org/github/Hinakoushar-Tatakoti/Library-Management-System)

[Travis-CI-Pipeline-Result](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Travis_ci_1.PNG)

[Travis-CI-Pipeline-Logs](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/task/Travis-CI-logs.txt)

**8) Pycharm IDE**

Previously i worked with jetbrains Intellij already knew shortcut keys which i really liked to use or used, and i'm comfortable with jetbrains IDE's,it has many in-build features, so i decided to use Pycharm for Python development.
   * ctrl+shift+k to push the code git through Pycharm IDE it's so handy.
   * ctrl+E to open recently opened files from the list
   * ctrl+/ add or remove line or block comment

**9) DSL((Domain specific language) snippet**

 DSL is a programming language or specification language dedicated to a particular problem domain, a particular problem representation technique, and/or a particular solution technique.Popular examples of DSL are SQL, HTML, XML, UML etc. LMS project used "regular expression" as a DSL.
 
 1. Regular expression:
 
A regular expression is a sequence of character that helps you to match or find other strings or set of strings, using a specialized syntax held in pattern. Regular expression used as a DSL in this project code. Regular expression used to match the valid chars, password strength and email pattern from user inputs.
 
 [Regular Expression](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/DSL_RegEx.JPG)

**10) Functional Programming used.**

Below are functional programming i have used in my LMS project

**1. Final data structures**

Some variables have been made immutable in project code.

[Final Data Structure](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Final_DS.JPG)

**2.Side effect free functions**

Side effect are operation that change the global state of a variable or expression. All assignment and input/output operators considered side effects. Here I used function programming in project code, which has no side effect and mostly in functional programming , function have no side effects. Following is an example of side effect free function.

[Side Effect Free Function](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_Side_Effect_Free.JPG)


**3. Higher-order functions**

A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e, the functions that operate with another function are known as Higher order Functions. It is worth knowing that this higher order function is applicable for functions and methods as well that takes functions as a parameter or returns a function as a result.

Decorators are the most common use of higher-order functions in Python. It allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

I have used decorators , fine_calc_decorator is callable function and calculate_fine is actual function inside the wrapper function.

[High-Order-Function](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/CCD_Decorators.JPG)

**4. Functions as parameters**

In the example below, a function is assigned to a variable user_username_pass_check. This assignment doesn’t call the function. It takes the function object referenced by user_condition and creates a second name pointing to it, user_username_pass_check.

[Function Stored As Variable](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_Stored_As_var1.JPG)

[Actual Function ](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_Stored_As_var2.JPG)

Below example shows functions that can accept other functions as arguments.validate_type is a function which accepts valid_usertype_check function as param.

[Function being called](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_As_Func_param1.JPG)

[Function_used](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_As_Func_param3.JPG)

[Actual_Fnction](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_As_Func_param2.JPG)


**5. Anonymous functions**

Lambda is an anonymous function. Lambda function used when we don’t want to write full function like def . A lambda function can take any number of arguments but can only have one expression. Assign the lambda expression to a variable, it works like python function. Lambda function used in this project code.

[Lambda](https://github.com/Hinakoushar-Tatakoti/Library-Management-System/blob/main/images/Func_Lambda.JPG)



