# for number in [1,2,3,4]:
#     print(number)
#
# for char in "Hello World":
#     print(char)


import random
class LotteryMachine:
  def __iter__(self):
    self.numbers = []
    return self
  def __next__(self):
    if len(self.numbers) == 6:
      raise StopIteration
    else:
      unique_num = False
      while unique_num == False:
        number = random.randint(1,49)
        if number not in self.numbers:
          self.numbers.append(number)
          unique_num = True
          return number
# This is what we want to do
machine = LotteryMachine()
for number in machine:
    print(number)
