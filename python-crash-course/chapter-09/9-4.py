# encoding=utf-8
class Restaurant():
    """描述餐馆的类"""
 
    def __init__(self, restaurant_name, cuisine_type):
        """设置餐馆的名称和烹饪风格"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the Restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine_type of the Restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is open")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
       
    def increment_number_served(self, number_served):
        if number_served > 0:
            self.number_served += number_served
        else:
            print("You can't roll back!")

chinese_rest = Restaurant('Mr.Li', 'Chinese food')

print("restaurant_name: " +  chinese_rest.restaurant_name)
print("cuisine_type: " + chinese_rest.cuisine_type)
print("")

chinese_rest.describe_restaurant()
chinese_rest.open_restaurant()
print("")

print("number_served: " + str(chinese_rest.number_served))
chinese_rest.set_number_served(46)
print("number_served: " + str(chinese_rest.number_served))
chinese_rest.increment_number_served(4)
print("number_served: " + str(chinese_rest.number_served))
