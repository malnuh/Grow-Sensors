import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Load the dataset containing GROW sensor locations
df = pd.read_csv('Growlocations.csv')

# Correct the latitude and longitude values
df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude']

# Filter out data points with invalid geographic coordinates
df = df[(df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985) &
        (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)]

# Remove duplicate entries based on Latitude and Longitude
df = df.drop_duplicates(subset=['Latitude', 'Longitude'])

# Load the map image of the United Kingdom
map = plt.imread('map7.png')  

# Create a scatter plot with the map as the background
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(map, extent=[-10.592, 1.6848, 50.681, 57.985])

# Plot the GROW sensor locations on the map
ax.scatter(df['Longitude'], df['Latitude'], color='green', s=30, label='Sensor Locations')

# Set plot title and axis labels
plt.title('Geographic Distribution of GROW Sensors in the United Kingdom')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Display the legend
plt.legend()

# Display the plot
plt.show()

# Save the cleaned dataset to a new CSV file
df.to_csv('Growlocations_corrected.csv', index=False)

# Save the plot as a PNG file
plt.savefig('GrowLocationsMap1.png')
