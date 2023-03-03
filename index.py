#Cassidy Hardisty, Kira Coleman, Tiffany Zang, Ryan Hawkins, Grace Chou, Ella Cook

# Create an Order class
#import random
import random
class Order() :
    def __init__ (self, burger_count) :
        self.burger_count = 0
        

    def randomBurgers() :
        return random.randint(1,20)
# Create a constructor that defines an instance variable called burger_count
# Create a method called randomBurgers that returns a number between 1 and 20
# The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable

# Create a Person class
# Create a constructor that defines an instance variable called customer_name
# Create a method called randomName() that contains a list of 9 names:
# asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", 
# "Carmen", "Invisible Swordsman", "Singing Bush"]
# This method randomly returns one of the 9 names when called
# The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name 
# instance variable

# Create a Customer class that inherits from the Person class
# Create a constructor that calls the parent constructor
# Create an instance variable called order in the constructor that is assigned an order object

# Create a variable for a Queue that will be assigned items of type Customer 
# This variable will represent your line of customers (objects) waiting outside to place their hamburger orders

# Create a variable for a Dictionary with keys of type string and values of type int.
# This variable will hold information about each customer 

# Put 100 customers into the queue. Each customer object will already have a random number of burgers for each order

# Make sure there is a key in the dictionary for each customer before you try incrementing their total! 
# Otherwise, add the customer to the dictionary.

# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
