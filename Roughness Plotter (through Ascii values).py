# Rename ASCII files to something 1_untreated in order to have proper lableing in legend
# Extract roughness using JPK application, then delete all things above values and save it

import matplotlib.pyplot as plt
import glob
import numpy as np

# Ask for the working directory
working_dir = input("Enter the working directory path: ")

# Load the ASCII files
data = []
for file_name in glob.glob(f"{working_dir}/*.cross"):
    x_data = []
    y_data = []
    with open(file_name, "r") as file:
        for line in file:
            x, y = line.split()
            x_data.append(float(x))
            y_data.append(float(y))
    data.append((x_data, y_data))

# working with
n_data = []
for x, y in data:

    x_norm = 1000000*(x - np.min(x))
    y_norm = 1000000*(y - np.min(y))
    
    #x_norm = (x - np.min(x)) / np.max(x)
    #y_norm = (y - np.min(y)) / np.max(y)
    n_data.append((x_norm, y_norm))

# Plot the normalized data as a graph
for i, (x, y) in enumerate(n_data):
    plt.plot(x, y, label=f"Data Set {i+1}")

plt.xlabel("Length(μm)")
plt.ylabel("Height(μm)")
plt.title("Roughness(nm)")
plt.legend(('Untreated','PPI(40mM)', 'SN_CNPs(200μg/ml)'), loc="upper left", bbox_to_anchor=[1, 1],
                 ncol=1, shadow=False, title=False, fancybox=True)

plt.savefig('E:\Bacterial_Images\LAzzat\Results\high_resolution_plot.png', dpi=600, facecolor='w', edgecolor='w',
       orientation='landscape', format='png', transparent=False, bbox_inches='tight', pad_inches=0.1,)

plt.show()
