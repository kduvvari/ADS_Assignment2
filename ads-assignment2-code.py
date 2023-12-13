#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 02 20:54:07 2023
@author: Kumari
"""

"""
# Importing required libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import skew
from scipy.stats import kurtosis


def dataframe(nameOfFile):
    """
       load dataset using pandas and return country and year columns data

       Parameters:
       - nameOfFile (str): the file location of the CSV file holding data
       from the World Bank.

       Returns:
       - countryData : Data with country column.
       - yearData : Data with year column

    """
    countryData = pd.read_csv(nameOfFile)
    yearData = countryData.copy()
    yearData[['Country Name' , 'Time']] = yearData[['Time' , 'Country Name']]
    yearData = yearData.rename(columns = {'Country Name': 'Time' , 'Time':
        'Country Name'})

    return countryData , yearData


def bargraph(data):
    """
        Plots a bar graph for the given data, comparing
        'access_to_electricity%' and '
        individuals_using_internet%'.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the data for
        the plot.

        Returns:
        - None
    """
    bar_width = 0.35
    # Plotting bar graph
    plt.figure(figsize = (12 , 8))
    data = data.copy()
    data = data[(data['Time'] >= 2008) & (data['Time'] <= 2015)]
    for country in ['India']:
        country_data = data[data['Country Name'] == country]
        bar_positions_agriculture = country_data['Time'] - bar_width / 2
        bar_positions_forest = country_data['Time'] + bar_width / 2
    plt.bar(bar_positions_agriculture , country_data['GDP growth (annual %)'] ,
            width = bar_width , label = 'GDP growth (annual %) ' , color = 'blue')
    country_data = country_data.copy()
    country_data['Net migration_per'] = (country_data['Net migration'] /
                                         country_data['Net migration'].sum()) * 100
    plt.bar(bar_positions_forest , country_data['Net migration_per'] , width = bar_width ,
            label = 'Net migration' , color = 'green')


    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('GDP GROWTH Vs NET MIGRATION (INDIA)' , fontsize = 18)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def heatmap(correlation_matrix):
    """
        Creates a heatmap for the correlation matrix.

        Parameters:
        - correlation_matrix (pd.DataFrame): The correlation matrix to visualize.

        Returns:
        - None
        """

    # Check if the correlation matrix has data
    if not correlation_matrix.empty:
        # Create a heatmap for the correlation matrix
        plt.figure(figsize = (12 , 8))
        heatmap = sns.heatmap(correlation_matrix , annot=True , cmap='coolwarm' ,
                              fmt=".5f" , linewidths=.10 ,annot_kws={"size": 12})
        # Add axis labels
        plt.xlabel('Indicators')
        plt.ylabel('Indicators')
        # Add color bar label
        cbar = heatmap.collections[0].colorbar
        cbar.set_label('Correlation Coefficient')
        plt.title('Correlation Matrix for Selected World Bank Indicators' , fontsize=18)
        plt.show()
    else:
        print("Correlation matrix is empty.")


def lineGraph(data):
    """
        Plots a line graph showing the agricultural land percentage over the
        years for selected countries.

        Parameters:
        - data (pd.DataFrame): The DataFrame containing the data for the plot.

        Returns:
        - None
        """
    data = data[(data['Time'] >= 2010) & (data['Time'] <= 2020)]
    for country in ['India', 'Ireland' , 'United States' , 'United Arab Emirates' ,
                    'United Kingdom']:
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'] , country_data['Unemployment, total (% of total)'] ,
                 label=country)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Unemployment')
    plt.title('Unemployment Over the Years' , fontsize=18)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)
    plt.show()


def barGraph2(data):
    bar_width = 0.35
    data = data[(data['Time'] >= 2010) & (data['Time'] <= 2020)]
    for country in ['United States']:
        country_data = data[data['Country Name'] == country]
        bar_positions_agriculture = country_data['Time'] - bar_width / 2
        bar_positions_forest = country_data['Time'] + bar_width / 2
    plt.bar(bar_positions_agriculture , country_data['Current health expenditure (% of GDP) '] ,
            width=bar_width , label='Current health expenditure (% of GDP) ' , color='blue')
    plt.bar(bar_positions_forest , country_data['Domestic general government health expenditure (% of GDP)'] ,
            width=bar_width ,
            label='Domestic general government health expenditure (% of GDP)' , color='green')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title('Domestic general government Vs Current health expenditure' , fontsize=18)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()


