from collections import UserDict
data_contacts = [
    {
                "id": "Contacts.current_id",
                "name": "name",
                "phone": "phone",
                "email": "email",
                "favorite": "favorite",
    },
    {
                "id": "Contacts.current_id",
                "name": "name",
                "phone": "phone",
                "email": "email",
                "favorite": "favorite",
    },
    {
                "id": "Contacts.current_id",
                "name": "name",
                "phone": "phone",
                "email": "email",
                "favorite": "favorite",
    },
    {
                "id": "Contacts.current_id",
                "name": "name",
                "phone": "phone",
                "email": "email",
                "favorite": "favorite",
    }
]

class Customer(UserDict):
    def get_phone(self):
        return f'{self.data.get("name")}: {self.data.get("phone")}'

    def get_email(self):
        return f'{self.data.get("name")}: {self.data.get("email")}'

data = [Customer(contact) for contact in data_contacts]
for data_one in data:
    print(data_one.get_phone())
    print(data_one.get_email())