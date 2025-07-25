import zipfile

with zipfile.ZipFile('together.zip', 'r') as zf:
    # zf.extractall("tmp")
    zf.extract("test1.txt")
    zf.extract("test2.txt", 'secret')