import matplotlib.pyplot as plt

years = [1900,1950, 1955, 1960, 1965,1970, 1975,1980, 1985, 1990, 1995, 2000,2005, 2010, 2015]

pop = [1.650,2.525,2.758,3.018,3.322,3.682,4.061,4.440,4.853,5.310,5.735,6.127,6.520,6.930,7.349]

plt.plot(years,pop,color=(255/255,100/255,100/255))
plt.xlabel("Pop. growth by year")
plt.ylabel("Pop. in billions")
plt.title("Pop. Growth")
plt.show()
