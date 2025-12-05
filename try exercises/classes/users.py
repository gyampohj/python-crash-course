class User:
    def __init__(self,first_name, last_name, age, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print(f"User Info")
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Age : {self.age}")
        print(f"Profession : {self.profession}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

"""Instance Creation and method calling"""
user1 = User("John", "Doe", age=30)


print(user1.greet_user)