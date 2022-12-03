print("Imported my Module...");
test = "Test String";

def find_index(to_search, target):
     """Find index your element within target element"""
     for i, val in enumerate(target):
          if to_search is val:
               return i
     return -1;

print(find_index("m", "Karim"));

# When we import a file in another file, you execute entire file

public = "public";
_private_var = 10
__accessable = 20;