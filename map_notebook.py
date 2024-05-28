import pandas as pd
from map_renderer import MapRenderer

districts_df = pd.read_csv("convex_hulls.csv")
points_df = pd.read_csv("points.csv")

renderer = MapRenderer(districts_df, points_df)
map_view = renderer.get_map()
print(map_view)