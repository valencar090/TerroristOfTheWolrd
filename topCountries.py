# Plot a thematic - Top Terrorism Countries of the World (1970-2015).
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import iplot, init_notebook_mode
%matplotlib inline
import pandas as pd

init_notebook_mode(connected=True)

df = pd.read_csv("../input/top_terror_countries.csv")
locations = df["country_name_iso2"]

data = [ dict(
        type = 'choropleth',
        locationmode ="country names", 
        locations = df["country_name_iso2"],
        z = df['fatalities'],
        text = df["country_name_iso2"],
        colorscale = 'Electric'  ,         
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            #tickprefix = '$',
            title = 'fatalities<br>per 1.000'),
      ) ]

layout = dict(
    title = '1970-2015 Terrorism Attack<br>Source:\
            <a href="http://start.umd.edu/gtd/">\
            GTD Global Terrorism Database</a>',
    geo = dict(
        showframe = False,
        showcoastlines = True,
        showcountries = True,
        projection = dict(
            type = 'Mercator'
    
        )
    )
)

fig = dict( data=data, layout=layout )
iplot( fig, validate=False, filename='d3-world-map' )
