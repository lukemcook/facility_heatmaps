import folium
from folium.plugins import HeatMap

# Define the center cooardinates for Japan
center_lat, center_lon = 36.2048, 138.2529  # Approximate center of Honshu

# Base map with English labels
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=6,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
    attr='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ'
)

# coordinates of facilities
data_centers = [
# ****removed for privacy/ to protect company secrets****
]

# Add markers with labels for each data center
for lat, lon, label in data_centers:
    folium.Marker(
        location=[lat, lon],
        popup=label,
        icon=folium.Icon(color='blue', icon='cloud', prefix='fa')
    ).add_to(m)

# Prepare data for the heatmap
heat_data = [[lat, lon] for lat, lon, _ in data_centers]

# Add the heatmap layer
HeatMap(heat_data).add_to(m)

# Save the map as an HTML file
m.save('data_centers_markers_with_heatmap.html')
