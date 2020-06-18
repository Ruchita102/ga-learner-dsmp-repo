### Project Overview

 Problem Statement
Bank Of New York wants to expand its branches and for that, it has a certain hypothesis and statements it wants to verify. Using the inferential statistics method to help the bank

About the Dataset
It has data from 9578 customers with the following 15 features:

Feature	Description
customer.id	ID of the customer
credit.policy	If the customer meets the credit underwriting criteria of LendingClub.com or not
purpose	The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
int.rate	The interest rate of the loan
installment	The monthly installments owed by the borrower if the loan is funded
log.annual.inc	The natural log of the self-reported annual income of the borrower
dti	The debt-to-income ratio of the borrower (amount of debt divided by annual income)
fico	The FICO credit score of the borrower
days.with.cr.line	The number of days the borrower has had a credit line.
revol.bal	The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
revol.util	The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
pub.rec	The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
inq.last.6mths	The borrower's number of inquiries by creditors in the last 6 months
delinq.2yrs	The number of times the borrower had been 30+ days past due on a payment in the past 2 years
paid.back.loan	Whether the user has paid back loan



### Learnings from the project

 Confidence Interval,z test,Central Limit Theorem,z critical, z staticsHypothesis Testing,Chi-Square Test


### Approach taken to solve the problem

 first task was involved  loading data and finding the confidence interval. then found Central Limit Theorem holds for installment column or not.then did hypothesis testing if p-value is less than 0.05, you can reject the null hypothesis, If 'p-value is greater than 0.05, you can't reject the null hypothesis so p value was greater so accept null hypothesis.The bank thinks that monthly installments (installment) customers have to pay might have some sort of effect on loan defaulters so  after applied z test on installment and paid back got the p value less than 0.05 so reject null hypothesis then applied chi2 and critical value so the p value came greater but still reject null hypothesis beacause If chi-squared statistic exceeds the critical value, reject the null hypothesis that the two distributions are the same, else null hypothesis cannot be rejected


