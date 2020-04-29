# encoding=utf-8
class User():
    """定义用户"""
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.login_attempts = 0
        self.full_name = self.last_name.title() + self.first_name.title()

    def describe_user(self):
        print("the name of user is " + self.full_name + ", is " + self.age + " years old!")
        print("User live in " + self.address)
    
    def greet_user(self):
        print("Hello, " + self.full_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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

xiaoming = Admin("ming", "xiao", "13", "气死人星球")
xiaoming.privileges.show_privileges()
