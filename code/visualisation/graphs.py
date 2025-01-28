import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def results_comparison(*score_label_pairs, step=500, max_x=10000):
    """
    Vergelijkt 1 of meer lijsten met scores (elk met een eigen label) in ranges
    met een stapgrootte van 500, en plot ze gegroepeerd in één histogram.
    
    Parameters
    ----------
    *score_label_pairs : 
        Variabel aantal tuples (scores_list, label_str)
        waarin 'scores_list' een list is met scores (bijv. [120, 630, 1000, ...])
        en 'label_str' een string voor de legenda.
        
    step : int, optional
        Stapgrootte van de intervallen. Default is 500.
    
    max_x : int, optional
        Maximale x-waarde (score) die op de x-as wordt getoond. Default is 10000.
    """

    # We willen minstens 1 dataset plotten
    if len(score_label_pairs) < 1:
        raise ValueError("Geef minstens één (scores_list, label)-paar mee.")

    # Stel bin-randen vast van 0 tot max_x in stappen van 'step'
    bin_edges = np.arange(0, max_x + step, step)
    
    # Bepaal per dataset de histogram-frequentie (absoluut),
    # deel vervolgens door het totaal aantal scores, daarna * 100 voor een percentage
    freqs = []
    labels = []
    for scores, label in score_label_pairs:
        freq, _ = np.histogram(scores, bins=bin_edges)
        freq = (freq / len(scores)) * 100  # Normaliseer naar percentage
        freqs.append(freq)
        labels.append(label)

    # Middelpunt van elke bin (nodig voor plaatsen van de staven)
    bin_midpoints = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Hoeveel datasets zijn er?
    num_datasets = len(freqs)

    # Verdeel bijvoorbeeld 80% van de binbreedte (step) over alle datasets
    total_bar_width = step * 0.8
    bar_width = total_bar_width / num_datasets

    # We gaan de gehele 'groep' bars per bin centreren rond bin_midpoints
    left_offset = total_bar_width / 2

    # Plot alle datasets
    for i, freq in enumerate(freqs):
        offset = -left_offset + (i + 0.5) * bar_width
        plt.bar(bin_midpoints + offset, freq, width=bar_width,
                label=labels[i], alpha=0.7)

    # De labels voor de x-as: gebruik de bovengrens van de bins
    bin_labels = [str(int(edge)) for edge in bin_edges[1:]]
    
    # Zet de x-ticks op de bin_midpoints, maar label ze met de *bovengrens*
    plt.xticks(bin_midpoints, bin_labels, rotation=45)

    # As-labels en titel
    plt.xlim([0, max_x])
    plt.ylim([0, 100])  # Y-as van 0 tot 100%
    plt.xlabel("Score (afgerond)")
    plt.ylabel("Runs Percentage (%)")  # Aangepast label voor percentage
    plt.title("Frequentie van scores (in %)")

    # Formater toevegen
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f%%'))

    # Legenda en layout
    plt.legend()
    plt.tight_layout()
    plt.show()


# voorbeeld van runnen:
if __name__ == "__main__":
    list1= [100, 250, 500, 750, 1200, 1600, 2000, 2100, 2500, 2900, 3000, 3200]
    list2= [200, 450, 800, 800, 1250, 1450, 1980, 2100, 2450, 2900, 3100]
    list3= [252, 450, 843, 867, 1250, 1450, 1980, 2230, 2476, 2250, 3140]
    name1= "greedy"
    name2= "random"
    name3= "hillclimber"
   
    results_comparison((list1, name1), (list2, name2), (list3, name3), step=2000)
