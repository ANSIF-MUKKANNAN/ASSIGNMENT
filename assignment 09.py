class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_address(self, new_address):
        self.address = new_address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

person = Person("Ansif", 22, "malappuram edavanna")

print("Initial Information:")
person.display_info()

person.update_name("ansif")
person.update_age(23)
person.update_address("kochi kerala")

print("\nUpdated Information:")
person.display_info()
