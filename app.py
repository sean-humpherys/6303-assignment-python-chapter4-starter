# Chapter 4.1 Defining Functions
def greet():
    print("Hi there")
    print("Welcome aboard")


greet()
print("***End Chapter 4.1 Defining Functions\n")


# Chapter 4.2 Arguments. This chapter demonstrates two arguments
# Note. You cannot have functions with the same name in the same file,
# which is why we change the name to greet2().
def greet2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet2("Ada", "Lovelace")  # Google who Ada Lovelace was
print("***End Chapter 4.2 Arguments\n")


# Chapter 4.3 Types of Functions
# Function of 'Do tasks'
def greet3(name):
    print(f"Hi {name}")


print(greet3("Ada"))


# Function of 'return value'
def greet4(name):
    return(f"Hi {name}")


message = greet4("Sophie Wilson")
print(message)
message = greet4("Grace Hopper")
print(message)
message = greet4("Ida Rhodes")
print(message)
print("***End Chapter 4.3 Types of Functions\n")


# Chapter 4.4 Keyword Arguments
def increment(number, by):
    return number + by


print(increment(2, by=1))
print("***End Chapter 4.4 Keyword Arguments\n")


# Chapter 4.5 Default Arguments
def increment_default(number, by=1):
    return number + by


print(increment_default(2, 5))
print("***End Chapter 4.5 Default Arguments\n")


# Chapter 4.6 xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
print(multiply(55, 87))
print(multiply(100, 98, 77, 4, -5, 72, 0.5))
print("***End Chapter 4.6 xargs\n")


# Chapter 4.7 xxargs
def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)
print("***End Chapter 4.7 xxargs\n")


# Chapter 4.8 Scope
message = "don't use global variables"


def greetings(name):
    global message
    message = "this is a local variable"


greetings("Sean")
print(message)
print("***End Chapter 4.8 Scope\n")


# Chapter 4.9 Debugging
# Watch the video and learn how to debug. Nothing to code.

# Chapter 4.10 & 4.11 VSCode Coding Tricks
# Watch the video and learn. Nothing to code.


# Chapter 4.12 Exercise / 4.13 Solution
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
print(fizz_buzz(3))
print(fizz_buzz(5))
print("***End Chapter 4.12 Exercise / 4.13 Solution")
