# 
import os;
# f = os.open("function.py","r"); Error
f = open("function.py","r");
# print(f.read()); # param: number of characters

# Access Mode
# R -> Open a file for reading only 
# R+ -> Open a file for reading and writing
# W -> Open a file for writing only 
# W+ -> Open a file for reading and writing
# A -> open a file for appending only
# A+ -> Open a file for appending and reading
# x -> create a file, throw an error, if there is already file
###################################################
# you can add "b" for each one of them It's OK
# rb, wb, ab

# #################################################
# f2 = open("testfile.txt", "r+")
# print("Before Reading Cursor: "+str(f2.tell()))
# print(f2.readlines())

# position = f2.tell();
# print("After Reading Crusor: "+str(position))

# f2.write("\nI want to Reading");
# print(f2.read())

# f2.close()



print(os.getcwd())
print(os.getcwd().split("/")[-1]) # Print Current Directory Only


print(os.listdir())
# you can pass path for know list of items in directory
# by default it give us list of item of current directory
# print(os.listdir().join("")) Error Syntax ( list has not .join() method )

print("\n".join(os.listdir()))


# makedirs for creating depth level of folder

# os.makedirs("testParent/testChild1/testChild2") # Works (Recommended)
# os.mkdir("testParent/testChild1/testChild2") # Doesn't Work

# 

# os.rmdir("testParent") (Recommended)

# os.removedirs("testParent/testChild1/testChild2") (Not Recommended)
# because it will remove folder recursively and that's might be dangerous


from datetime import datetime;
# State of file/folder (information)
print(os.stat("slice.py"))
print(os.stat("slice.py").st_size) # size by byte
last_modi = os.stat("slice.py").st_mtime;

print(last_modi)
print("{}".format(datetime.fromtimestamp(last_modi))) # last modification

# Very Useful Note, for many application need date

# print(os.getcwd())
# print(os.walk(os.getcwd()))

# for d in os.walk(os.getcwd()):
#      print(d)
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#      print("******{}*****".format(os.getcwd()))
     # folder_name = dirpath.split("/")[-1]
     # folder_name = os.path.dirname(dirpath)
     # folder_name = os.path.split(dirpath)
     # folder_name = os.path.basename(dirpath)
#      print("|----Folder Name----| : ", folder_name)
#      if folder_name != 'FORK-THIS-Python-Tutorial-by-Clever-Programmer' or "environments" or "__pycache__":
#           print("Dirctory Path : " , dirpath)
          # print("Dirctory Name : " , dirnames)
          # print("Files : " , filenames)
     # else:
          # print(folder_name)


# Environ
# https://youtu.be/tJxcKyFMTGo?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=854

print(os.environ)
print(os.environ.get("HOME"))
# print(os.environ.get("karim"))

# os.path is very useful methods for dealing with urls, paths
# os.path.join()

folder_name = os.path.split("/temp/text.txt") # return both, dir name, file name
os.path.exists("tmp/") # return true if this path is really real path

print(os.path.isdir("/test/text.txt")) # False
print(os.path.isfile("/test/text.txt")) # True

print(os.path.splitext("/temp/text.txt"));

print(os.path)
print(dir(os.path))

print(__name__)