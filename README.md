實作影片 [Indian Pythonista - Plotting Choropleth Maps using Python](https://www.youtube.com/watch?v=aJmaw3QKMvk)

Github：[IndianPythonista-PlottingChoroplethMaps](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps)

使用 Python 中的 Plotly 繪製 Choropleth 地圖，展示地理數據並提供豐富的可視化效果，適用於區域性統計如人口密度、性別比等。
## 繪製人口密度折線圖
![Population Density Across Indian States](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/64fd89a6-ec78-4b62-82c3-30562d2722f4)

## 繪製 log 轉換後的人口密度折線圖
![Log-scaled Population Density Across Indian States](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/bc8165c3-3b0c-4563-b50c-051bb071fb90)

## 使用 Plotly Express 繪製人口密度的地理資訊圖
![Plotly Express - India Population Density](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/4e3699c0-83b0-40a6-aba6-d6509d4e594b)

## 使用 Mapbox 繪製人口密度的地理資訊圖
![Mapbox - India Population Density](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/ef196167-305f-4f3d-ae11-ea17f161761c)

## 使用 Plotly Express 繪製性別比的地理資訊圖
![Plotly Express - India Sex Ratio](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/7aec7209-92b8-4014-9114-68a88695c707)


## 技術簡介：
1. Plotly: 是一家開發在線數據分析和可視化工具的技術公司，提供多種科學繪圖庫，其中包括plotly.py，一個用於Python的交互式、開源且基於瀏覽器的繪圖庫。
2. Plotly Express: 是plotly的一個高級Python繪圖庫，它提供了對複雜圖表的簡單語法，可以用於繪製choropleth maps。
3. GeoJSON: 是一種用於表示簡單地理特徵的開放標準格式，包含特徵的類型、幾何形狀（坐標）和非空間屬性。在此情境中，用於定義地理邊界。
4. Mapbox: 是一家提供自定義設計地圖的公司和平台，plotly中的`choropleth mapbox`函數使用mapbox基本地圖，可以根據需求使用不同風格的地圖。

## 實作步驟：
1. 下載印度各邦的 GeoJSON 文件，這將包含地理邊界的定義。
2. 利用 Pandas 從 Wikipedia 頁面下載 HTML 表格數據，轉換為 DataFrame，這些數據包含各邦的統計信息，如人口密度和性別比例。
3. 預處理數據，將人口密度轉換為整數形式。
    ![image](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/aa63861f-a505-4ce5-bcaa-bdc4db5c3b0f)
5. 為了繪製 Choropleth map，需要建立 geojson 特徵和 DataFrame 之間的映射，以便將統計信息映射到地理特徵。
    ![image](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/c4d4a797-3ddb-4571-85bb-c0a9e0c8894a)
7. 使用plotly express的`choropleth`函數創建choropleth map，設置數據框、位置、geojson、顏色（這裡是人口密度）等參數。
8. 調整地圖的視圖範圍和風格，以使其更適應印度的範圍。
    ![Population Density Across Indian States](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/64fd89a6-ec78-4b62-82c3-30562d2722f4)
9. 通過對人口密度應用對數變換，改進視覺效果。
    ![Log-scaled Population Density Across Indian States](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/bc8165c3-3b0c-4563-b50c-051bb071fb90)
10. 添加懸停提示，顯示每個地區的具體信息，如人口密度和地名。
    ![Plotly Express - India Population Density](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/4e3699c0-83b0-40a6-aba6-d6509d4e594b)
11. 使用mapbox基本地圖，使用不同的風格和視圖中心點，創建更豐富的地圖視覺效果。
    ![Mapbox - India Population Density](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/ef196167-305f-4f3d-ae11-ea17f161761c)
12. 通過使用diverging color scale，繪製性別比例的choropleth map，提供更具信息性的視覺化。
    ![Plotly Express - India Sex Ratio](https://github.com/RainBowT0506/IndianPythonista-PlottingChoroplethMaps/assets/109667537/7aec7209-92b8-4014-9114-68a88695c707)

## 專業術語
* Choropleth Map (分區地圖)：一種使用色彩編碼在地理地圖上表示區域數據的特殊地圖類型。
* GeoJSON (地理JSON)：一種開放標準格式，用於表示地理特徵的簡單地理數據，包括非空間屬性。
* Plotly：一家技術計算公司，提供在線數據分析和可視化工具，並為Python等語言提供科學繪圖庫。
* Plotly Express：Plotly的高級Python繪圖庫，提供簡單的語法來創建複雜的圖表。
* Mapbox：一家提供自定義設計地圖的公司和開放源碼地圖平台。
* Density Scale (密度比例)：用於表示地區人口密度的比例尺。
* Choropleth Map with Mapbox Base Maps (使用Mapbox基本地圖的分區地圖)：使用Mapbox提供的基本地圖樣式創建的分區地圖。
* Diverging Color Scale (分歧顏色刻度)：一種連續色彩刻度，通常用於區分正值和負值的情況，具有中點用於區分兩個極端。
* Hover Name (懸停名稱)：在choropleth地圖上，當鼠標懸停在某區域時顯示的標題名稱。
* Hover Data (懸停數據)：在choropleth地圖上，懸停時顯示的其他數據信息。
* Color Scale (色彩刻度)：指在地圖上使用的顏色範圍，根據數據值的變化呈現不同的色彩。
* Logarithmic Scale (對數刻度)：使用對數函數將數據值轉換成對數值，以平滑數據的變化。
* Map Access Token (地圖訪問令牌)：用於訪問Mapbox地圖服務的權限令牌，有時需要進行身份驗證。
## 參考
* [印度行政區人口列表](https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population)
* [Shapes of Indian administrative boundaries](https://un-mapped.carto.com/tables/states_india/public/map)
* [Plotly - Choropleth map](https://plotly.com/python/choropleth-maps/)
* [Plotly - Color Scales](https://plotly.com/python/colorscales/)
* [Mapbox Choropleth Maps in Python](https://plotly.com/python/mapbox-county-choropleth/)
* [Mapbox Map Layers in Python](https://plotly.com/python/mapbox-layers/)
* [面量圖 (Choropleth map)](https://zh.wikipedia.org/zh-tw/%E9%9D%A2%E9%87%8F%E5%9C%96)
* [Mapbox](https://www.mapbox.com/)
