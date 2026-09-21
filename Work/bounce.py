# bounce.py
#
# Exercise 1.5
bounce = 0 # Bounce times
ball_height = 100 # Initialize ball height (meters)

while bounce < 10:
    bounce = bounce + 1
    ball_height = ball_height * 3 / 5
    print(bounce, round(ball_height, ndigits=4))