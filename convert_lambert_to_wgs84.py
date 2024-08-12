import pandas as pd
from pyproj import Proj, transform

# Define the Lambert-93 and WGS84 projections
lambert93 = Proj(init='epsg:2154')
wgs84 = Proj(init='epsg:4326')

# Read the Excel file
input_file = 'your_input_file.xlsx'  # Replace with your actual file name
df = pd.read_excel(input_file)

# Function to convert Lambert-93 to WGS84
def lambert_to_wgs84(x, y):
    lon, lat = transform(lambert93, wgs84, x, y)
    return lon, lat

# Apply the conversion function to the dataframe
df['Longitude'], df['Latitude'] = zip(*df.apply(lambda row: lambert_to_wgs84(row['coordonneeLambertAbscisseEtablissement'], row['coordonneeLambertOrdonneeEtablissement']), axis=1))

# Save the updated dataframe to a new Excel file
output_file = 'converted_coordinates.xlsx'
df.to_excel(output_file, index=False)

print(f"Conversion completed. The updated file has been saved as {output_file}")
