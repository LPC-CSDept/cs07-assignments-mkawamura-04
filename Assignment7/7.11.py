import matplotlib.pyplot as plt
fig, ax = plt.subplots()
subjects= ['Math', 'English','Physics','Computer']
Bill= [100,90,80,60]
Mary= [90,80,70,100]
Bill_bar=ax.bar(subjects,Bill,label='Bill')
Mary_bar=ax.bar(subjects,Mary,bottom=Bill,label='Mary')
ax.set_title('Stacked Graph For Scores')
ax.legend(handles=[Bill_bar, Mary_bar])
plt.show()