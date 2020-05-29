# bounce.py
#
# Exercise 1.5

height = 100  # meters

for i in range(1, 11):
    height = (3/5) * height
    print(f'{i} {round(height, 4)}')
