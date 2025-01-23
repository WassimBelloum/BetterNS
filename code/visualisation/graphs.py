import matplotlib.pyplot as plt
import numpy as np

def graph(random_scores):
    bins = range(0, 10001, 500)
    
    counts, edges, patches = plt.hist(random_scores, bins = bins, edgecolor = "black")
    
    for count, edge in zip(counts, edges[:-1]):
        if count > 0:
            plt.text(edge + 250, count + 0.5, f"{int(count)}", ha='center', fontsize=10)
    
    plt.xlim(0, 10000)
    plt.ylim(0, None)
    
    plt.xlabel("Score (K)")
    plt.ylabel("Count")
    plt.title("Count for range of scores, rounded to 1000")
    plt.show()










def results_comparison(scores_list1: list, label_list1: str, scores_list2: list, label_list2: str):
    """
    vergelijkt 2 lists resultaten met elkaar in ranges met 500 als stapsgrootte
    
    Parameters:
    -----------
    scores_list1 : list
        Lijst met scores.

    label_list1 : str
        Naam list1 (te zien in de legenda).

    scores_list2 : list
        Lijst met scores.

    label_list2 : str
        Naam list2 (te zien in de legenda).
    """

    # Stapgrootte en maximale waarde voor de x-as vast instellen
    step = 500
    max_x = 10000

    # Stel bin-randen vast van 0 tot 10.000 in stappen van 500
    bin_edges = np.arange(0, max_x + step, step)

    # Bereken de frequenties per bin voor beide lijsten
    freq1, _ = np.histogram(scores_list1, bins=bin_edges)
    freq2, _ = np.histogram(scores_list2, bins=bin_edges)

    # Bepaal de middens van de bins (voor het plaatsen van de staven)
    bin_midpoints = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Staafbreedte (bijvoorbeeld 40% van de stapgrootte)
    width = step * 0.4

    # Plot de staven voor beide lijsten naast elkaar
    plt.bar(bin_midpoints - width/2, freq1, width=width, label=label_list1, alpha=0.7)
    plt.bar(bin_midpoints + width/2, freq2, width=width, label=label_list2, alpha=0.7)

    # Labels voor de x-as (bijv. "0-500", "500-1000", ...)
    bin_labels = [f"{int(bin_edges[i])}-{int(bin_edges[i+1])}" for i in range(len(bin_edges)-1)]

    # Zet de x-as ticks op de midpoint en label ze met de intervalnaam
    plt.xticks(bin_midpoints, bin_labels, rotation=45)

    # As-labels en titel
    plt.xlabel("Score Intervallen (stap=500, tot 10.000)")
    plt.ylabel("Frequentie")
    plt.title("Frequentie van scores in vaste intervallen (0 tot 10.000)")

    # Legenda toevoegen
    plt.legend()

    # Beperk de x-as tot 0 - 10.000 (zodat het niet automatisch schaalt)
    plt.xlim([0, max_x])

    # Layout netter maken
    plt.tight_layout()

    # Toon de grafiek
    plt.show()



# Voorbeeld van aanroepen:

# if __name__ == "__main__":
#     list1= [100, 250, 500, 750, 1200, 1600, 2000, 2100, 2500, 2900, 3000, 3200]
#     list2= [200, 450, 800, 800, 1250, 1450, 1980, 2100, 2450, 2900, 3100]
#     name1= "greedy"
#     name2= "random"
#     results_comparison(list1, name1, list2, name2)



import matplotlib.pyplot as plt
import numpy as np

def results_comparison_1(*score_label_pairs, step=500, max_x=10000):
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
    
    # Bepaal per dataset de histogram-frequentie
    freqs = []
    labels = []
    for scores, label in score_label_pairs:
        freq, _ = np.histogram(scores, bins=bin_edges)
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

    # In plaats van "0-500" willen we één getal op de x-as, bijvoorbeeld
    # de bovengrens van iedere bin (dat is bin_edges[1:], bin_edges[2:], etc.)
    # De lengte van 'bin_midpoints' is hetzelfde als 'bin_edges[:-1]', dus
    # we kunnen als label de bin_edges[1:] nemen.
    bin_labels = [str(int(edge)) for edge in bin_edges[1:]]
    
    # Zet de x-ticks op de bin_midpoints, maar label ze met de *bovengrens*
    plt.xticks(bin_midpoints, bin_labels, rotation=45)

    # As-labels en titel
    plt.xlim([0, max_x])
    plt.xlabel("Score (afgerond)")
    plt.ylabel("Frequentie")
    plt.title("Frequentie van scores")

    # Legenda en layout
    plt.legend()
    plt.tight_layout()
    plt.show()


# if __name__ == "__main__":
#     list1= [100, 250, 500, 750, 1200, 1600, 2000, 2100, 2500, 2900, 3000, 3200]
#     list2= [200, 450, 800, 800, 1250, 1450, 1980, 2100, 2450, 2900, 3100]
#     name1= "greedy"
#     name2= "random"
#     results_comparison((list1, name1), (list2, name2), step=1000, max_x=10000)