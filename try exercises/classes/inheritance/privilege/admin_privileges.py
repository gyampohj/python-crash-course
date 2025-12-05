class Privileges:
    def __init__(self):
        self.prviliges = ["can add post", "can delete post"]

    def show_privileges(self):
        print("Privileges")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.privileges = Privileges()