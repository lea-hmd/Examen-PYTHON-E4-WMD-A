import pandas as pd
import plotly.graph_objects as go

cols = ['name', 'code', 'lat', 'long']
df = pd.read_csv('aeroports.csv', names=cols, header=None, quotechar='"', encoding='utf-8')

df.head()

# Création du graph
fig = go.Figure()

# On itère à travers chaque entrée pour ajouter un point sur la source et la destination
fig.add_trace(
    go.Scattergeo(
        lon=df["long"].values.tolist(
        ),
        lat=df["lat"].values.tolist(
        ),
        hoverinfo='text',
        mode='markers',
        marker=dict(size=10, color='red', opacity=0.1,))
)

# Stylisation de la carte
fig.update_layout(title="Exam python",
                  height=500, width=500,
                  margin={"t": 0, "b": 0, "l": 0, "r": 0, "pad": 0},
                  showlegend=False,
                  geo=dict(projection_type='orthographic', showland=True, landcolor='lightgrey', countrycolor='grey'))

fig.show()
