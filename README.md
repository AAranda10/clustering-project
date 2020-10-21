# Zillow Clustering Project

### Author: Austin Aranda

## Description: 
The purpose of this project is to develop a model that is able to predict log error for the counties of Los Angeles, Orange, and Ventura, using the Zillow dataset. I intend to discover the key features that most accurately predict property value. 

In addition, I have provided these deliverables:
    1. Map showing variations in property values by location.
    2. Acquire.py, Prep.py, Wrangle.py files to be able to recreate my efforts.
    3. Presentation with the results of our findings.

## Project Planning

Initial Questions:
- Does location impact the value of a home?
- Is there a variance in log error based on location?
- Does the square footage of a home impact the value?
- Will clustering help clarify what's driving the log error?


### Hypotheses:

𝐻 0 - There is no difference in log error between houses in Orange County and Los Angeles/Ventura Counties

𝐻 a - There is a difference between log error in Orange County and Los Angeles/Ventura Counties

𝐻 0 - There is no difference in log error between houses with greater than 1500 square feet and houses with less than 1500 square feet.

𝐻 a - There is a difference in log error between houses with greater than 1500 square feet and houses with less than 1500 square feet.


## Data Dictionary

| Feature | Definition |
| --- | --- |
| bathroomcnt | Number of bathrooms in property (includes half bathrooms) |
| lotsizesquarefeet | The lot size of the home in square feet |
| calculatedbathnbr | Number of both bedrooms and bathrooms in property |
| calculatedfinishedsquarefeet | Total Square Footage of the property |
| taxvaluedollarcnt | Value of the property |

| Target | Definition |
| --- | --- |
| log error | The number of deviation from the actual value of property |


## Key Findings

- I found that the lot size and location heavily weight the value of the homes for high price homes.

- The model predicted with 99 percent accuracy and improved on on train to validate, then slight change on test, but did not overfit.

- Based on the clusters, the houses that were causing so much variance on the my prior model was due to pockets of high priced homes in areas where prices were reasonable.


## Takeaways

- I created a useable model that can recreate the accuract of the log error column with 99 percent accuracy.

- Now that the model has provided the key features in deciding what home valuation is based on in Los Angeles, we can apply this model to other areas to see if it is still as accurate.
