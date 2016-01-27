import geohash
import json

coll = { "type": "FeatureCollection", "features": []}

h = geohash.encode(48.862004, 2.33734, precision=5)
cells = [h] + geohash.neighbors(h)

for cell in cells:
	b = geohash.bbox(cell)
	coordinates = []

	coordinates.append( [ b['e'], b['s'] ])	
	coordinates.append( [ b['e'], b['n'] ])	
	coordinates.append( [ b['w'], b['n'] ])	
	coordinates.append( [ b['w'], b['s'] ])	
	coordinates.append( [ b['e'], b['s'] ])	

	feat = {
		"type": "Feature", 
		"properties": {"name": cell}, 
		"geometry": { 
			"type": "Polygon",
			"coordinates": [ coordinates ]
			}
		}

	coll["features"].append(feat)

print json.dumps(coll)