---
csv_url: ../../assets/data/music_data.csv
---

# Sorting

`ipyvizzu` provides multiple options to sort data. By default, the data is
sorted by the order it is added to `ipyvizzu`. This is why we suggest to add
temporal data such as dates in chronological order - from oldest to newest.

You can also sort the elements by value, which will provide you with an
ascending order.

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
                    "y": {"set": ["Popularity", "Kinds"]},
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
            "sort": "byValue",
        }
    )
)
```

If you want descending order instead, you have to set the `reverse` parameter to
`True`. When used without setting the sorting to `byValue`, the elements will be
in the opposite order than they are in the data set added to `ipyvizzu`.

<div id="tutorial_02"></div>

```python
chart.animate(
    Config(
        {
            "reverse": True,
        }
    )
)
```

This is how to switch back to the default sorting.

<div id="tutorial_03"></div>

```python
chart.animate(
    Config(
        {
            "sort": "none",
            "reverse": False,
        }
    )
)
```

When you have more than one dimension on a channel, their order determines how
the elements are grouped. For example, below - each set of bars is first
organized by `Genres`, and then we have one bar for each of `Kinds`.

<div id="tutorial_04"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "y": {"detach": ["Kinds"]},
                "x": {"set": ["Genres", "Kinds"]},
            }
        }
    )
)
```

When switching the order of dimensions on the x-axis `ipyvizzu` will rearrange
the elements according to this new logic.

!!! note
    The legend is automatically removed during the animation.

<div id="tutorial_05"></div>

```python
chart.animate(
    Config(
        {
            "channels": {
                "x": {"set": ["Kinds", "Genres"]},
            }
        }
    )
)
```

<script src="../sorting.js"></script>
