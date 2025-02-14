import random  # Importing the random module for generating random numbers
import matplotlib.pyplot as plt  # Importing Matplotlib for visualization
import datetime  # Importing datetime to work with date and time
import os  # Importing os to interact with the file system

# Generate a random number between 0 and 10
number = random.randint(0, 10)
print(f"Random Number: {number}")

# Get the current date and time
now = datetime.datetime.now()

# Generate a random hour and minute for a random timestamp today
random_hour = random.randint(0, 23)
random_minute = random.randint(0, 59)

# Create a new datetime object with the random hour and minute
random_time = now.replace(hour=random_hour, minute=random_minute, second=0)

# Print the current time and the generated random time
print(f"Current time: {now}")
print(f"Random time today: {random_time}")

# List all files in the current directory
files = os.listdir(".")
print("Files in this directory:", files)

# Generate a list of 5 random numbers between 0 and 10 for the bar chart
numbers = [random.randint(0, 10) for _ in range(5)]

# Create a bar chart with the random numbers
plt.bar(range(1, 6), numbers, color='blue')  # X-axis: indices 1-5, Y-axis: random numbers
plt.xlabel('Index')  # Label for the X-axis
plt.ylabel('Random Number')  # Label for the Y-axis
plt.title('Random Numbers Bar Chart')  # Title of the plot

# Display the plot
plt.show()
