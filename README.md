# REST API for Covid-19 in India

## Data-cleansing/Transformation process on the Dataset
 * Formatted dates (YYYY-MM-DD format).
 * Formatted time (from 12-hour to 24-hour format).
 * Missing values for the no. of hospitals and beds have been replaced by the mean values.
 * Missing age values have been replaced by mode.
 * Age ranges have been replaced by the mean of the lower bound and upper bound.
 * After decimal part has been ignored for ages (some ages were in decimal).
 * In StatewiseTestingDetails.csv, positive_cases + negative_cases = total_samples, so if one of the two values is missing (i.e. pos. or neg.) it is substituted by performing substraction from total samples but if both are missing then 0 is assigned.
 * Finally there are columns in dataset where more than 80-90% of the values is missing, these columns have been simply ignored.

## Loading of Dataset into Database
 * Load csv file into dataframe using pandas.
 * Reload the database by hitting the required endpoint (check [urls.py](https://github.com/WizArdZ3658/REST-API-for-COVID19-in-INDIA/blob/master/covid_api/covid/urls.py)).
 * Perform transformations.
 * It will create each object (row by row) and then save it in the database.
 * Databse used is SQLite (because of small application).

## Technology Stack
##### Languages :-
Python

##### Frameworks, Libraries and Tools:-
Django, Django-REST-Framework, Pandas, Numpy, Git

##### Databases:-
SQLite, Postgresql

##### Environment:-
Windows(my PC)
