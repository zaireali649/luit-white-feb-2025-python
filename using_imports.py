import random
import matplotlib.pyplot as plt
import datetime
import os

number = random.randint(0, 10)
print(f"Random Number: {number}")

now = datetime.datetime.now()
random_hour = random.randint(0, 23)
random_minute = random.randint(0, 59)

random_time = now.replace(hour=random_hour, minute=random_minute, second=0)
print(f"Current time: {now}")
print(f"Random time today: {random_time}")

files = os.listdir(".")
print("Files in this directory:", files)

numbers = [random.randint(0, 10) for _ in range(5)]

plt.bar(range(1, 6), numbers, color='blue')
plt.xlabel('Index')
plt.ylabel('Random Number')
plt.title('Random Numbers Bar Chart')

plt.show()
