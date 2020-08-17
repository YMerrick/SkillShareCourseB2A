import matplotlib.pyplot as plt
import pandas as pd

rawData = {'name':['John','Panda','Henry','Geralt','Jennifer'],
           'janIR':[143,122,101,111,169],
           'febIR':[122,145,100,90,111],
           'marchIR':[65,12,123,70,88]
           }

df = pd.DataFrame(rawData,columns=['name','janIR','febIR','marchIR'])

df['totalIR' ] = df['janIR'] + df['febIR'] + df['marchIR']

color = [(1,.4,.4),(1,.6,1),(.5,.3,1),(.3,1,1),(.7,.7,.1)]
plt.pie(df['totalIR'],labels=df['name'],colors=color)
plt.axis('equal')
plt.show()
print(df)
