def say_hello():
    return "hello world!"

# print(say_hello)

hi = say_hello

#some_function is a callback some_function
# function_caller is a HIGHER ORDER function_caller
        # a higher order function is any function that
        # takes another function as an arguement

def function_caller(some_function):
    return some_function()

print(function_caller(hi))

def outer_function():
  def inner_function():
    print("Hello from the inner function")

  inner_function()

outer_function()

def make_pretty(callback):
    def wrapper():
        print("I am doing some more cool functionality 😎")
        callback()
    return wrapper

@make_pretty
def bare_bones_business():
    print("I am doing the core ordinary work")

bare_bones_business()

# bare_bones_business()
# bare_bones_business()
# bare_bones_business()
# fancy_business = make_pretty(bare_bones_business)
# fancy_business()
