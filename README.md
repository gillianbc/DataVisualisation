# Data Visualisation

My first venture into matplotlib using the book Python Crash Course and python3

Page 310 - to see available styles:
```python
import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.available
```

# Running from the Shell

I have a venv containing matplotlib
To run a python script outside of IntelliJ, I need to activate the venv before running the script e.g

> source venv/bin/activate
> python3 mpl_squares.py

# Installing 
Typically the steps you always takes are:

- `git clone <repo>`
- `cd <repo>`
- `pip install virtualenv` (if you don't already have virtualenv installed)
- `virtualenv venv` to create your new environment (called 'venv' here)
- `source venv/bin/activate` to enter the virtual environment
- `pip install -r requirements.txt` to install the requirements in the current environment