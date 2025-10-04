# LCP String Generation
# Install matplotlib module to run
# pip install matplotlib

import matplotlib.pyplot as plt

def generate_plots(x, y, labels, title):
    '''
        Generate linear plots
        x : list of floats
            list containing measurement points along x-axis
            assumming it is same for all categories
        y : list of lists of floats
            list containing numberical list data for multiple categories
        labels : list of strings
            list containing labels for the categories
        title : string
            title for the plot
    '''
    plt.figure(figsize=(10, 6))

    for i in range(len(y)):
        plt.plot(x, y[i], marker="o", label=labels[i])

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of Items (log scale)")
    plt.ylabel("Time (seconds, log scale)")
    plt.title(title)
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()