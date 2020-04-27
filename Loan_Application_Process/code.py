# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
banks = bank.drop(columns=['Loan_ID'])
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]

banks.fillna(bank_mode, inplace = True)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')

print(avg_loan_amount)
# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed'] == 'Yes')]['Self_Employed'].count()

loan_approved_nse = banks[(banks['Loan_Status'] == 'Y') & (banks['Self_Employed'] == 'No')]['Self_Employed'].count()

percentage_se = (loan_approved_se * 100)/614
print(percentage_se)
percentage_nse = (loan_approved_nse * 100)/614
print(percentage_nse)

# code ends here


# --------------
# code starts here

def conv(num):
    return num/12

loan_term = banks['Loan_Amount_Term'].apply(lambda x : conv(x))

print(loan_term)

big_loan_term = len(loan_term[loan_term >= 25])

print(big_loan_term)
# code ends here


# --------------
# code starts here
print(banks['Loan_Status'])

loan_groupby = banks.groupby(['Loan_Status'])

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()

print(mean_values)

# code ends here


