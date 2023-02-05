import matplotlib

matplotlib.use
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
"""
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 
'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 
'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 
'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 
'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 
'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

small_font = 14
large_font = 24

ax.plot(input_values,
        squares, linewidth=3)

# Set chart title and label the axes
ax.set_title("Square Numbers", fontsize=small_font)
ax.set_xlabel("Value", fontsize=small_font)
ax.set_ylabel("Square of Value", fontsize=small_font)

# Set the size of the tick labels
ax.tick_params(axis='both', labelsize=small_font)

# Show the plot
plt.show()