def pieGraph(data):
    data = data[(data['Time'] == 2020)]
    countrynames = []
    sizes = []
    for country in ['United States' , 'India' , 'United Kingdom' , 'Singapore' , 'Philippines']:
        countrynames.append(country)
        country_data = data[data['Country Name'] == country]
        sizes.append(country_data['Domestic general government health expenditure (% of GDP)']
                     .values[0])
        print(country_data['Domestic general government health expenditure (% of GDP)']
              .values)


    # Create a pie chart
    plt.pie(sizes , labels=countrynames , autopct='%1.1f%%' , startangle=90)

    # Customize the plot as needed
    plt.title('Domestic general government health expenditure (% of GDP)' , fontsize=18)

    # Show the plot
    plt.show()


# Example Usage
file = 'DATA.csv'
country_Data , year_Data = dataframe(file)
print('***********************')
print("country Data")
print('***********************')

print(country_Data.head())
print('***********************')
print("year Data")
print('***********************')
print(year_Data.head())


#statistical analysis
print('***********************')
print("""Statistical analysis""")
print('***********************')

"""
From describe we can conclude that there are 130 data points in the dataset.
The avg population across the entities is 
approximately 183,608,200.
The smallest population value in the dataset is approximately 1,444,277.25% 
of the entities have a population 
less than or equal to approximately 4,820,049.
The median population, representing the middle value when the data is sorted, 
is approximately 14,786,470.
75% of the entities have a population less than or equal to approximately 100,918,900.
The largest population value in the dataset is approximately 1,396,387,000.

"""
statistics_describes = country_Data['Population, total '].describe()
print("***** DESCRIBES")
print(statistics_describes)


print("******* SKEWNESS")
skew_column_name = 'Water productivity, total '
# Calculate skewness
skewness = country_Data[skew_column_name].dropna().apply(pd.to_numeric , errors='coerce').skew()
print("Skewness for water productivity: " , skewness)
print("positive skewness suggests that there might be a few instances or "
      "entities with exceptionally high water productivity values,"
      " contributing to the longer right tail.")

print("******* Kurtosis")
kurtosisData = country_Data['Forest area (% of land area)'].dropna()
kurtosis_value = kurtosis(kurtosisData , fisher=False)
print("Kurtosis:" , kurtosis_value)
print("A kurtosis value of 1.7690071157448517 suggests that the distribution of the "
      "forest data has relatively "
      "heavy tails and a sharper peak compared to a normal distribution. "
      "This implies that there may be some outliers "
      "or extreme values in the dataset, leading to a more peaked distribution.")


#Bar Graph
bargraph(country_Data)
#Heat map
# Select a few indicators for analysis
country_Data['totalPOpulation_per'] = (country_Data[
                                           'Population, total '] /
                                       country_Data[
                                           'Population, total '].sum()) * 100

selected_indicators = ['GDP growth (annual %)', 'Unemployment, total (% of total)' ,
                       'totalPOpulation_per']
# Extract the relevant data for the selected indicators
df_selected_indicators = country_Data[selected_indicators]
# Calculate the correlation matrix
correlation_matrix = df_selected_indicators.corr()
heatmap(correlation_matrix)

lineGraph(country_Data)

country_Data['waterProductivity_per'] = (country_Data['Water productivity, total ']
                                         /country_Data['Water productivity, total '].sum()) * 100

selected_indicators = ['Forest area (% of land area)' , 'waterProductivity_per']
# Extract the relevant data for the selected indicators
df_selected_indicators = country_Data[selected_indicators]
# Calculate the correlation matrix
correlation_matrix = df_selected_indicators.corr()
heatmap(correlation_matrix)

barGraph2(country_Data)
pieGraph(country_Data)



