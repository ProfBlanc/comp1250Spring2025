import os
name = "mydir/subdir/child/grandchild"
if os.path.exists(name):
    print(name, "already exists")
else:
    #os.mkdir(name)
    os.makedirs(name)