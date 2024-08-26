# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
    # Create a higher-order function that will take a callback as an argument

# def feed(pet):
#     return f'{pet} has been fed!'

# def walked(pet):
#     return f'{pet} has been walked!'

# def taskForRose(func):
#     return func("rose")

# print(taskForRose(walked))
# print(taskForRose(feed))


# 2. ✅ Create a higher-order function that returns a function
def taskForPet():
    def feed(pet):
        return f'{pet} has been fed!'
    return feed

print(taskForPet()("rose"))

# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'
# Without pie syntax 
def coupon_calculator(func):
    def wrapper():
        print("Base Price $35.00/hour")
        new_price = func(35.00)
        print(f'Price after coupon ${new_price}/hour')
    return wrapper

def halfOff(price):
    return '{:.2f}'.format(round(price/2,2))

halfOff = coupon_calculator(halfOff)
halfOff()

#With pie syntax '@'
@coupon_calculator
def tenOff(price):
    return '{:.2f}'.format(round(price-10,2))

tenOff()