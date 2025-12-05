class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
 
class Admin(User):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.privileges = ["can add post", "can delete post"]

    def show_privileges(self):
        print(f"Privileges for {self.name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

"""Usage"""
admin = Admin("Holmes", "Master")
admin.show_privileges()           
    