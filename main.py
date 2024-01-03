import plotly.io as pio
import json
import pandas as pd

pio.renderers.default = 'browser'
pd.set_option('display.max_columns', None)

india_states = json.load(open("states_india.geojson", "r"))

state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

print("India States ID Map:")
print(state_id_map)

df = pd.read_csv("india_census.csv")
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])

print(df.head())