import matplotlib.pyplot as plt

squares = [ 1, 4, 9, 16, 25]

fig, ax = plt.subplots()

small_font = 14
large_font = 24

ax.plot(squares, linewidth=3)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=large_font)
ax.set_xlabel("Value", fontsize=small_font)
ax.set_ylabel("Square of Value", fontsize=small_font)

# Show the plot
plt.show()
