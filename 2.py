class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")


restaurant1 = Restaurant("Теремок", "Русская")
restaurant2 = Restaurant("Вкусно и точка", "Фастфуд")
restaurant3 = Restaurant("Поке", "Азиатская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

