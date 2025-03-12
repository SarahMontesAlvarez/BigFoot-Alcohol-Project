# CapstoneProject
CodeKY Data Science Capstone Project

# Project Title:
Spirits and Sasquatch: Analyzing Alcohol Consumption and Bigfoot Sightings in the U.S.

### 1. Objective:
Investigate whether there is a statistical relationship between alcohol consumption and reported Bigfoot sightings across U.S. states. The analysis will include data cleaning, exploratory data analysis, statistical correlation, and visualization in Tableau.

### 2. Tools & Technologies:
SQL (for data extraction and transformation)
Python (for data cleaning, statistical analysis, and visualization), Pandas, NumPy, Matplotlib, Seaborn
Tableau (for interactive visualizations and dashboards)

### 3. Data Sources:
Bigfoot Sightings Dataset ([Kaggle](https://www.kaggle.com/datasets/josephvm/bigfoot-sightings-data))
Contains details on reported Bigfoot encounters, including state, date, latitude/longitude, and sighting descriptions.
Alcohol Consumption Dataset ([IHME United States Alcohol Use Prevalence by County 2002-2012: National](https://ghdx.healthdata.org/sites/default/files/record-attached-files/IHME_USA_COUNTY_ALCOHOL_USE_PREVALENCE_2002_2012_NATIONAL.zip))
Provides U.S. state-level per capita alcohol consumption over time, categorized by beverage type (beer, wine, spirits).

### 4. Database & SQL Setup:
Load both datasets into a PostgreSQL/MySQL database.
Create tables:
bigfoot_sightings (id, date, state, latitude, longitude, description, classification)
alcohol_consumption (state, year, beer_per_capita, wine_per_capita, spirits_per_capita, total_per_capita)
Perform SQL queries to:
Aggregate Bigfoot sightings per state per year.
Join both datasets on state and year for analysis.

### 5. Data Cleaning & Preprocessing (Python):
Handle missing/null values.
Convert dates to a uniform format.
Standardize state names for accurate joins.
Remove outliers (e.g., duplicate sightings, extreme alcohol values).

### 6. Exploratory Data Analysis (EDA):
Calcualte correlation and statistical signifigance per state and year and overall
Create visualizatoins to view correlation and signifigance


### 8. Tableau Dashboard Design (Time Permitting):

Create an interactive dashboard with Tableau Public


### 9. Conclusion & Insights:
Correlation Coefficient: 0.06440976464219382
P-Value: 0.21090463639065118
The correlation is NOT statistically significant.

Although there did not appear to be a strong correlation between alcohol consumption patterns over the course of the years and bigfoot sightings, this varied widely by state (see bar chart). These states show a strong positive correlation, implying that as alcohol consumption increases, so do Bigfoot sightings.

North Dakota: 1.000 (perfect correlation)
South Dakota: 0.865
Illinois: 0.798
Massachusetts: 0.668
North Carolina: 0.634

The Dakotas and Illinois show the highest positive correlations, potentially due to more rural areas where Bigfoot sightings might be more common (Norht Carolina could also be considered higher correlation with a large rural population).

Some states (Once again like North Dakota and South Dakota) show consistently high correlations across years.
Other states, like Illinois and Massachusetts, have more fluctuation, suggesting variations in either alcohol consumption patterns or Bigfoot sighting reports.
The overall trend suggests that while correlations are high in some states, they are not always stable over time.

Data Gaps: Some states lack correlation data, meaning further analysis might be needed.