import os
import zipfile


class Toy:
    def __init__(self, name, description, release_date):
        self.name = name
        self.description = description
        self.release_date = release_date
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Release Date: {self.release_date}"
    def save(self):
        file_name = f'{self.name.lower().replace(' ', '_')}.txt'
        with open(file_name, 'w') as f:
            f.write(str(self).replace(", ", '\n'))
        return file_name
class Collection:
    def __init__(self, name):
        self.name = name  # name of collection
        self.toys = list()
    def add_toy(self, toy):
        if isinstance(toy, Toy):
            self.toys.append(toy)
    def save_all(self):
        for toy in self.toys:
            toy.save()
    def zip_all(self):
        zip_name = self.name.lower().replace(' ', '_') + '.zip'
        to_remove = list()
        with zipfile.ZipFile(zip_name, "w") as f:
            for toy in self.toys:
                file_name = toy.save()
                f.write(file_name)
                to_remove.append(file_name)

        for file_name in to_remove:
            os.remove(file_name)

t1 = Toy("Toy 1", "description 1",
         "Jan 2025")
t2 = Toy("Cool Toy", "awesome description",
         "July 2025")

# t1.save()
# t2.save()

items = Collection("My Collection")
items.add_toy(t1)
items.add_toy(t2)
items.zip_all()