# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
total=len(df)
p_a=((df['fico']>700).sum())/total
print(p_a)
p_b=((df['purpose']=='debt_consolidation').sum())/total
print(p_b)
df1=df[df['purpose']=='debt_consolidation']
p_a_b=((df1['fico']>700)).sum()/total
print(p_a_b)
result=(p_a==p_a_b)
print(result)




# code ends here


# --------------
# code starts here
total=len(df)
prob_lp=((df['paid.back.loan']=='Yes').sum())/total
print(prob_lp)
prob_cs=((df['credit.policy']=='Yes').sum())/total
print(prob_cs)
new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)

# code ends here


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distrubution of Purpose ")
plt.xlabel('number of purpose')
plt.ylabel('Probability')
plt.show()
df1=df[df['paid.back.loan']== 'No']
df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distrubution of Purpose ")
plt.xlabel('number of purpose')
plt.ylabel('Probability')
plt.show()

# code ends here


# --------------
# code starts here
inst_median=df.median().installment
inst_mean=df.mean().installment
df['installment'].hist(normed=True,bins=90)
plt.axvline(x=inst_median,color='r')
plt.axvline(x=inst_mean,color='g')
plt.show()
df['log.annual.inc'].hist(normed=True,bins=90)
plt.show()



# code ends here


