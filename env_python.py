# What is env in Python
# env help us to separate different python environment for different projects

# if we have multiple projects and each of them depend on packages
# for example one of projects using flask old version, and another uses new version

# if i go upgrade this package in general
# may break this project which uses old version

# so the solution is isolated each project with own environment
# which contains only the dependencies and packages that they need

# Steps:
# 1- pip install virtualenv
# 2- cd <Location_Project>
# 3- virtualenv <Name_of_Project>/
# to Activate virtual env
# 4- source <Name_of_Project>/bin/activate

# then it will appear in above of terminal you use specific environment

# when we type >>> which python
# output <Location_Project>/<Name_of_Project>/bin/python

# when we type >>> which pip
# output <Location_Project>/<Name_of_Project>/bin/pip

# if we type pip list
# it will output few packages by default
# pip list

# you can now install your packages in separated way, not conflict on other your projects
# pip install numpy (example)

# if we want export these packages to another environment/project
# pip freeze --local > requirements.txt

# why we typed --local?
# because we can access global environment to get the packages
# so to avoid deal with global env instead local
# we have to type --local to print these local packages into file is called requirements.txt
# 
# to import/install these packages in another environments
# 
# before that of course we have to quit from current environment
# we can do this by typing >>> deactivate
# which python
# output : /Users/karim/bin/python (Global environment)
# 
# then type new env >>> virtualenv project2
# source project2/bin/activate
# install packages which we stored
# by typing this >>> pip install -r requirements.txt



# to remove our local env >>> rm -rf <name_environment> 


# To Specify Version of Python in specific environment
# we use virtualenv -p /usr/bin/python2.6 <name_project>
# ti ensure version of python
# after did that type >>> python --version
# -> python 2.6.9


# 