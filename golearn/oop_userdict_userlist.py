from  collections import UserList, UserDict
class Phones(UserList):
    def set_phone(self, phone):
        self.data.append(phone)

    def get_phones(self):
        return self.data
#{name: name, phones: [phone, phone, phone]}
class User(UserDict):
    def set_name(self, name):
        self.data['name'] = name

    def set_phone(self,phone):
        list_phones = self.data.get('phones', Phones())
        list_phones.data.append(phone)
        self.data['phones'] = list_phones

    def get_name(self):
        return self.data.get('name')

    def get_phones(self):
        return self.data.get('phones')

user_1 = User()
user_1.set_name('Bill')
user_1.set_phone(38097091111255)
user_1.set_phone(191984898111)
print(user_1.data)
print(user_1.get_name())
print(user_1.get_phones())
