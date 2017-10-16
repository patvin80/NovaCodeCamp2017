# Nova Code Camp 2017
Basic Flask Repository for starting the Nova Code Camp

## Sponsors 
[Sponsors List](https://drive.google.com/file/d/0B-4OXcyEUdEIeW9nX0Q5WTFJbXFDQUN3Ul8zWDIxWnJFQkg4/view?usp=sharing)

## About Me
[LinkedIn](http://www.linkedin.com/in/pvinit)

## Talking About
Why should you be here: [Fastest Growing Programming Language](http://www.techrepublic.com/article/which-is-the-fastest-growing-programming-language-hint-its-not-javascript/)

Python Flask is a Web Framework to develop Restful Endpoints and Enterprise Applications using Python as the programming language. Dockerizing the application facilitates the resolution of production issues as it makes your MacOSX or Windows environment behave like the Linux environment in which the applications are hosted.

## Basic Instructions:

1. pip install virtualenv
2. git clone 
3. cd NovaCodeCamp2017
4. virtualenv venv
5. source venv/bin/activate
6. venv/Scripts/Activate.bat (for Windows)
7. pip install -r requirements.txt
8. cd static
9. npm run build
10. cd ..
11. python FlaskBasicAppStart.py 
12. navigate to http://127.0.0.1:5000

## Advanced Instructions
1. export FLASK_APP=FlaskBasicAppWithConfig.py
2. export FLASK_DEBUG=1
3. flask run
4. Navigate to http://127.0.0.1:5000

## React Integration
Here is a reference to a great article that explains the Integration of REACT into the application.
[Link Here](https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9)

## Docker Environments:
Dockerize the Environment -- https://github.com/tiangolo/uwsgi-nginx-flask-docker
1. Docker File - Infrastructure as Code
2. Docker File walkthrough
    1. from specifies the image that you want to work with
    2. COPY specifies that copy the contents of the current director to the app folder on the image
    3. RUN executes commands on the images
    4. Additional RUN Commands in the Dockerfile-dev to ensure that the uwsgi file is replaced appropriately.
3. Apart from the Docker Files, docker also gives a Docker Compose mechanism to structure your infrastructure using yml syntax.
    1. services indicates the machines
    2. Dependency can be indicated
    3. Configuration of the Postgres environment is setup in the Postgres DB and ensures that all environments are consistent
4. The image for Python Flask with UWSGI configuration needs uwsgi.ini file setup
    1. The Development environment has Command to run flask in debug mode locally to ensure that the local code changes would be reflected immediately
    2. The Production environment has uwsgi nginx environment configured
    3. The module and the app name have to be configured. The default value expected is "application" for callable.
    4. The callable is the file name in which the app is created in our case FlaskBasicAppWithConfig

## Docker Environment Execution
### Development
1. docker-compose -f docker-compose-dev.yml build
2. docker-compose -f docker-compose-dev.yml up
3. Navigate to http://127.0.0.1:4444 -- Port 4444 has been mapped to port 80 of the Docker Container
4. Change code and watch the code changes being reflected.

### Production
1. docker-compose build
2. docker-compose up
3. Navigate to http://127.0.0.1  -- Port 80 has been mapped to port 80 of the Docker Container.

## Instructions for AWS CodeStar

1. AWS CodeStar is an AWS Service
2. Needs a Custom IAM Login with permissions to CodeStar
3. Make Modifications to the application.py file
4. Make changes to the install_dependencies.sh file
5. Make changes to the appspec.yml file to ensure that the file permissions are managed

## Contact Information
  Author: Vinit Patankar [LinkedIn](http://www.linkedin.com/in/pvinit)
