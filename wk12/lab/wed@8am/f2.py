import zipfile

with zipfile.ZipFile("collection.zip") as zfo:
    zfo.extract("Singer_Test.txt", "fake_album")
    zfo.extractall("unzipped_content")
