import folium
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd

# Load the Excel file
file_path = r'C:\Users\norsk\dijon_rest\dijon_et_beaune.xlsx'
data = pd.read_excel(file_path)

# Create a map centered around Dijon
m = folium.Map(location=[47.3220, 5.0415], zoom_start=13)

# Define colors for broad categories
category_colors = {
    'Restaurant': 'blue',
    'Hotel': 'darkblue',
    'Bar': 'pink',
    'Cafe': 'lightblue',
    'Brasserie': 'darkgreen',
    'Caterer': 'lightgreen',
    'Retirement': 'gray',
}

# Function to group categories
def categorize_establishment(category):
    if any(keyword in category.lower() for keyword in [
        'restaurant', 'brasserie', 'creperie', 'bistro', 'gastropub',
        'sushi', 'patisserie', 'takeout', 'buffet', 'steakhouse', 'grill', 
        'cafe', 'dim sum', 'fine dining', 'haute french', 'sandwich', 'salad',
        'wok', 'kebab', 'asian', 'japanese', 'chinese', 'thai', 'indian', 
        'italian', 'mexican', 'turkish', 'portuguese', 'moroccan', 'lebanese', 
        'korean', 'african', 'syrian', 'armenian', 'hawaiian', 'swedish', 
        'modern indian', 'latin american', 'sicilian', 'mandarin', 'vietnamese', 
        'sicilian', 'eritrean', 'swedish', 'tunisian', 'fusion', 'french'
    ]):
        return 'Restaurant'
    if 'caterer' in category.lower():
        return 'Caterer'
    if 'hotel' in category.lower():
        return 'Hotel'
    if 'bar' in category.lower():
        return 'Bar'
    if any(keyword in category.lower() for keyword in ['retirement', 'home', 'community']):
        return 'Retirement'
    return category

# Function to determine the color based on the category
def get_category_color(category):
    mapped_category = categorize_establishment(category)
    return category_colors.get(mapped_category, 'gray')

# Create a marker cluster layer
marker_cluster = MarkerCluster(name='Detailed View').add_to(m)

# Add markers to the map with colors based on grouped categories
for index, row in data.iterrows():
    category = row['categoryName']
    color = get_category_color(category)
    
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=(
            f"<b>{row['title']}</b><br>"
            f"{row['street']}<br>{row['city']} {row['postalCode']}<br>"
            f"{row['phone']}<br>{row['categoryName']}"
        ),
        tooltip=row['title'],
        icon=folium.Icon(color=color)
    ).add_to(marker_cluster)

# Create heatmap layer
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
heatmap = HeatMap(heat_data, name='Distribution View').add_to(m)

# Add layer control to the map
folium.LayerControl().add_to(m)

# Create a legend with adjusted size
legend_html = """
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 180px; height: 250px; 
            background-color: white; border:2px solid grey; z-index:9999; font-size:14px;
            overflow: auto;
            padding: 10px;">
            <b>Legend</b> <br>
            <i class="fa fa-map-marker fa-2x" style="color:blue"></i>&nbsp; Restaurant <br>
            <i class="fa fa-map-marker fa-2x" style="color:darkblue"></i>&nbsp; Hotel <br>
            <i class="fa fa-map-marker fa-2x" style="color:pink"></i>&nbsp; Bar <br>
            <i class="fa fa-map-marker fa-2x" style="color:lightblue"></i>&nbsp; Cafe <br>
            <i class="fa fa-map-marker fa-2x" style="color:darkgreen"></i>&nbsp; Brasserie <br>
            <i class="fa fa-map-marker fa-2x" style="color:lightgreen"></i>&nbsp; Caterer <br>
            <i class="fa fa-map-marker fa-2x" style="color:gray"></i>&nbsp; Retirement <br>
</div>
"""

# Add the legend to the map
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m.save('dijon_establishments_combined.html')

print("Map created without search functionality and saved as 'dijon_establishments_combined.html'")
