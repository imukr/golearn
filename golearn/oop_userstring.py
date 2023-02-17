from collections import UserString
text = [
    'Python supports a String like a container called UserString present in the collections module. ' ,
    'This class acts as a wrapper class around the string objects. This class is useful when one wants' ,
    ' to create a string of their own with some modified functionality or with some new functionality. ' ,
    'It can be considered as a way of adding new behaviors for the string. This class takes any argument ' ,
    'that can be converted to string and simulates a string whose content is kept in a regular string. ' ,
    'The string is accessible by the data attribute of this class.'
]

'''
|  0  |Python supports a String like a container called UserString present in the collections module. |
|  1  |This class acts as a wrapper class around the string objects. This class is useful when one wants|
|  2  | to create a string of their own with some modified functionality or with some new functionality. |
|  3  |It can be considered as a way of adding new behaviors for the string. This class takes any argument |
|  4  |that can be converted to string and simulates a string whose content is kept in a regular string. |
|  5  |The string is accessible by the data attribute of this class.|
'''
for num, st in enumerate(text):
    print('|{:^5}|{:>15}|'.format(num, st))
    # print(num, st)

'''
|  0  |Python suppo...|
|  1  |This class a...|
|  2  | to create a...|
|  3  |It can be co...|
|  4  |that can be ...|
|  5  |The string i...|
'''
class Sort(UserString):
    def get_limit(self, limit = 15):
        return f"{self.data[:limit-3]}..."

comments = [Sort(comment) for comment in text]

for num, comment in enumerate(comments):
    print('|{:^5}|{:>15}|'.format(num, comment.get_limit()))



