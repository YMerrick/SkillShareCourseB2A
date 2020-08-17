import matplotlib.pyplot as plt
import numpy as np

colCount = 3
barWidth = .1

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(colCount)

k1 = plt.bar(index,korea_scores,barWidth,alpha=.8,label='Korea')
c1 = plt.bar(index+barWidth, canada_scores,barWidth,alpha=.8,label='Canada')
ch1 = plt.bar(index+barWidth+barWidth, china_scores,barWidth,alpha=.8,label='China')
f1 = plt.bar(index+(barWidth*3),france_scores,barWidth,alpha=.8,label='France')

def createLabels(data):
    for item in data:
        height = item.get_height()

plt.ylabel('Mean score in PISA 2012')
plt.xlabel('Subjects')
plt.title('Comparison of test scores')

plt.xticks(index+.3/2,('Mathematics','Reading','Science'))
plt.legend()

plt.show()
