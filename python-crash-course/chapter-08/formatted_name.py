# encoding=utf8 
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    fullname = last_name + first_name
    return fullname.title()

zha = get_formatted_name('nan','zha')
print(zha)
