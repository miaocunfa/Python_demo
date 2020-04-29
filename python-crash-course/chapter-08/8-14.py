# encoding=utf-8
def car_profile(brand, type, **car_info):
    """创建一个字典，其中包含我们知道的有关汽车的一切"""
    profile = {}
    profile['brand'] = brand
    profile['type'] = type
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = car_profile('Honda', 'CRV', color='black')
print(car_profile)
