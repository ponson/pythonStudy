from choices import fast, advice
import sys

print("Let's go to ", fast.pick())
print("Shout we take out?", advice.give())

for place in sys.path:
    print(place)

from collections import Counter
breakfast = ['spam','spam','spam','eggs']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)

txt = "Hello World"[::-1]
print(txt)