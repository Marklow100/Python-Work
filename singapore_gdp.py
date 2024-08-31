import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file
file_path = r'C:\Users\User\OneDrive\Python Project\Linkedln\Economic Analysis_Singapore\gdp_run\200240824.xlsx'
data_adjusted = pd.read_excel(file_path, skiprows=9)

# Set the first row (which contains the years) as the header
data_adjusted.columns = data_adjusted.iloc[0]
data_adjusted = data_adjusted.drop(0).reset_index(drop=True)

# Extract the relevant rows for Manufacturing, Services, Construction, and GDP
manufacturing_adjusted = data_adjusted.loc[data_adjusted['Data Series'] == '    Manufacturing'].iloc[:, 1:].values.flatten()
services_adjusted = data_adjusted.loc[data_adjusted['Data Series'] == '  Services Producing Industries'].iloc[:, 1:].values.flatten()
construction_adjusted = data_adjusted.loc[data_adjusted['Data Series'] == '    Construction'].iloc[:, 1:].values.flatten()
gdp_adjusted = data_adjusted.loc[data_adjusted['Data Series'] == 'GDP At Current Market Prices'].iloc[:, 1:].values.flatten()

# Convert the values to numeric types
manufacturing_values_adjusted = pd.to_numeric(manufacturing_adjusted, errors='coerce')
services_values_adjusted = pd.to_numeric(services_adjusted, errors='coerce')
construction_values_adjusted = pd.to_numeric(construction_adjusted, errors='coerce')
gdp_values_adjusted = pd.to_numeric(gdp_adjusted, errors='coerce')

# Extract the years
years_adjusted = data_adjusted.columns[1:]
years_adjusted_numeric = pd.to_numeric(years_adjusted, errors='coerce')

# Filter out any NaN values in the years to match the length of the data
valid_years = years_adjusted_numeric[~years_adjusted_numeric.isna()]
valid_manufacturing_values = manufacturing_values_adjusted[:len(valid_years)]
valid_services_values = services_values_adjusted[:len(valid_years)]
valid_construction_values = construction_values_adjusted[:len(valid_years)]
valid_gdp_values = gdp_values_adjusted[:len(valid_years)]

# Plot the trends for Manufacturing, Services, Construction, and GDP over the valid years
plt.figure(figsize=(10, 6))
plt.plot(valid_years, valid_manufacturing_values, label='Manufacturing', marker='o')
plt.plot(valid_years, valid_services_values, label='Services', marker='o')
plt.plot(valid_years, valid_construction_values, label='Construction', marker='o')
plt.plot(valid_years, valid_gdp_values, label='GDP', marker='o', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Value in Million Dollars')
plt.title('Singapore Economy: Manufacturing, Services, Construction, and GDP Over Time')
plt.legend()
plt.grid(True)
plt.show()
