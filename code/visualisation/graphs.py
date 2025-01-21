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

    # Bepaal de maximale score over beide lijsten
    max_score = max(max(scores_list1), max(scores_list2))

    # Bepaal de bin-randen met intervallen van 500, tot iets boven de max score
    step = 500
    bin_edges = np.arange(0, max_score + step + 1, step)

    # Bereken de frequenties per bin voor beide lijsten
    freq1, _ = np.histogram(scores_list1, bins=bin_edges)
    freq2, _ = np.histogram(scores_list2, bins=bin_edges)

    # Bepaal de middens van de bins (voor het plaatsen van de staven)
    bin_midpoints = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Staafbreedte kiezen (zodat ze netjes naast elkaar passen)
    width = step * 0.4  # bijvoorbeeld 40% van de stapgrootte

    # Plot de staven voor beide lijsten naast elkaar
    plt.bar(bin_midpoints - width/2, freq1, width=width, label=label_list1, alpha=0.7)
    plt.bar(bin_midpoints + width/2, freq2, width=width, label=label_list2, alpha=0.7)

    # Labels maken voor de x-as (bijv. "0-500", "500-1000", ...)
    bin_labels = [f"{int(bin_edges[i])}-{int(bin_edges[i+1])}" for i in range(len(bin_edges)-1)]

    # Zet de x-as ticks op de midpoint en label ze met de intervalnaam
    plt.xticks(bin_midpoints, bin_labels, rotation=45)

    # As-labels en titel
    plt.xlabel("Score Intervallen")
    plt.ylabel("Frequentie")
    plt.title("Frequentie van scores in intervallen van 500")

    # Legenda toevoegen
    plt.legend()

    # Layout netter maken
    plt.tight_layout()

    # Toon de grafiek
    plt.show()


# Voorbeeld van aanroepen:

if __name__ == "__main__":
    list1= [100, 250, 500, 750, 1200, 1600, 2000, 2100, 2500, 2900, 3000, 3200]
    list2= [200, 450, 800, 800, 1250, 1450, 1980, 2100, 2450, 2900, 3100]
    name1= "greedy"
    name2= "random"
    results_comparison(list1, name1, list2, name2)
    