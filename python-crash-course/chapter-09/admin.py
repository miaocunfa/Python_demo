from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("What privileges does admin have: ")
        for pri in self.privileges:
            print("\t" + pri)

class Admin(User):
    def __init__(self, first_name, last_name, age, adress):
        super().__init__(first_name, last_name, age, adress)
        self.privileges = Privileges()
