import pandas as pd
from map_renderer import MapRenderer

points_df = pd.read_csv("points.csv")
districts_df = pd.read_csv("districts_convex_hull.csv")

renderer = MapRenderer(districts_df, points_df)
print(renderer.get_map())