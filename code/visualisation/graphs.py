import matplotlib.pyplot as plt

def graph(random_scores):
    bins = range(0, 10001, 1000)
    
    plt.hist(random_scores, bins = bins, edgecolor = "black")
    
    plt.xlabel("Score (K)")
    plt.ylabel("Count")
    plt.title("Count for range of scores, rounded to 1000")
    plt.show()