import subprocess
#import os


class Commander:

    def __init__(self):
        self.confirm = ["yes","affirmative","sure","do it","yeah","confirm"]
        self.cancel = ["no","negative","don't","wait","cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven\'t told me your name yet, Fuck off!'")
                print("my name?")
            elif "your" in text:
                self.respond("My name is Hitler Adolf. How are you?")
                print("your name?")
        else:
            self.respond(text)

    def respond(self, response):
        subprocess.call("say %s"%response, shell = True)
