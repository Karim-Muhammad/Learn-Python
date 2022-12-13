import os;

# Files

# os.rename("rname1.txt", "rename1.txt");
# os.rename("rname2.txt", "rename2.txt");

# os.remove("rename1");


# folders
# os.mkdir("./test_folders")


# cd == chdir === Change Directory

os.chdir("../")

# cwd
# print(os.getcwd())

# remove
# os.rmdir("test_folder")

# os.rmdir() without argument, will remove current directory by default

import time

os.mkdir("temporary_dir");

time.sleep(4) # 4 seconds

os.rmdir("temporary_dir")