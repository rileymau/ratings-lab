"""Restaurant rating lister."""
import sys
input_file = open(sys.argv[1])
rating_dict = {}

for line in input_file:
    name, rating = line.rstrip().split(":")
    rating_dict[name] = rating

input_file.close()

restaurant_name = input("What is the restraunt name? ")
restaurant_rating = input("What is their rating?")
rating_dict[restaurant_name] = int(restaurant_rating)

sorted_dict = sorted(rating_dict.keys())
for key in sorted_dict: 
      print(f"{key} is rated at {rating_dict[key]}")


