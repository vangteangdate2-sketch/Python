import pandas as pd
import plotly.express as px

data = {
    'Day': [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday','Sunday'
    ],
    'Sales': [
        100,200,300,400,500,600,700
    ]
}

df = pd.DataFrame(data)
fig = px.bar(
    df,
    x = 'Day',
    y = 'Sales',
    title = 'Weekly E-commerce Sales',
    labels ={
        'Sales': 'Sales ($)', 'Days': 'Days'
    }
)

fig.show()
