import matplotlib.pyplot as plt

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