---
csv_url: ../../assets/data/music_data.csv
---

# Without coordinates & noop channel

Certain chart types have neither measures nor dimensions on the axes such as
treemaps and bubble charts. This is a case when the `noop` channel comes in
handy for grouping and stacking elements in these kinds of charts.

To get to a treemap, we have to detach all dimensions and the measure from the
axes and put two of them on the `size` channel, whereas the other dimension is
still on the `color` channel.

<div id="tutorial_01"></div>

??? info "Info - How to setup Chart"
    ```python
    import pandas as pd
    from ipyvizzu import Chart, Data, Config

    df = pd.read_csv(
        "https://ipyvizzu.vizzuhq.com/latest/assets/data/music_data.csv"
    )
    data = Data()
    data.add_df(df)

    chart = Chart()

    chart.animate(data)

    chart.animate(
        Config(
            {
                "channels": {
                    "y": {"set": ["Kinds", "Popularity"]},
                    "x": {"set": ["Genres"]},
                    "color": {"set": ["Kinds"]},
                    "label": {"set": ["Popularity"]},
                },
            }
        )
    )
    ```

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {
                    "set": None,
                },
                "x": {
                    "set": None,
                },
                "size": {
                    "attach": ["Genres", "Popularity"],
                },
            }
        }
    )
)
```

Getting from a treemap to a bubble chart is simply by changing the geometry to
circle. This bubble chart is stacked by the `Kinds` dimension that is on the
`size` channel - this is why the bubbles are in separate, small groups.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "geometry": "circle",
        }
    )
)
```

In order to show all bubbles as one group, we use the `noop` (no operations)
channel for the `Genres` dimension. The `noop` channel enables us to have a
dimension on the chart, that doesn’t affect any parameter of the elements, only
their count.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "size": {"detach": "Genres"},
                "noop": {"set": "Genres"},
            }
        }
    )
)
```

<script src="../without_coordinates_noop_channel.js"></script>
