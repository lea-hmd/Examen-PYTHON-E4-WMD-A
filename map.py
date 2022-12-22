import pandas as pd
import plotly.graph_objects as go

# Lecture du fichier csv et récupération des colonnes qui nous intéresse
data_frame = pd.read_csv(r"C:\Users\lhamadouche\Documents\ESTIAM\Python\Examen\brazil_flights_data.csv",
                         nrows=500, encoding="latin1")
data_frame = data_frame[["Voos", "Companhia.Aerea", "LongDest", "LatDest", "LongOrig",
                         "LatOrig", "Cidade.Origem", "Cidade.Destino", "Pais.Origem", "Pais.Destino"]]
# Affichage des premières entrées du data_frame
data_frame.head()

# Filtration du dataset (seulement les vols internationaux)
overseas_df = data_frame[(data_frame["Pais.Origem"] != data_frame["Pais.Destino"]) & (
    data_frame["Pais.Destino"] != "Brasil")]
overseas_cnt_df = overseas_df.groupby(["LongDest", "LatDest", "LongOrig", "LatOrig"]).count()[
    ["Voos"]].rename(columns={"Voos": "Num_Of_Flights"}).reset_index()
overseas_cnt_df = overseas_cnt_df.merge(data_frame, how="left", left_on=[
                                        "LongDest", "LatDest", "LongOrig", "LatOrig"], right_on=["LongDest", "LatDest", "LongOrig", "LatOrig"])


# On affiche seulement les 1000 premières entrées
overseas_cnt_df = overseas_cnt_df.sample(frac=1.0).head(1000)
overseas_cnt_df.head()

# Création du graph
fig = go.Figure()

source_to_dest = zip(overseas_cnt_df["LatOrig"], overseas_cnt_df["LatDest"],
                     overseas_cnt_df["LongOrig"], overseas_cnt_df["LongDest"],
                     overseas_cnt_df["Num_Of_Flights"])

# On itère à travers chaque entrée pour ajouter une ligne entre la source et la destination
for slat, dlat, slon, dlon, num_flights in source_to_dest:
    fig.add_trace(go.Scattergeo(
        lat=[slat, dlat],
        lon=[slon, dlon],
        mode='lines',
        line=dict(width=num_flights/100, color="blue")
    ))

# Création des étiquettes des villes des vols
cities = overseas_cnt_df["Cidade.Origem"].values.tolist(
)+overseas_cnt_df["Cidade.Destino"].values.tolist()
countries = overseas_cnt_df["Pais.Origem"].values.tolist(
)+overseas_cnt_df["Pais.Destino"].values.tolist()
scatter_hover_data = [country + " - " +
                      city for city, country in zip(cities, countries)]

# On itère à travers chaque entrée pour ajouter un point sur la source et la destination
fig.add_trace(
    go.Scattergeo(
        lon=overseas_cnt_df["LongOrig"].values.tolist(
        )+overseas_cnt_df["LongDest"].values.tolist(),
        lat=overseas_cnt_df["LatOrig"].values.tolist(
        )+overseas_cnt_df["LatDest"].values.tolist(),
        hoverinfo='text',
        text=scatter_hover_data,
        mode='markers',
        marker=dict(size=10, color='red', opacity=0.1,))
)

# Stylisation de la carte
fig.update_layout(title="Connection Map Depicting Flights from Brazil to All Other Countries (Orthographic Projection)",
                  height=500, width=500,
                  margin={"t": 0, "b": 0, "l": 0, "r": 0, "pad": 0},
                  showlegend=False,
                  geo=dict(projection_type='orthographic', showland=True, landcolor='lightgrey', countrycolor='grey'))

fig.show()
