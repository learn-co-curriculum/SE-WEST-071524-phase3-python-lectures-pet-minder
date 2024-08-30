# 1. ✅ Demonstrate First Class Functions
# Create functions to be used as callbacks
# Create a higher-order function that will take a callback as an argument


# def feed(pet):
#     return f"{pet} has been fed!"


# def walk(pet):
#     return f"{pet} has been walked!"


# def task_for_Rose(func):
#     return func("Rose")


# def task_for_cutely(func):
#     return func("Cutely")


# print(task_for_Rose(feed))
# print(task_for_cutely(walk))

# 2. ✅ Create a higher-order function that returns a function


def task_for_pet():
    def feed(pet):
        return f"{pet} has been fed!"

    return feed


print(task_for_pet()("Brigid"))
print(task_for_pet()("Cutely"))


# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'

# Without pie syntax


def coupon_calculator(func):
    def wrapper():
        print("Base price is $35.00/hour")
        new_price = func(35.00)
        print(f"Price after coupon ${new_price}/hour")

    return wrapper


def halfOff(price):
    return f"{round(price/2):.2f}"


def twenty_off(price):
    return f"{round(price*.8):.2f}"


half_off = coupon_calculator(halfOff)
half_off()

twenty_percent_off = coupon_calculator(twenty_off)
twenty_percent_off()


# With pie syntax


@coupon_calculator
def ten_off(price):
    return f"{round(price * .9):.2f}"


ten_off()
