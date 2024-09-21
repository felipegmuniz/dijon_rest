import folium
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd

# Load the Excel file
file_path = 'C:\\Users\\norsk\\dijon_rest\\dijon_et_beaune.xlsx'
data = pd.read_excel(file_path)

# Function to simplify categories
def simplify_category(category):
    category = category.lower()
    if 'restaurant' in category or 'gastropub' in category:
        return 'Restaurant'
    elif 'ehpad' in category or 'senior' in category or 'retraite' in category:
        return 'EHPAD/École/Senior'
    return category.title()

data['categoryName'] = data['categoryName'].apply(simplify_category)

# Define colors for categories
category_colors = {
    'Restaurant': 'red',
    'Hospital': 'green',
    'EHPAD/École/Senior': 'blue',
    'Bar': 'purple',
    'Hotel': 'darkblue'
}

# Create the map
m = folium.Map(location=[47.3220, 5.0415], zoom_start=13)

# Create a marker cluster and explicitly name it
marker_cluster = MarkerCluster(name='Liste d\'établissements').add_to(m)

# Adding markers with custom popups
for index, row in data.iterrows():
    color = category_colors.get(row['categoryName'], 'gray')
    popup_html = f"""
    <div style="font-size: 12px; width: 200px;">
        <b style="font-size: 14px;">{row['title']}</b><br>
        {row['street']}<br>
        {row['postalCode']} {row['city']}<br>
        {row['categoryName']}
    </div>
    """
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color=color),
        tooltip=row['title']
    ).add_to(marker_cluster)

# Add heatmap layer
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
heatmap = HeatMap(heat_data, name='Heatmap Distribution')
m.add_child(heatmap)

# Create a wider legend
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 200px; height: auto; 
            background-color: white; border:2px solid grey; z-index:9999; font-size:14px;
            overflow: auto; padding: 10px;">
<b>Legend</b><br>'''
for category, color in category_colors.items():
    legend_html += f'<i style="background:{color};width: 12px;height: 12px;float: left;margin-right: 5px;"></i> {category}<br>'
legend_html += '</div>'
m.get_root().html.add_child(folium.Element(legend_html))

# Add layer controls to toggle visibility
folium.LayerControl().add_to(m)

# Save the map
m.save('dijon_restaurants_map.html')
print("Map updated with a wider legend and saved as 'dijon_restaurants_map.html'")
