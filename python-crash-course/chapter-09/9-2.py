# encoding=utf-8
class Restaurant():
    """描述餐馆的类"""
 
    def __init__(self, restaurant_name, cuisine_type):
        """设置餐馆的名称和烹饪风格"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the Restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine_type of the Restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is open")

chinese_rest1 = Restaurant('Mr.Li', 'Chinese food')
chinese_rest2 = Restaurant('HaiDiLao', 'Chinese food')
chinese_rest3 = Restaurant('ShanXiMianGuan', 'Chinese food')

chinese_rest1.describe_restaurant()
print("")

chinese_rest2.describe_restaurant()
print("")

chinese_rest3.describe_restaurant()
print("")
