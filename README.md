# CapstoneProject
CodeKY Data Science Capstone Project

# Project Title:
"Spirits and Sasquatch: Analyzing Alcohol Consumption and Bigfoot Sightings in the U.S."

### 1. Objective:
Investigate whether there is a statistical relationship between alcohol consumption and reported Bigfoot sightings across U.S. states. The analysis will include data cleaning, exploratory data analysis, statistical correlation, and visualization in Tableau.

### 2. Tools & Technologies:
SQL (for data extraction and transformation)
Python (for data cleaning, statistical analysis, and visualization), Pandas, NumPy, Matplotlib
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
Categorize Bigfoot sightings (e.g., by season, rural vs. urban areas).

### 6. Exploratory Data Analysis (EDA):
Bigfoot Sightings Analysis:
Map sightings using geospatial visualizations (Seaborn, Folium).
Identify peak years/seasons for sightings.
Alcohol Consumption Trends:
Visualize alcohol consumption per state over time.
Compare beer, wine, and spirits consumption.
Comparing Sightings & Alcohol:
Identify high-alcohol vs. high-sighting states.


### 8. Tableau Dashboard Design (Time Permitting):

Create an interactive dashboard with:

Choropleth maps (Bigfoot sightings and alcohol consumption per state).
Line charts (Sightings | Alcohol consumption trends over time).
Scatter plots (Correlation between sightings and alcohol).
Filter options (State selection, year range, alcohol type).
9. Conclusion & Insights:
Determine if alcohol consumption has a statistically significant effect on Bigfoot sightings.
Discuss alternative explanations and possible confounding factors.
Suggest next steps, such as finer geographic analysis or sentiment analysis of sighting reports.
