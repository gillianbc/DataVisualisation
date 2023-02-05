import matplotlib
matplotlib.use
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')

small_font = 14
large_font = 24

fig, ax = plt.subplots()
# show a single point at coordinate (2,4), size 200
# ax.scatter(2, 4, s=200)


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
# show points for the x and y values
ax.scatter(x_values, y_values, s=100)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=small_font)
ax.set_xlabel("Value", fontsize=small_font)
ax.set_ylabel("Square of Value", fontsize=small_font)

# Set the size of the tick labels
ax.tick_params(axis='both', which='major', labelsize=small_font)

plt.show()
