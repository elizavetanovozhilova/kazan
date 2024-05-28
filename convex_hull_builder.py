import pandas as pd
from scipy.spatial import ConvexHull
import numpy as np


class ConvexHullBuilder:
    def __init__(self, points: pd.DataFrame):
        self.__points = points

    def get_convex_hull(self) -> pd.DataFrame:
        result = []
        for district, group in self.__points.groupby('district'):
            points = group[['lat', 'lon']].values
            hull = ConvexHull(points)
            hull_points = points[hull.vertices]

            center = tuple(np.mean(hull_points, axis=0))
            color = self.__get_color(district)

            result.append({
                'district': district,
                'points': hull_points.tolist(),
                'center': center,
                'color': color
            })

        return pd.DataFrame(result)

    def __get_color(self, district: str) -> str:
        # Простой генератор цвета на основе хеша названия района
        np.random.seed(abs(hash(district)) % (2 ** 32))
        return '#%02X%02X%02X' % tuple(np.random.randint(0, 256, 3))

