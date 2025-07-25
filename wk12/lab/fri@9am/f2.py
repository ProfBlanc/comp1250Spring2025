import zipfile

with zipfile.ZipFile('my_collection.zip', "r") as f:
    #f.extractall()
    # f.extractall("my_dir")
    f.extract("toy_1.txt", "this_dir")