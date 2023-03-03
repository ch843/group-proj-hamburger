#Cassidy Hardisty, Kira Coleman, Tiffany Zang, Ryan Hawkins, Grace Chou

# Create an Order class
# Create a constructor that defines an instance variable called burger_count
# Create a method called randomBurgers that returns a number between 1 and 20
# The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable

# Create a Person class
class Person() :
    def __init__(self) :
        self.customer_name = randomName() # Create a constructor that defines an instance variable called customer_name # The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable

    def randomName(self) : # Create a method called randomName() that contains a list of 9 names:
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]# asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers) # This method randomly returns one of the 9 names when called

class Customer(Person) :# Create a Customer class that inherits from the Person class

    def __init__(self):
        super().__init__()
        self.order = Order()





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
