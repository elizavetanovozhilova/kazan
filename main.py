import pandas as pd
from convex_hull_builder import ConvexHullBuilder

points_df = pd.read_csv("points.csv")
builder = ConvexHullBuilder(points_df)
result_df = builder.get_convex_hull()
result_df.to_csv('districts_convex_hull.csv', index=False)
