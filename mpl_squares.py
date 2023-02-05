import matplotlib
matplotlib.use
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

small_font = 14
large_font = 24

ax.plot(input_values,
        squares, linewidth=3)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=large_font)
ax.set_xlabel("Value", fontsize=small_font)
ax.set_ylabel("Square of Value", fontsize=small_font)

# Set the size of the tick labels
ax.tick_params(axis='both', labelsize=small_font)

# Show the plot
plt.show()
