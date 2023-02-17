from  collections import UserList
from random import randint

class MyList(UserList):
    _info = "This is my list"

    def get_positive(self):
        return list(filter(lambda x: x > 0, self.data))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))

    def _info(self):
        return self._info


r = []

for _ in range(1, 20):
    r.append(randint(-5, 5))

result = MyList(r)
print(result.data)
print(result.get_positive())
print(result.get_negative())

