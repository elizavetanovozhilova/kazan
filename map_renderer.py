import pandas as pd
from ipyleaflet import Map, Marker, Polygon, FullScreenControl, LegendControl
from ipywidgets import Layout

class MapRenderer:
    def __init__(self, district_data: pd.DataFrame, points_data: pd.DataFrame):
        self.__points_data = points_data
        self.__district_data = district_data

    def get_map(self) -> Map:
        center_lat = self.__points_data['lat'].median()
        center_lon = self.__points_data['lon'].median()

        m = Map(center=(center_lat, center_lon), zoom=11, layout=Layout(width='100%', height='800px'))
        m.add_control(FullScreenControl())

        legend_items = []

        for _, row in self.__district_data.iterrows():
            district = row['district']
            color = row['color']
            points = row['points']
            center = row['center']

            polygon = Polygon(
                locations=points,
                color=color,
                fill_color=color,
                fill_opacity=0.5
            )
            m.add_layer(polygon)

            marker = Marker(
                location=center,
                draggable=False,
                title=district
            )
            m.add_layer(marker)

            legend_items.append((district, color))

        legend = LegendControl({"Districts": legend_items}, name="Legend", position="topright")
        m.add_control(legend)

        return m
