class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Кухня: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг {self.restaurant_name} изменился до  {self.rating}")

restaurant1 = Restaurant("TOKIO CITY", "Азиатская", 4.2)
restaurant1.describe_restaurant()
restaurant1.update_rating(4.6)
