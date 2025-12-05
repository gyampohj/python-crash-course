class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, 'Ice Cream')
        self.flavours = flavours

    def display_flavours(self):
        print(f"Flavours available at {self.restaurant_name}")
        for flavour in self.flavours:
            print(f"- {flavour}")

#Usage
icecream_stand = IceCreamStand("Sweet treats", "Mixed","Vanilla")
icecream_stand.display_flavours