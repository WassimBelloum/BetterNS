import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def results_comparison(*score_label_pairs, step=500, max_x=10000):
    """
    Compares one or more lists of scores (each with its own label) in ranges 
    with a step size of 500, and plots them grouped in a single histogram.

    Parameters
    ----------
    *score_label_pairs : 
        A variable number of tuples (scores_list, label_str), where:
          - scores_list is a list of scores (e.g., [120, 630, 1000, ...])
          - label_str is a string for the legend.
        
    step : int, optional
        The step size of the intervals. Default is 500.
    
    max_x : int, optional
        The maximum x-value (score) shown on the x-axis. Default is 10000.
    """

    # We want at least one dataset to plot
    if len(score_label_pairs) < 1:
        raise ValueError("Please provide at least one (scores_list, label) pair.")

    # Set bin edges from 0 to max_x in increments of 'step'
    bin_edges = np.arange(0, max_x + step, step)
    
    # For each dataset, determine the histogram frequency (absolute),
    # then divide by the total number of scores, and then multiply by 100 to get a percentage
    freqs = []
    labels = []
    for scores, label in score_label_pairs:
        freq, _ = np.histogram(scores, bins=bin_edges)
        freq = (freq / len(scores)) * 100  # Normalize to percentage
        freqs.append(freq)
        labels.append(label)

    # Midpoint of each bin (needed for bar placement)
    bin_midpoints = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # How many datasets are there?
    num_datasets = len(freqs)

    # Distribute, for example, 80% of the bin width (step) among all datasets
    total_bar_width = step * 0.8
    bar_width = total_bar_width / num_datasets

    # We center the entire 'group' of bars per bin around bin_midpoints
    left_offset = total_bar_width / 2

    # Plot all datasets
    for i, freq in enumerate(freqs):
        offset = -left_offset + (i + 0.5) * bar_width
        plt.bar(bin_midpoints + offset, freq, width=bar_width,
                label=labels[i], alpha=0.7)

    # The labels for the x-axis: use the upper limit of the bins
    bin_labels = [str(int(edge)) for edge in bin_edges[1:]]

    # Set x-ticks at bin_midpoints, but label them with the *upper limit* of the bins
    plt.xticks(bin_midpoints, bin_labels, rotation=45)

    # Axis labels and title
    plt.xlim([0, max_x])
    plt.ylim([0, 100])  # Y-axis from 0% to 100%
    plt.xlabel("Score (rounded)")
    plt.ylabel("Percentage of Runs (%)")  
    plt.title("Frequency of Scores (in %)")

    # Add a formatter to show '%' in integer format
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))

    # Legend and layout
    plt.legend()
    plt.tight_layout()
    plt.show()


# Example of how to run:
# if __name__ == "__main__":
#     list1 = [100, 250, 500, 750, 1200, 1600, 2000, 2100, 2500, 2900, 3000, 3200]
#     list2 = [200, 450, 800, 800, 1250, 1450, 1980, 2100, 2450, 2900, 3100]
#     list3 = [252, 450, 843, 867, 1250, 1450, 1980, 2230, 2476, 2250, 3140]
#     name1 = "greedy"
#     name2 = "random"
#     name3 = "hillclimber"
#
#     results_comparison((list1, name1), (list2, name2), (list3, name3), step=2000)





def curve_diagram(score_run: list[float]):
    """
    A makes a diagram were Y axis the score is and the X axis the run number.
    """
    for i, k in enumerate(score_run):
        plt.plot(i, k, 'ro')
    plt.xlabel('Iteration')
    plt.ylabel('Score')
    plt.title('Score vs Iteration')
    plt.grid(True)
    plt.show()