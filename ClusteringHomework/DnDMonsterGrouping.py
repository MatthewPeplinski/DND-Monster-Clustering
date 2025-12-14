"""
This program attempts to group officially published Dungeons and Dragons monsters into
distinct clusters in order to make inferences on the overall game design.

https://docs.google.com/spreadsheets/d/16ajgJpvUI0wYcSU7kjHutw8oB6Zv6eIAo5JtI6PLvu8/edit?usp=sharing
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

## This program attempts to find groupings of roughly 800 officially published
# monsters in the game Dungeons and Dragons using KMeans

monsters = pd.read_csv("Monster Spreadsheet (D&D5e).csv")
monsters = monsters[['Name', 'CR', 'Size', 'AC', 'HP',
                         'STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']]
monsters.dropna(inplace=True)

##Seperate out the labels
# get the monster names
monsterNames = monsters['Name']
# using rudimentary numeric stats, which will not tell the entire strength of a monster but
# hopefully will still be informative enough to formulate groups that make sense
monsterStats = monsters[['CR', 'AC', 'HP','STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']]

# Need to normalize data for proper comparison of different labels, namely HP being way different
X = monsterStats.copy().to_numpy() * 1.0
std = np.std(X, axis=0)
X /= std

## First we check the number of clusters using inertia

# I would expect there to be either roughly 20 or 5 groups based on subject
# knowledge, 5 referring to tiers of play, and 20 relating to the range of CR
inertia = np.zeros(19)
for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, n_init=30).fit(X)
    inertia[i-1] = kmeans.inertia_

plt.plot(np.arange(1, 20), inertia)
plt.show()
# The graph generally shows a distinct elbow at 5, which lines up with the assumption of tiers of play

#Using the 5 clusters for KMeans, we will group monsters
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

#Show info about the clusters
print(kmeans.inertia_)
print(kmeans.cluster_centers_ *std)

# Display the 5 clusters
for i in range(5):
    print(f"Average Stats for cluster {i}:")
    for label, value in zip(stat_labels, kmeans.cluster_centers_[i] * std):
        print(f"  {label}: {value:.2f}")
    print()
#     print(f"Average Stats for cluster {i}: {kmeans.cluster_centers_[i] *std}")
#     # checking what monsters are in each cluster
#     for name in monsterNames[kmeans.labels_ == i]:
#         print(name)
