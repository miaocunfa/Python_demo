from user import User 
from admin import Privileges, Admin

admin = Admin('ming', 'xiao', '13', 'Earth')
admin.describe_user()
admin.greet_user()
print("")
admin.privileges.show_privileges()
