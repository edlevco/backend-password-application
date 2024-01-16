import turtle
from button import Button
from design import Design
import csv

# Sample data
data = [
    ["Username", "Password"],
]

# Specify the file name
csv_file_path = "users_data.csv"

# Open the CSV file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)
    # Write the data to the CSV file
    csv_writer.writerows(data)
print(f"CSV file '{csv_file_path}' has been created.")


turtle.colormode(255)

screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor((59, 255, 111))
screen.listen()

design = Design()

sign_up = Button(-120, -10, "sign up")
sign_in = Button(20, -10, "sign in")

def on_click(x, y):
    if x >= -120 and x <= -20 and y >= -10 and y <= 40:
        print("sign up")
        username = turtle.textinput("Username", "Enter your username:")
        password = turtle.textinput("Password", "Enter your password:")

        # with open("user_data.csv", "r") as file:

        
    elif x >= 20 and x <= 120 and y >= -10 and y <= 40:
        username = turtle.textinput("Username", "Enter your username:")
        password = turtle.textinput("Password", "Enter your password:")
        print("sign in")

# Bind the on_click function to the left mouse button click event
turtle.onscreenclick(on_click, 1)

# Keep the window open
turtle.mainloop()
