import psycopg2
import branca.colormap as cm
import os

# needs .env file with DB_CREDENTIALS="dbname={db} user={user} password={password}"
# .env supported by python-dotenv library
credentials = os.getenv("DB_CREDENTIALS")

# Functions that load db data locally on the server
# Flask will make them available, which will be downloaded on the js part of the html page

def getGraffitiPerPublicArt():
    conn = psycopg2.connect(credentials)
    cur = conn.cursor()
    cur.execute("select * from get_graffiti_per_public_art;")

    features = []
    # finding max and min to use in color ramp
    minGPA = None
    maxGPA = 0

    for row in cur.fetchall():
        id_, name, art, graffiti, graffitiPerArt, geometry, area_m2 = row

        if minGPA is None or graffitiPerArt < minGPA:
            minGPA = graffitiPerArt
        if graffitiPerArt > maxGPA:
            maxGPA = graffitiPerArt

        feature = {
            "type": "Feature",
            "geometry": geometry,  # JSON-compatible
            "properties": {
                "id": id_,
                "name": name,
                "art": art,
                "graffiti": graffiti,
                "graffitiPerArt": graffitiPerArt,
                "area_m2": area_m2
            }
        }
        features.append(feature)

    colormap = cm.linear.YlOrRd_09.scale(float(minGPA), float(maxGPA))

    for feature in features:
        gpa = float(feature["properties"]["graffitiPerArt"])
        feature["properties"]["color"] = colormap(gpa) if gpa is not None else "#999999"
    
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return geojson

def getGraffiti():
    conn = psycopg2.connect(credentials)
    cur = conn.cursor()
    cur.execute("select * from get_graffiti;")

    features = []
    for row in cur.fetchall():
        id_, geometry = row
        feature = {
            "type": "Feature",
            "geometry": geometry,  # JSON-compatible
            "properties": {
                "id": id_
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return geojson

def getPublicArt():
    conn = psycopg2.connect(credentials)
    cur = conn.cursor()
    cur.execute("select * from get_public_art;")

    features = []
    for row in cur.fetchall():
        id_, geometry, name, typeArt, status = row
        feature = {
            "type": "Feature",
            "geometry": geometry,  # JSON-compatible
            "properties": {
                "id": id_,
                "name": name,
                "type": typeArt,
                "status": status
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return geojson

def getCombineAll():
    geojson = {
        "graffitiPerPublicArt" : getGraffitiPerPublicArt(), 
        "graffiti": getGraffiti(), 
        "publicArt": getPublicArt()
    }

    return geojson