# Intro
This program uses dnd monster stat blocks to determine the number of groups dnd monsters would fall into based purely their base stats, then forms those groups. Using inertia for KMeans to determine the number of clusters, it was determined that there would be 5 groupings of monsters, which roughly fall in line with wizards of the coast'sown "Tiers of play" philosophy.

## Stats
Creatures are given statistics which correspond to their state of being. These are what I am using to group monsters by, and are listed as follows:

CR: Challenge rating -> Expected level that a DnD party would be at to fight this monster
- AC: Armor Class -> The number that needs to be rolled to hit the creature in combat
- HP: Hit Points -> Amount of damage that a creature can take before dying
- STR: Strength -> How much physical ability a creature has
- DEX: Dexterity -> How nimble a creature is
- CON: Constitution -> Strenth of vitality, normally HP is derrived based on level and something to do with this stat
- WIS: Wisdom -> Innate knowledge or understanding of the world
- INT: Intelegence -> Measure of how smart a creature is, sometimes construed as cleverness
- CHA: Charisma -> Measure of the force of personality of a given creature

## Determining number of clusters
Using intertia, the number of clusters for grouping is determined to be 5 by subjectively identifying the elbow in the graph:

![K Means Elbow Graph](https://github.com/MatthewPeplinski/DND-Monster-Clustering/blob/main/kmeans_intertia_elbow.png)

## Final output
After the 5 clusters are determined, the monsters are grouped, resulting in groups which look like the following:

Average Stats for cluster 0:
- CR: 11.57
- AC: 17.40
- HP: 153.25
- STR: 18.31
- DEX: 14.12
- CON: 18.19
- WIS: 15.11
- INT: 15.27
- CHA: 16.52

Average Stats for cluster 1:
- CR: 5.60
- AC: 14.88
- HP: 100.77
- STR: 18.96
- DEX: 10.87
- CON: 17.46
- WIS: 10.51
- INT: 6.08
- CHA: 7.65

Average Stats for cluster 2:
- CR: 21.65
- AC: 20.20
- HP: 352.54
- STR: 26.72
- DEX: 14.85
- CON: 25.17
- WIS: 18.28
- INT: 16.96
- CHA: 21.61

Average Stats for cluster 3:
- CR: 0.67
- AC: 11.91
- HP: 20.18
- STR: 10.85
- DEX: 12.37
- CON: 12.11
- WIS: 9.78
- INT: 3.60
- CHA: 4.94

Average Stats for cluster 4:
- CR: 2.90
- AC: 13.90
- HP: 46.64
- STR: 11.74
- DEX: 14.52
- CON: 13.07
- WIS: 12.23
- INT: 11.60
- CHA: 12.19
