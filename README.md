# CapstoneProject
CodeKY Data Science Capstone Project

# Spirits and Sasquatch: Analyzing Alcohol Consumption and Bigfoot Sightings in the U.S.

### Objective:
Investigate whether there is a statistical relationship between alcohol consumption and reported Bigfoot sightings across U.S. states. The analysis will include data cleaning, exploratory data analysis, statistical correlation, and visualization in Tableau.

### Tools & Technologies:
SQL (for data extraction and transformation)
Python (for data cleaning, statistical analysis, and visualization), Pandas, NumPy, Matplotlib, Seaborn
Tableau (for interactive visualizations and dashboards)

## Features Utilized for the project

  | Feature        | Description                           |
  |----------------|---------------------------------------|
  | Read TWO data files| Used 2 CSV files from kaggle          |
  | Clean your data and perform a pandas merge with your two data sets, then calculate correlation and statistical signifigance.      | Cleaned my data and merged them with pandas & SQL. The calculated stats from various data points |
  | Make 3 matplotlib, and Seaborn| Made various plots to show off my findings. |
  | Make a Tableau dashboard      | Made a dashboard with my findings. [Tableau](https://public.tableau.com/authoring/SpiritsandSasquatchAnalyzingAlcoholConsumptionandBigfootSightingsintheU_S_/Dashboard1#1) |
  | Utilize a virtual environment      | Made a venv for this project to keep my computer clean. |
  | Notate your code with markdown cells in Jupyter Notebook | Included in my code, you will find clear notes describing each code block. |


### Data Sources:
Bigfoot Sightings Dataset ([Kaggle](https://www.kaggle.com/datasets/josephvm/bigfoot-sightings-data))
Contains details on reported Bigfoot encounters, including state, date, latitude/longitude, and sighting descriptions.
Alcohol Consumption Dataset ([IHME United States Alcohol Use Prevalence by County 2002-2012: National](https://ghdx.healthdata.org/sites/default/files/record-attached-files/IHME_USA_COUNTY_ALCOHOL_USE_PREVALENCE_2002_2012_NATIONAL.zip))
Provides U.S. state-level per capita alcohol consumption over time, categorized by beverage type (beer, wine, spirits).

### Database & SQL Setup:
Load both datasets into a SQL database.
Create tables:
bigfoot_sightings (id, date, state, latitude, longitude, description, classification)
alcohol_consumption (state, year, beer_per_capita, wine_per_capita, spirits_per_capita, total_per_capita)
Perform SQL queries to:
Aggregate Bigfoot sightings per state per year.
Join both datasets on state and year for analysis. (Year, State, Avg_alcohol_consumption, Bigfoot_sightings)

### Data Cleaning & Processing (Python):
Handle missing/null values.
Convert dates to a uniform format.
Standardize state names for accurate joins.
Remove outliers (e.g., duplicate sightings, extreme alcohol values).

### Exploratory Data Analysis (EDA):
Calcualte correlation and statistical signifigance per state and year and overall
Create visualizatoins to view correlation and signifigance

### Tableau Dashboard Design (Time Permitting):

Create an interactive dashboard with Tableau Public

### Conclusion & Insights:
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

## Getting Started

To run this project, follow these steps:

1. Clone the repository: `git clone https://github.com/SarahMontesAlvarez/BigFoot-Alcohol-Project.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Explore the Jupyter notebooks or scripts in the respective folders.

## Dependencies

Pandas
MatPlotLib
Seaborn

###  Virtual Environment Instructions
---
1. After you have cloned the repo to your machine, navigate to the project 
folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. 
1. Activate the virtual environment.
1. Install the required packages. 
1. When you are done working on your repo, deactivate the virtual environment.

Virtual Environment Commands

| Command | Linux/Mac | GitBash |
|---------|-----------|---------|
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |