# Creating a program for a personal budget manager. 
# The program will allow users to input income and expenses with categores (ie. food, rent, entertainment)
# Output a summary of spending, income, and remaining budget
# Save user data to a file and load it automatically on startup
# Allow exporting reports as text/pdf files for offline use

from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]

plt.scatter(x_values, y_values)

other_x_values = [1, 2, 3, 4]
other_y_values = [4, 2, 3, 9]

plt.plot(other_x_values, other_y_values, color="navy")

plt.title("Sample Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()



