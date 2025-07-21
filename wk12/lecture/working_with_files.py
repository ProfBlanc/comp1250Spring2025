class FileWorker:
    def __init__(self, file_name, file_mode="r"):
        self.file_name = file_name
        self.file_mode = file_mode
        self.fo = open(self.file_name, self.file_mode)

    def is_writable(self):
        return self.file_mode in "a,w,a+,r+"

    def write_content(self, text):
        if self.is_writable():
            self.fo.write(text)
        else:
            print("Operation not possible")

    def __str__(self):
        return f"Working with file '{self.file_name}' " \
               f"using mode {self.file_mode}"


if __name__ == "__main__":
    my_file = FileWorker("test1.txt", "a")

    my_file.write_content("Hello World\n")
