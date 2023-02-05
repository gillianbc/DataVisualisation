import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

small_font = 14
large_font = 24

fig, ax = plt.subplots()
# show a single point at a coordinate
ax.scatter(2, 4, s=200)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=small_font)
ax.set_xlabel("Value", fontsize=small_font)
ax.set_ylabel("Square of Value", fontsize=small_font)

# Set the size of the tick labels
ax.tick_params(axis='both', which='major', labelsize=small_font)

plt.show()
