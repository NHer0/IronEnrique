![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

**Midterm project for house price predictions**

By **The Supermodels** 💃🏻 🕺🏻 💃🏼 Henrike Sahnwaldt, Enrique Hernani Ros & Rand Abu Ajamia

**Objective**: The task is to build a model that will predict the price of a house based on features provided in the dataset. The senior management also wants to explore the characteristics of the houses using some business intelligence tool. One of those parameters include understanding which factors are responsible for higher property value - \$650K and above.

**Tools used: Python, numpy, matplotlib, Pandas, Seaborn, sklearn Tableau**

**Steps**: The following steps describe the project planning: 

1. Exploring the data **(done)**: 
	- Get rough idea of variables / features and which ones to focus on **(Weekend)**
	- Describe method **(Weekend)**
	- Explore numerical and categorical columns **(Weekend)**
	- Clean data **(Monday)**
	- Checking null values **(Monday)**
	- Visualize data to understand details **(Monday)**
	- Distribution plot **(Monday)**
	- Correlation heatmap **(Monday)**
	- Boxplots for outliers **(Monday)**

3. Prepare the data for modelling **(Monday)(done)**
	- Dropping columns with multicorrelation
	- Transformation / processing
	- Normalization
	- Outlier treatment
	- Test / Train Split
	- Scaling numerical variables
	- Encoding categorical variables

4. Predictive Modelling **(Tuesday)**
	- Taking a walk!!!!!! 12:00 - 13:00 
	- Linear regression: first version done
	- Other models necessary / useful (log regression & others in sklearn): in research
	- Interpret the results
	- Metrics: R-square, P-values, plot regression and errors / residuals
	- Dig deeper with the models that perform best
	- Improving the model 
	- Compare the predictions (using the same measures of accuracy as a benchmark for each model)
 	- Find model that best fits the data
 	- Document the steps
 	- Outline the presentation

5. Presentation 
	- Make a draft presentation with preliminary plots **(Wednesday)**
	- Developing visualizations with Tableau **(Wednesday)**
	- Prepare presentation **(Wednesday)**
	- Practice the presentation (2, 3 times) **(Thursday)**
	- Buffer **(Thursday)**

6. Presenting **(Friday)**

**Background**: You are working as an analyst for a real estate company. Your company wants to build a machine learning model to predict the selling prices of houses based on a variety of features on which the value of the house is evaluated.

**Data**: The data set consists of information on some 22,000 properties.  The dataset consisted of historic data of houses sold between May 2014 to May 2015.
These are the definitions of data points provided:
(Note: For some of the variables that are self explanatory, no definition has been provided)

- **Id**: Unique identification number for the property.
- **date**: date the house was sold.
- **price**: price of the house.
- **waterfront**: house which has a view to a waterfront.
- **condition**: How good the condition is (overall). **1** indicates worn out property and **5** excellent.
- **grade**: Overall grade given to the housing unit, based on King County grading system. 1 poor ,13 excellent.
- **Sqft_above**: square footage of house apart from basement.
- **Sqft_living15**: Living room area in 2015(implies - some renovations). This might or might not have affected the lotsize area.
- **Sqft_lot15**: lotSize area in 2015(implies - some renovations).


