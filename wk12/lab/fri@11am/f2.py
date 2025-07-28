import zipfile

to_write = [
    {
    "filename": "test1.txt",
    "content": "Hello World!",
    },
    {
        "filename": "test2.txt",
        "content": "Everyone is welcome to learn",
    },
]

for item in to_write:
    with open(item['filename'], "w") as fo:
        fo.write(item['content'])
class ToWrite:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content
    def write(self):
        with open(self.filename, "w") as fo:
            fo.write(self.content)

ToWrite("test1.txt", "Hello World!").write()
ToWrite("test2.txt", "Everyone").write()


with zipfile.ZipFile("test_zip.zip", "w") as zfo:
    zfo.write("test1.txt")
    zfo.write("test2.txt")


with zipfile.ZipFile("test_zip.zip", "r") as zfo:
    zfo.extractall()
    zfo.extract("test1.txt")
    zfo.extract("test2.txt", "my_dir")