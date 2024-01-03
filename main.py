import plotly.io as pio
import json

pio.renderers.default = 'browser'

india_states = json.load(open("states_india.geojson", "r"))

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

print("India States ID Map:")
print(state_id_map)