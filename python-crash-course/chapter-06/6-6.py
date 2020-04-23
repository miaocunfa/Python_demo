favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

list = ['jen', 'zhazha', 'zhanan', 'phil', 'zhanv']

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("")

for i in list:
    if i not in favorite_languages.keys():
        print(i + ", please take out poll!") 
    else:
        print(i + ", thank you for taking the poll.")
