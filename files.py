# there are two ways to interact with files
# recommended way (using context manager)
# normal way using `open()` function

# f= open("test.txt", 'r');
# print(f.name);
# f.close();

# In This Way we have to remember .close() method
# to avoid any leaks of remaining file is opening


# Second Way

with open("test.txt", 'r') as f2:
     # Do anything for File
     print(f2.mode)

print(f2.closed) # isClosed? Yeah, after context will be closed
# print(f2.read()); # Read Closed File not Allowed!

# outside the file will close automatically
# and if there are any thrown an Error, will close file auto as well

# NOTE f2 variable you have access to it outside context manager, it is OK
# but the file will be closed

############################################################

with open('test.txt', 'r') as f3:
     # 1# (Code)
     # f_contents = f3.read();
     # print(f_contents);

     # if your file is small, so this way works well
     # but if you have extremly large file, and you don't want load all of these content of that file into a memory
     
     # 2# (readlines()) (Code)
     # f_lines = f3.readlines();
     # print(f_lines);
     
     # 3# (readline()) (Code)
     f_chunks = "";
     print(f3.readline())
     print(f3.readline())

     ## Example (Code)
     # for line in f3.readline():
     #      f_chunks+= line;
     # print(f_chunks, end="")

     ## Explaination 
     # by default print() end each statment with new line
     # here you can control that by 'end' argument

     # 4#
     ## Example (Code)
     # for line in range(f3.readlines().__len__()):
          # f_chunks+= f3.readline();

     # print(f_chunks);
     ## Not Expected result

     # 5#
     ## Example (Code)
     # for line in f3:
          # print(line);
          # that's more effiecnt than previous other

     # 6#
     ## Example (Code)
     # f3_part1 = f3.read(30);
     # print(f3_part1, end="");
     # f3_part2 = f3.read(30);
     # print(f3_part2, end="");
     
     # Another Technique
     size_to_read = 30;
     f3_content = f3.read(size_to_read);
     while len(f3_content) > 0:
          print(f3_content, end='');
          f3_content = f3.read(size_to_read);


# To know current Crusor use .tell() method
# to manipulate and determine place of cursor use .seek();

# file3.seek(0);
# this line make cursor begin from 0
# file3.seek(10);
# this line make cursor begin from 10(tenth) character

with open("writetest.txt", 'w') as wfile:
     wfile.write("Welcome to Text File 1\n");
     wfile.seek(wfile.tell())
     wfile.write("Welcome to Text File 2");
# try to avoid using .seek() in writing mode file
# because it is a little confusing

# Example Copy Original File to Copy File

with open("test.txt", "r") as orgFile:
     with open("copy_file.txt", "w") as copy_file:
          for line in orgFile:
               copy_file.write(line);

# we can use previous example for copying Pictures but instead read/write a file by character
# we interact with files as bytes (in case pictures) and we append "b" in our mode to indicate to "binary"

with open("python_pic.png", "rb") as picture:
     with open("copy_file.png", "wb") as copy_file:
          # 1#
          # chunk_size = 4096;
          # picture_chunk = picture.read(chunk_size);
          # while len(picture_chunk) > 0
          #      copy_file.write(picture_chunk);
          #      picture_chunk = picture.read(chunk_size);

          # 2#
          # you can use another extension like .txt to inspect decoding
          for byte in picture:
               # print(byte)
               copy_file.write(byte);


# Watch out!
# TypeError: a bytes-like object is required, not 'str'


# Important Lessons
# Temporary Files, Memory Files, Text File, Byte File (Images)
# understand this error: 'utf-8' codec can't decode byte 0xff in position 0
# this error was result reading/writing text mode on on images objects
# "w", "r" -> "wb", "rb"