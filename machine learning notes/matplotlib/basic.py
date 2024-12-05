import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a plot
# plt.plot(x, y, label="Line")
plt.plot(x, y, "r+",label='Plus') #with + in red
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.legend()

# Show the plot
plt.show()
