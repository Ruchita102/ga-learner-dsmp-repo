### Project Overview

 For this project, exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

Problem Statement
What is the probability that the borrower paid back their loan in full?

about dataset
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

 Independency check,Bayes theorem,Visualized discrete variable using bar plot,Visualized continuous variable usning histogram.



### Approach taken to solve the problem

 checked Independence by calculating joint probability the condition fico credit score is greater than 700 and purpose == 'debt_consolidation' is independent of each otherso the result came falst that means they are not independent.Calculating conditional probability is a very important step.so used the Bayes theorem for the probability of credit policy is yes and the person is given the loan.then drawn Probability Distrubution of Purpose using bar plot. then drawn histogram for continuous variable. So got the basic idea about how the distribution of continuous variables looks like.



