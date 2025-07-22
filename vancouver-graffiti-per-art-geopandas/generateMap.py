import geopandas as gpd
import folium
import branca.colormap as cm

def make_style_function(column, colormap):
    def style_function(feature):
        value = feature["properties"].get(column)
        return {
            "fillColor": colormap(value) if value is not None else "#999999",
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.7,
        }
    return style_function

areasFile = 'data/final/local-area-boundary.geojson'
graffittiFile = 'data/final/graffiti.geojson'
publicArtFile = 'data/final/public-art.geojson'


areasDF = gpd.read_file(areasFile)
graffittiDF = gpd.read_file(graffittiFile)
publicArtDF = gpd.read_file(publicArtFile)

# Count Graffitis per area
# use size instead of count
# count returns another dataframe (table) and for each column it sets the number of non null occurrences per group
# size returns a series (list) with the number of rows in each group
graffittiCount = areasDF.sjoin(graffittiDF, how="left", predicate="contains").groupby(['name']).size().reset_index(name="grafitti")
# fillna will handle all empty values
areasDF = areasDF.merge(graffittiCount, on="name", how="left").fillna({"grafitti": 0})

# Count PublicArt per area
publicArtCount = areasDF.sjoin(publicArtDF, how="left", predicate="contains").groupby(['name']).size().reset_index(name="publicArt")
areasDF = areasDF.merge(publicArtCount, on="name", how="left").fillna({"publicArt": 0})

# Calculate ratio per area
areasDF["graffitti_per_art"] = round(areasDF["grafitti"] / areasDF["publicArt"], 2)

# Display on web map
m = folium.Map()
minx, miny, maxx, maxy = areasDF.total_bounds

# Fit the map to the bounds of the data
m.fit_bounds([[miny, minx], [maxy, maxx]])

colormap = cm.linear.YlOrRd_09.scale(areasDF["graffitti_per_art"].min(), areasDF["graffitti_per_art"].max())
colormap.caption = "Population"

folium.GeoJson(
    areasDF,
    name="Areas",
    style_function=make_style_function("graffitti_per_art", colormap),
    tooltip=folium.GeoJsonTooltip(fields=['name', 'area_m2', "grafitti", "publicArt", "graffitti_per_art"]),
    highlight_function=lambda x: {"weight": 3},
).add_to(m)

folium.LayerControl().add_to(m)

m.save("output.html")