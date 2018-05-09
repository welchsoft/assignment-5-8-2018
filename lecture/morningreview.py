class Customer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

customers = []

for index in range(0,10):
    customer = Customer("clone" +str(index), "clonington"+str(index), 10)
    customers.append(customer)

for clone in customers:
    print(clone.first_name, clone.last_name, clone.age)

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.addresses = []

    def add_adress(self, address):
        self.addresses.append(address)

class Geo:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Address:
    def __init__(self, street, city, state,geo):
        self.street = street
        self.city = city
        self.state = state
        self.geo = geo

my_person = Person("john", "johnboy", 25)
my_adress = Address("S streat","H town","TX",Geo(34,100))
my_person.add_adress(my_adress)

print(my_person.addresses[0].street)
print(my_person.addresses[0].geo.latitude)
