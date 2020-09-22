import csv

# data class to store data about one winner
class Winner:
    def __init__(self, index, year, age, name, movie):
        self.index = int(index)
        self.year = int(year)
        self.age = int(age)
        self.name = name
        self.movie = movie

    def values(self):
        return [self.index, self.year, self.age, self.name, self.movie]

winners = []
count = 1 # so we know at what position to append our new data to the file

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)

    next(reader) # skips the first
    for row in reader:
        #current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
        count += 1
        current_winner = Winner(*row)
        winners.append(current_winner)

with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    # Write header row
    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])
    for winner in winners:
        winner.age += 1
        writer.writerow(winner.values())


# for winner in winners:
    # print(f"{winner.name} won the oscar for {winner.movie}")
#     print(f"{winner.name} was born during or near {winner.year - winner.age}")

# with open("oscars.csv", "a") as csvfile:
#     writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#     new_winner = Winner(count, "2020", "50", "Renée Zellweger", "Judy")
#     # writer.writerow([winner.index, winner.year, winner.age, winner.name, winner.movie])
#     writer.writerow(new_winner.values())

# Create a list with all of the winners from the 1980s
eighties_winners = [winner for winner in winners if winner.year >= 1980 and winner.year <= 1989]
for winner in eighties_winners:
  print(f"{winner.name} won in {winner.year}")

# Find the age of the oldest Oscar winner
max_age = 0
for winner in winners:
    if winner.age > max_age:
        max_age = winner.age
print(f"Oldest oscar winner was {max_age} years old when they won!")


# Create a list with all of Meryl Streep's Oscar winning movies
meryls_best_ones = [winner for winner in winners if winner.name == "Meryl Streep"]
for meryl in meryls_best_ones:
    print(f"{meryl.movie} in { meryl.year}")
