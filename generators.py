# Print all numbers from 1 to 10
numbers = range(1, 11)

# for number in numbers:
#     print(number)

# print(numbers) # This will print a range object
                                            # (generator)
                                            # (not a list!!!)

# generator that generates all the even numbers
def generate_evens(max):
    index = 1
    while index <= max:
        if index % 2 == 0:
            yield index
        index += 1

# for number in generate_evens(10):
#     print(number)

print(list(generate_evens(10)))
