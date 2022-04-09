import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x=np.arange(2)
subjects= ['Math', 'English','Physics','Computer']
Bill= [100,90,80,60]
Mary= [90,80,70,100]
width=0.15
names=['Bill','Mary']

Math=[Bill[0],Mary[0]]
English=[Bill[1],Mary[1]]
Physics=[Bill[2],Mary[2]]
Computer=[Bill[3],Mary[3]]

Math_bar=ax.bar(x-width*1.5,Math,width,label='Math')
English_bar=ax.bar(x-width*0.5,English,width,label='English')
Physics_bar=ax.bar(x-width*-0.5,Physics,width,label='Physics')
Computer_bar=ax.bar(x-width*-1.5,Computer,width,label='Computer')

ax.set_title('Grouped Graph For Scores')
ax.legend(handles=[Math_bar,English_bar,Physics_bar,Computer_bar])

ax.bar_label(Math_bar)
ax.bar_label(Physics_bar,padding=2)
ax.bar_label(English_bar,padding=2)
ax.bar_label(Computer_bar,padding=2)

plt.xticks(x,names)
plt.show()