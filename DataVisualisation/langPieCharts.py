import matplotlib.pyplot as plt


labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'

sizes = [33, 52, 12, 17, 62, 48]
separated = (.2,0,0,0,0,0)

print(type(labels))
#Pie chart
plt.pie(sizes,labels=labels,autopct='%1.11f%%',explode=separated)
plt.show()
