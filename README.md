## Introduction

Project McQueen is a fun and interactive web portal to allow students to create their own challenges on a real life car. The web portal stimulates critical and logical thinking in students by forcing students to think of a way to get their car to the finishing line in the least amount of turns as possible. Critial and logical thinking is an important skill in programming and we hope to introduce students to programming in a fun and meaningful way with Project McQueen.

## How To Run

In order to run our application, make sure python 3.9 is installed on your system and execute the following command.

```pip3 install -r requirements.txt```

This will install all requirements that are needed for the application. Finally, execute the following command to start the server.

```python3 app.py```

This will start the server. Navigate to localhost:5000 to view the web app.

## Development Workflow

Github has been a very big part of our team's effort to collaborate with each other during the development of this application. Our project makes use of Github's project board to track our tasks and backlog. The issues feature allow us to assign people to different tasks as well. In addition to the documentation features, we make use of Github's Pull Request feature to manage our codebase. Our code base is split into 2 branches, Master and Develop. All development work by the team is done on each team member's feature branch before opening Pull Requests for reviews and merging into the develop branch. Weekly releases are tagged and released on Github under the releases section, this allows us to fall back on a backup if necessary.

For more information about our git workflow, please refer to flow.md.

## User Acceptance Testing

- Include an updated use case diagram and system state diagram if there are changes made based on M2. Highlight the changes clearly.
- An embedded video that runs through all the system test cases you have created (and refined) from M2
- ~3 mins long to cover all system tests

## Whitebox Testing

- choose one meaningful class to demonstrate your test code. “Meaningful” here means 2 or more interactions with other classes, e.g., a Control class. Please do not use an Entity class.
- list the test cases for this test suite (for this one class) and where they reside in your repo
- show code coverage statistics for each test case, including an explanation of how you have generated these statistics (whether manual, through a lib, or via the IDE)
- provide instructions how to run the test suite
- embed an animated gif or another short video (~1 min) of the test case being ran

For our whitebox testing, we selected the CarManagement control class. This control class encompasses the instructor login and the car connection which are ip.py and authenticate.py respectively. For each of the python file, we manually created test cases that will cover as much lines of code as possible. After creating the test cases, we used Coverage.py to test for code coverage. The results of this can be seen in CoverageReport.txt and in index.html inside the htmlcov folder.

To run the tests, execute the following commands in sequential order

```coverage run authenticate_test.py```
```coverage run -a ip_test.py```

To generate the report, execute the following commands in sequential order

```coverage report```
```coverage html```

Coverage report will print the results directly in the terminal while coverage html will generate a website for easier viewing.

## Test Case Video
