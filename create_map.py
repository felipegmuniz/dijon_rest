import folium
import pandas as pd
from folium.plugins import Search, MarkerCluster

# Load the Excel file
file_path = 'C:\\Users\\norsk\\dijon_rest\\dijon_et_beaune.xlsx'
data = pd.read_excel(file_path)

# Create a map centered around Dijon
m = folium.Map(location=[47.3220, 5.0415], zoom_start=13)

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers to the cluster
for index, row in data.iterrows():
    marker = folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=(
            f"<b>{row['title']}</b><br>"
            f"{row['street']}<br>{row['city']} {row['postalCode']}<br>"
            f"{row['phone']}<br>{row['categoryName']}"
        ),
        tooltip=row['title']
    )
    marker.add_to(marker_cluster)

# Add the search functionality to the marker cluster
search = Search(
    layer=marker_cluster,  # Correctly attaching to the marker cluster
    search_label='title',  # Ensure this matches your DataFrame's column name
    placeholder='Search for a restaurant...',
    search_zoom=14,
).add_to(m)

# Save the map to an HTML file
m.save('dijon_restaurants_map.html')

# Optionally, print a message when done
print("Map created and saved as 'dijon_restaurants_map.html'")
