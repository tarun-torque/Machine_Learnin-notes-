import matplotlib.pyplot as plt
import numpy as np

# x =np.linspace(-5,5,50)
# plt.plot(x,np.sin(x),'g+')
# plt.plot(x,np.cos(x),'r--')

# plt.show()


# bar graph

# fig,ax = plt.subplots()
# languages = ['English','French','Spanish','German']
# people = [100,50,150,40]

# ax.bar(languages,people)
# plt.xlabel('Languages')
# plt.ylabel('No of people speaking')

# plt.show()


# pi chart

# Data
languages = ['English', 'French', 'Spanish', 'German']
people = [100, 50, 150, 40]

# Create a pie chart
# plt.figure(figsize=(6, 6))  # Optional: Set the figure size
# plt.pie(
#     people, 
#     labels=languages, 
#     autopct='%1.1f%%',  # Display percentage with 1 decimal
#     startangle=90,      # Start angle for better layout
#     colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Optional: Custom colors
# )

# # Add a title
# plt.title('Percentage of People Speaking Different Languages')

# # Show the plot
# plt.show()



# scatter plot
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# # Create a scatter plot
# plt.scatter(x, y, color='blue', label='Data Points')  # Add a label and color

# # Customize the plot
# plt.title('Scatter Plot Example')
# plt.xlabel('X-axis (Independent Variable)')
# plt.ylabel('Y-axis (Dependent Variable)')
# plt.legend()  # Display the legend

# # Show the plot
# plt.show()


# 3d scatter plot
from mpl_toolkits.mplot3d import Axes3D

# Data
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
z = [1, 3, 2, 4, 5, 7, 6, 8, 5, 9]

# Create a figure for the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
scatter = ax.scatter(x, y, z, color='purple', marker='o', label='Data Points')

# Add labels and title
ax.set_title('3D Scatter Plot Example')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# Show the plot
plt.show()


