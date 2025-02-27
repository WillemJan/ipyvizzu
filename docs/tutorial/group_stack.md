---
csv_url: ../../assets/data/music_data.csv
---

# Group/stack

The following example shows how to group and stack elements of a bar chart.

To get a stacked chart, you need to add a new dimension to the same channel
where the measure is: the y-axis. However, since doing only this would result in
multiple column chart elements with the same color stacked on top of each other,
we also add the same dimension to the color channel.

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
                    "y": {"set": ["Popularity"]},
                    "x": {"set": ["Genres"]},
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
                "y": {"attach": ["Kinds"]},
                "color": {"attach": ["Kinds"]},
            }
        }
    )
)
```

By detaching this newly added dimension from the y-axis and attaching it to the
x-axis, you get a grouped bar chart in a way that is easy to follow for the
viewer.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": ["Kinds"]},
                "x": {"attach": ["Kinds"]},
            },
        }
    )
)
```

In order to change the category via which the elements are grouped, just change
the order of the dimension with another one on the same axis.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"set": ["Kinds", "Genres"]},
            },
        }
    )
)
```

To stack a grouped chart, you just have to do the same thing the other way
around: detach the dimension from the x-axis and attach it to the y-axis.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"attach": "Kinds"},
                "x": {"detach": "Kinds"},
            },
        }
    )
)
```

<script src="../group_stack.js"></script>
