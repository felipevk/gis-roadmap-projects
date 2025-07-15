# Week 3 - Raster Data

Practiced using QGIS to work with Raster Data. 

The goal is to categorize each zone by its average elevation. As an extra I also added hillshade visualization to the elevation model.

## What I Did
- Downloaded digital elevation model (https://opendata.vancouver.ca/explore/dataset/digital-elevation-model/information/)
- Loaded zone boundary data
- Used Zonal Statistics to calculate the average, min and max height of each zone in the polygon layer
- Displayed average height using graded symbology
- Displayed data as hillshade using a combination of hillshade + singleband pseudocolor layers
- Used Layout Loader templates

## Map Preview
![Vancouver Zone Mean Elevation](print.png)
![Vancouver Hillshade Elevation](print_hill.png)

## Skills Practiced
- Raster data handling
- Layer styling, filtering and symbology
- Zonal Statistics
- Hillshade visualization

## Tools
- QGIS
- OpenStreetMap / city open data
