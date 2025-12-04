class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super(). __init__(name)
        self.address = address

    def place_order(self, item):
        self.item = item
        return DeliveryOrder(self.name, self.item)

class Driver(Person):
    def __inti__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")

class DeliveryOrder(Person):
    def __inti__(self, item, customer, status = "preparing"):
        self.item = item
        self.customer = customer
        self.status  = status

    def assign_driver(self, driver):
        self.driver_name = driver.name

    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.name}\nStatus: {self.status}Driver: {self.name}"


#main code
person1 = Person('Alice')
customer1 = Customer(person1.name, 'home')
customer1.introduce()

person2 = Person('Bob')
customer2 = Customer(person2.name, 'home')
customer2.introduce()

person3 = Person('David')
driver = Driver(person3.name, 'motorcycle')
driver.introduce()

print()

order1 = DeliveryOrder('Laptop', customer1)
order1.assign_driver(driver)
order1.summary()

order2 = DeliveryOrder('Headphones', customer2)
order2.assign_driver(driver)
order2.summary()

print()

driver.deliver(order1)
driver.deliver(order2)

print()
print("Final Status:")
print(f"Order for {order1.item} → delivered")
print(f"Order for {order2.item} → delivered")



