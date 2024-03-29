import plotly.io as pio
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

pio.renderers.default = 'browser'
pd.set_option('display.max_columns', None)

# 載入印度各邦的地理資訊
india_states = json.load(open("states_india.geojson", "r"))

# 將各邦的地理資訊和編碼建立映射
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

print("India States ID Map:")
print(state_id_map)

# 載入人口普查資料
df = pd.read_csv("india_census.csv")

# 處理人口密度資料，添加 log 轉換後的欄位
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map[x])
df["DensityScale"] = np.log10(df["Density"])

# 處理性別比資料
df["SexRatioScale"] = df["Sex ratio"] - 1000

print(df.head())

# 繪製人口密度折線圖
df["Density"].plot()
plt.title("Population Density Across Indian States")
plt.xlabel("State")
plt.ylabel("Population Density")
plt.show()

# 繪製 log 轉換後的人口密度折線圖
df["DensityScale"].plot()
plt.title("Log-scaled Population Density Across Indian States")
plt.xlabel("State")
plt.ylabel("Log-scaled Population Density")
plt.show()

# 使用 Plotly Express 繪製人口密度的地理資訊圖
fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="DensityScale",
    hover_name="State or union territory",
    hover_data=["Density"],
    title="India Population Density",
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()

# 使用 Mapbox 繪製人口密度的地理資訊圖
fig = px.choropleth_mapbox(
    df,
    locations="id",
    geojson=india_states,
    color="DensityScale",
    hover_name="State or union territory",
    hover_data=["Density"],
    title="India Population Density",
    mapbox_style="carto-positron",
    center={"lat": 24, "lon": 78},
    zoom=3,
    opacity=0.5,
)
fig.show()

# 使用 Plotly Express 繪製性別比的地理資訊圖
fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color="SexRatioScale",
    hover_name="State or union territory",
    hover_data=["Sex ratio"],
    title="India Sex Ratio",
    color_continuous_scale=px.colors.diverging.BrBG,
    color_continuous_midpoint=0,
)
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
