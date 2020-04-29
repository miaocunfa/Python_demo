# coding: utf-8
from collections import OrderedDict

word_list = OrderedDict()
python_list = OrderedDict()

word_list['sign']      = '标志'
word_list['parking']   = '停车'
word_list['hard']      = '困难的'
word_list['translate'] = '翻译'
word_list['useful']    = '有用的'

python_list['for']   = 'for循环'
python_list['[]']    = '列表'
python_list['{}']    = '字典'
python_list['if']    = '判断'
python_list['print'] = '控制台打印'

for word, describe in word_list.items():
    print(word + ": " + describe)

print("")

for word, describe in python_list.items():
    print(word + ": " + describe)
