class Contact:
    def __init__(self, number, name=""):
        self.number = number
        self.name = name if len(name) > 0 else "Unknown"
        self.username = self.name.lower().replace(" ", "_")

    def __str__(self):
        return (f"Contact has a name "
                f"of {self.name} "
                f"and a number of {self.number}")

    def save(self):
        file_name =  self.username + ".txt"
        with open(file_name, "w") as fo:
            content = f"Name={self.name}\nNumber={self.number}"
            fo.write(content)


class Message:
    def __init__(self, sender, recipient, body):
        self.sender = sender
        self.recipient = recipient
        self.body = body

class Conversation:
    def __init__(self, name):
        self.name = name
        self.messages = []
    def add_message(self, message):
        if isinstance(message, Message):
            self.messages.append(message)

    def __str__(self):
        content = ""
        for message in self.messages:
            content += (f"{message.sender.name} ({message.sender.number})\n"
                       f"sends a message to\n{message.recipient.name} "
                       f"({message.recipient.number})\nContent:\n{message.body}\n")
            content += "*" * 20 + "\n"

        return content


me = Contact(name="Ben Blanc", number=4164152000)
print(me.name)
print(me.number)
print(me.username)
me.save()
print(me)

you = Contact(name="My Friend", number=4165551234)
convo = Conversation("Talk Between Besties")
convo.add_message(Message(me, you, body="Hey, how are you doing?"))
convo.add_message(Message(you, me, "Who dis?"))
print(convo)
