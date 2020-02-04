# online Shoppers Intent

## Executive Summary:
We are assuming the position of business members at DataScienceDeals.com a company that sells courses on Data Science. We have data related to the visitors that come to our site.

The objective of this project is to predict which visitors are likely to produce revenue. This will feed into our new 1:1 chat help service feature that will be able to aid potential customers.

##  Key Files:
1.  [Link](https://docs.google.com/presentation/d/1Cu6vxCA_1aIgoW1ZqArEayFVPDSDD8eRxzvjWMUvT2I/edit#slide=id.g76cc41dd4c_0_1)
to google slides presentation file
2.  .pdf: PDF of presentation slides)to google slides presentation file: 
3.  'namegoeshere'.ipynb: Jupyter Notebook
4.  utils.py:
5.  :Raw CSV file with data

##  Methodology:
insert contents here.
##  Key Findings:
The first baseline Decision Tree model provided a low -insert evaluation - score.
Very small improvements were made using a combinatory hyperparameter optimisation.

A logistic Regression model performed much better giving a roc_auc score of 0.89.
Random Forest ensemble began with a lower roc_auc score initially (0.89) but was increased to 0.927 using hyperparameter optimisation through Random and Grid Search CV.

##  Conclusions:
there was a slight increase in model performance when using ensemble models (Random Forest) over Logistic Regression. 
The Grid Search Parameter optimsation was paramount in obtaining the highest model roc_auc score.

A Key component of our model was incoroporating the costs (penalties for getting predictions wrong or right)
Once we chose a threshold that took those costs into account we were able to obtain :  - insert value here - 

##  Reccomendations:
Based on the model performance we can go ahead and provide the feature engineer team with the data needed to build a chat box model. This model will certainly benefit from having the performance 
