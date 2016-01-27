import json
import s2

coll = { "type": "FeatureCollection", "features": []}

region_rect = s2.S2LatLngRect(
    s2.S2LatLng.FromDegrees(2.250824, 48.819524),
    s2.S2LatLng.FromDegrees(2.421799, 48.900387))
    
coverer = s2.S2RegionCoverer()
coverer.set_min_level(10)
coverer.set_max_level(30)
coverer.set_max_cells(9)
covering = coverer.GetCovering(region_rect)

for cell in covering:
    new_cell = s2.S2Cell(cell)
    coordinates = []

    for i in [0, 1 ,2 ,3, 0]:
        vertex = new_cell.GetVertex(i)
        latlng = s2.S2LatLng(vertex)
        coordinates.append([latlng.lat().degrees(),
                           latlng.lng().degrees()])


    feat = {
        "type": "Feature", 
        "properties": {}, 
        "geometry": { 
            "type": "Polygon",
            "coordinates": [ coordinates ]
            }
        }

    coll["features"].append(feat)

#print coll
print json.dumps(coll)