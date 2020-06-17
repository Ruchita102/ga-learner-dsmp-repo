# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-','Agender')
#Code starts here 
gender_count=data.Gender.value_counts()
print(gender_count)
plt.bar(gender_count.index,gender_count)
plt.show()


# --------------
#Code starts here
alignment=data.Alignment.value_counts()
print(alignment)
plt.pie(alignment,labels=alignment.index,explode=(0.05,0.05,0.05),autopct='%1.1f%%')
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_covariance=data['Strength'].cov(data['Combat'])
sc_strength=data.Strength.std()
sc_combat=data.Combat.std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df=data[['Intelligence','Combat']]
ic_covariance=data['Intelligence'].cov(data['Combat'])
ic_intelligence=data.Intelligence.std()
ic_combat=data.Combat.std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high=data['Total'].quantile(0.99)
super_best=data[data['Total']>total_high]
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title='Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set(title='Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set(title='Power')




