# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico'] > 700]) / len(df['fico'])
print(p_a)

p_b = len(df[df['purpose'] == 'debt_consolidation']) / len(df['purpose'])
print(p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

p_a_b = len(df1[df1['fico'] > 700])/len(df1['fico'])
print(p_a_b)

if p_a_b == p_a:
    result = True
else:
    result = False
print(result)

# code ends here


# --------------
# code starts here
'''
Calculating conditional probability is a very important step. Let's calculate the Bayes theorem for the probability of credit policy is yes and the person is given the loan.
'''

prob_lp = len(df[df['paid.back.loan'] == 'Yes']) / len(df['paid.back.loan'])
print(prob_lp)

prob_cs = len(df[df['credit.policy'] == 'Yes']) / len(df['credit.policy'])
print(prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes']) / len(new_df['credit.policy'])

print(prob_pd_cs)

bayes = prob_pd_cs * prob_lp / prob_cs

print(bayes)
# code ends here


# --------------
# code starts here
'''
Let's visualize the bar plot for the purpose and again using condition where
'''

df.purpose.value_counts(normalize=True).plot(kind='bar')
plt.show()

df1 = df[df['paid.back.loan'] == 'No'] 

df1['paid.back.loan'].value_counts().plot(kind='bar')
plt.show()

# code ends here


# --------------
# code starts here
'''
visualization of continuous variable
Let's plot the histogram for visualization of the continuous variable. So that you will get the basic idea about how the distribution of continuous variables looks like.
'''

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].plot(kind='hist')
plt.show()
df['log.annual.inc'].plot(kind='hist')
plt.show()
# code ends here


