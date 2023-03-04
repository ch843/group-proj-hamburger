#Cassidy Hardisty, Kira Coleman, Tiffany Zang, Ryan Hawkins, Grace Chou, Ella Cook

# Create an Order class
#import random
import random
class Order() :
    def __init__ (self) :
        self.burger_count = Order.randomBurgers(self)

    # Create a constructor that defines an instance variable called burger_count
    # Create a method called randomBurgers that returns a number between 1 and 20
    # The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable
    def randomBurgers(self) :
        self.burger_count = random.randint(1,20)
        return self.burger_count

# Create a Person class
class Person() :
    def __init__(self) :
        # Create a constructor that defines an instance variable called customer_name 
        # The Person constructor should call the randomName() method and assign the 
        # return value (a random name) to the customer_name instance variable
        self.customer_name = self.randomName() 

    # Create a method called randomName() that contains a list of 9 names:
    # This method randomly returns one of the 9 names when called: ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", 
    # "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    def randomName(self) :
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(self.asCustomers)

# Create a Customer class that inherits from the Person class
# Create a constructor that calls the parent constructor
# Create an instance variable called order in the constructor that is assigned an order object
class Customer(Person) :
    def __init__(self):
        super().__init__()
        self.order = Order()

# Create a variable for a Queue that will be assigned items of type Customer 
# This variable will represent your line of customers (objects) waiting outside to place their hamburger orders
queueCustomers = []

# Create a variable for a Dictionary with keys of type string and values of type int.
# This variable will hold information about each customer 
dCustomer = {}

# Put 100 customers into the queue. Each customer object will already have a random number of burgers for each order
for iCount in range(0, 101):
    queueCustomers.append(Customer())

#loop runs while queue has items in it
while (len(queueCustomers) > 0) :
    # Make sure there is a key in the dictionary for each customer before you try incrementing their total! 
    # Otherwise, add the customer to the dictionary.
    if (dCustomer.get(queueCustomers[0].customer_name)) :
        #increment total for that customer name
        dCustomer[queueCustomers[0].customer_name] += queueCustomers[0].order.burger_count
    else:
        #adding customer to the dictionary because it doesn't exist already
        dCustomer[queueCustomers[0].customer_name] = queueCustomers[0].order.burger_count
    
    queueCustomers.pop(0)

# sort the dictionary from lowest to highest
sortedCustomers = sorted(dCustomer.items(), key=lambda x: x[1], reverse=True)

# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
for iCount in range(0, len(sortedCustomers)):
    print(sortedCustomers[iCount][0].ljust(19), sortedCustomers[iCount][1])
