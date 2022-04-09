import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x=np.arange(3)
Bill= [100,90,90,90]
Jim= [100,90,80,80]
Joe= [100,80,90,90]
width=0.15
names=['Bill','Jim','Joe']

Math=[Bill[0],Jim[0],Joe[0]]
English=[Bill[1],Jim[1],Joe[1]]
Physics=[Bill[2],Jim[2],Joe[2]]
Computer=[Bill[3],Jim[3],Joe[3]]

Math_bar=ax.bar(x-width*1.5,Math,width,label='Math')
English_bar=ax.bar(x-width*0.5,English,width,label='English')
Physics_bar=ax.bar(x-width*-0.5,Physics,width,label='Physics')
Computer_bar=ax.bar(x-width*-1.5,Computer,width,label='Computer')

ax.set_title('Grouped Graph For Scores')
ax.legend(handles=[Math_bar,English_bar,Physics_bar,Computer_bar],loc='upper center',bbox_to_anchor=(0.75,0.5))

ax.bar_label(Math_bar)
ax.bar_label(Physics_bar)
ax.bar_label(English_bar)
ax.bar_label(Computer_bar)

plt.xticks(x,names)
plt.show()