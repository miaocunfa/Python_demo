current_users = ['admin', 'zhanan', 'zhanv', 'zhazha', 'zhagod']

new_users = ['admin', 'songjiang', 'zhazha', 'lujunyi', 'wuyong']

for new in new_users:
    if new in current_users:
        print(new + " is already in use, Please enter a different user name")
    else:
        print(new + " is not in use")
