
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_file_path = 'dataset.csv'
data_df = pd.read_csv(data_file_path, skiprows=4)

# Filter data for CO2 emissions (metric tons per capita)
co2_emissions_data = data_df[data_df['Indicator Code'] == 'EN.ATM.CO2E.PC']

# Calculate the global average of CO2 emissions per year
global_co2_average = co2_emissions_data.mean()

# Plotting the Global Trend Plot for CO2 Emissions
plt.figure(figsize=(15, 7))
plt.plot(global_co2_average.index, global_co2_average.values, marker='o', linestyle='-', color='b')
plt.title('Global CO2 Emissions Trend (1960-2021)')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (Metric Tons Per Capita)')
plt.grid(True)
plt.show()
