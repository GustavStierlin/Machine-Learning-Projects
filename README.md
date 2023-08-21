# Machine-Learning-Projects
The following is code I wrote for my machine learning module 

Here are the questions I had to answer

Study the scenario and complete the question(s) that follow:
Credit Worth Assessment: Technical Consultant
Poer Bank is a prolific South African bank. Due to the bank competitive loan interest rate, the company 
has faced a surge of many clients borrowing money from the bank, however not always paying back 
their loans on time. Thus, the company would like to minimise the risk of potential customers and have 
more informed decision on if it should grant a loan or not to a potential debtor. Poer Bank has therefore 
contacted your business intelligence expert team to assist them with this endeavour. Aware of the fact 
that Banks keep records of clients’ transactions, you have requested Poer Bank to give access to 
customer credits information for the past 10 years to undergo the investigation. The Bank has granted 
you access to some of its data in its relational databases which they have exported in a voluminous 
SQL file under your disposition (“poer_credit_data.sql”). 
Source: Yves Matanga, 2022
1.1 Using the SQL file provided, create a local database (all tables included) on your system.
Using Python and relevant SQL queries within Python, create a dataframe or list of 
customer records with the following attributes: customer age, gender, marital status, 
education level, amount loaned as well as payback percentage at end of term.
(7 marks)
ITMLA2-B44 – Assignment – Block 4 2022 | V1.0 Page 6 of 10
1.2 To estimate the solvency of potential customers borrowing at Poer Bank, you have decided 
to build a multilayer perceptron (MLP) neural network regression model that evaluate the 
relationship between the customer age, marital status, education level against the payback 
percentage. Use 75% of your data to train the model and 15% for testing the model. You 
may use discrete numbers (single = -1, divorced = 0, married = 1) to condition the 
categorical variable: “marital_status” 
a. To better estimate the data inner relationships, normalize the model features (age, 
marital status, education level). (5 marks)
b. Using Python, train the MLP regressor and plot two scatter plots to estimate the 
goodness of fitness for the trained data (training data vs model prediction) and the 
tested data (test data vs model prediction). Calculate the coefficient of determination 
R2 for both sets (see appendix section). Retrain the model until you obtain a 
satisfactory goodness of fit for both trained set and tested set.
(You may the early stopping technique while training your model) (20 marks)
[Sub Total 25 Marks]
1.3 Having obtained the model estimate the extent to which potential debtors having the 
following profile will pay their debt to the end of term: 
age gender Marital status NQF Loan request Pb
28 f married 7 90000
28 m married 7 90000
40 m single 8 1000000
40 m divorced 8 1000000
50 f single 7 120000
50 f single 7 800000
50 f married 5 800000
28 f single 7 90000
65 f single 7 90000
25 m single 5 380000
(8 marks) 
All graphs must have titles, x-axis, and y-axis labels as well as grids. Print your python code 
below each graph and results in your assignment documentation.
End of Question 1
ITMLA2-B44 – Assignment – Block 4 2022 | V1.0 Page 7 of 10
Question 2 35 Marks 
Study the scenario and complete the question(s) that follow:
DSS: Automating HR employee selection
Prek Hi Tech is an IT company in Sandton that design top notch software. The company would like to 
up its competitiveness in the market by selecting quality workforce. Over the years, the company has 
noticed that not all implied hired perform at the highest standard. Hence, the company has profiled all 
its employees for the past five years with a quality score capturing the following attributes: age, NQF 
level, previous experience prior to employment including their appreciation of their work quality.
Prek Hi Tech uses an online recruitment process to stock potential employees’ details. Based on the 
profiling information stocked (“Prek_HR_data.csv”), the company would like to design an automatic 
selection criterion that pre-select the potential quality workers which will could through an actual 
interview process. As a machine learning guru in the company, you have been tasked to design the 
algorithm.
Source: Matanga, NY (2022)
2.1 From the data in Prek HR data (“Prek_HR_data.csv”), using Python generate a dataset 
that has as attributes: the NQF level, age and experience level of each profile employee 
against quality score as target. Split your dataset into a training set and validation set (15 
% test data, 85% training data) and submit your python code for the effect. (6 marks)
2.2 . Design a decision tree classifier from the training data and compute the classification 
accuracy of both the training set and test set. Plot the decision tree (tree rules). You may 
use “graphviz” Python library to plot the decision tree rules. (19 marks) 
2.3 Evaluate if the following candidate profiles will perform well or not at Prek Hi Tech based on 
the train model.
Age NQF Experience Level (num years) Quality score
23 7 1 ?
30 9 3 ?
60 8 3 ?
45 10 8 ?
36 6 10 ?
(5 marks)
ITMLA2-B44 – Assignment – Block 4 2022 | V1.0 Page 8 of 10
2.4 Based on the result in 3 and the decision tree, Determine the profile of an eligible candidate 
for Prek Hi Tech. (5 marks)
All graphs must have titles, x-axis, and y-axis labels as well as grids. Print your python code 
below each graph and results in your project documentation.
End of Question 2
ITMLA2-B44 – Assignment – Block 4 2022 | V1.0 Page 9 of 10
Question 3 25 Marks
Study the scenario and complete the question(s) that follow:
Optimising crops production: Merka Agri
Merka Agri is a wholesaler producer of corns. The company makes use of fertilizer to accelerate the 
growth of its crops added for 30 days period from planting prior to the harvesting. The amount of 
fertilizer obviously as an impact of the growth of the corns and the company would like to have an 
adequate estimate of the relationship between the amount of fertilizer added overall against the weight 
of the final corn. You have conducted an experiment for 100 crops whereby a fixed amount of mg per 
pot is added every day and at the end of 30 days the weights of the corns have been recorded. You are 
currently in the analysis of the data (“merka_argi_corn_experiment.csv”). 
Source : http://www.stat.cmu.edu/~hseltman/309/Book/chapter9.pdf
3.1. Generate a Scatter plot that shows the relationship between the amount of fertilizer per day 
(mg) and the weight of the corn. Label your x and y-axis appropriately as well as provide a 
title for your plot (6 marks) 
3.2. Using Python, estimate by linear regression the relationship between the corn final weight 
and the fertilizer addition (mg) from Merka Agri data. (Use all your data for training the linear 
regressor). Write down the linear model of the corn growth: 
weight = a*fertilizer_addition + b
 (10 marks)
3.3. Generate a new plot of your linear model, superimpose your scatterplot in question 1.
(6 marks)
3.4. What is the expected weigh of a corn planted in Merka Agri farms if the 50mg of fertilizer is 
regularly added for 30 days prior to harvesting?
