import random 

jterm4week = ["Dei in bio", "fem in col", "astronomy", "sociology"]

jtermweek1 = ["aviation", "love contemp", "wandavision"]
jtermweek2 = ["audio production", "aviation", "la noir", "rocketry"]

"""jterm4week.shuffle() 
jtermweek1.shuffle()
"""
random.shuffle(jtermweek1)
random.shuffle(jtermweek2)
random.shuffle(jterm4week)
k = int(input("pick a num 0 to 3"))
print(jterm4week[k])
print(jtermweek1[k])
print(jtermweek2[k])