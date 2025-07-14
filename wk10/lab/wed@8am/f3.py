import os

print(os.name)
print(os.sep)
print(repr(os.linesep))

folder_name = "test1/test2/test3/test4"
if not os.path.exists(folder_name):
    #os.mkdir(folder_name)
    os.makedirs(folder_name)