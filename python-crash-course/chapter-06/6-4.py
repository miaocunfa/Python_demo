# coding: utf-8

word_list = {'sign':'标志', 'parking':'停车', 'hard':'困难的', 'translate':'翻译', 'useful':'有用的'}
python_list = {'for':'for循环', '[]':'列表', '{}':'字典', 'if':'判断', 'print':'控制台打印'}

for word, describe in word_list.items():
    print(word + ": " + describe)

print("")

for word, describe in python_list.items():
    print(word + ": " + describe)
