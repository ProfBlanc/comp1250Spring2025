from working_with_files import FileWorker


fo = FileWorker("test2.txt", "w")

fo.write_content("Overwriting content")
