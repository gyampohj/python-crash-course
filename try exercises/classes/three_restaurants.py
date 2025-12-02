class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

""" Create instance and class calls"""
restaurant1 = Restaurant("Asanka local", "local")
restaurant2 = Restaurant("Zoes kitchen", "mixed")
restaurant3 = Restaurant("coffee lounge", "continental")  

print(restaurant1.cuisine_type)
print(restaurant2.restaurant_name)