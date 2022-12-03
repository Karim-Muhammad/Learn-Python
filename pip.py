# pip help === pip -h
# pip search === pip_search === poetry search
# pip install <Package_Name>
# pip list

# to check latest version for all packages
# pip list -o ( -o === --outdated )

# if you want upgrade your <Package>
# pip install -U <Package_Name>

# if you want provide for people all packages that they need for that project
# 1# you can install manually one-by-one separated by "comma"

# 2# you can use "freeze" command
# which outputs all packages you have with requirement format
# pip freeze

# if you want store these packages, versions within a file
# pip freeze > requirements.txt

# if you want read this file
# cat <File_name> || nano <File_name> || Vim || notebad ||...

# so after you store your requirement within a file, what then??
# you can send it to another someone, developer to install these packages

# How?
# BY this command
# pip install -r <Requirement_File>

# -r => (refer to requirements)


# Last Trick here
# If you Want Upgrade many Packages you have
# You will do it manually? Of Course Not
# We Use this Command as it is

# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U

# (pip freeze --local) -> refer to only local packages
# (grep -v '^\-e') -> Grep is a Linux / Unix command-line tool used to search for a string of characters in a specified file. The text search pattern is called a regular expression. When it finds a match, it prints the line with the result. The grep command is handy when searching through large log files.

# for example
# pip freeze --local | grep '^y'
# will filter all packages which produced in left hand pip to match regular expression
# ^y
# means it will output only files which start with letter "y" like "youtube-dl", ... 
# but -v in grep [-v] refer to invert following regex, produce all files which not match regex

# like if i pip freeze --local | grep -v '^y'
# thats means produce all files which does not start with "y"
# it won't produce now "youtube-dl"!
# 

# ls snap | grep 'c'
# it will outputs only folders which contains letter "c"


# Now Part 3
# (cut -d = -f 1) -> refer to (do cut separate between version number and filename)
# to contain all filenames only without version number

# Last Part 4
# xargs -n1 pip install -U

# Take all produced filenames which produced previous pip
# then loop through it, to run one at a time, and install -U for each one of them

# NOTE
# You don't build your project within environment!
# it is just for you to use specific version or specific packages you select on your project
# just create your environment, and activate it
# then build your files of project in same directory, not within environment