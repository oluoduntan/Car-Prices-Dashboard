from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

stylesheet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
'''def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Load the Data
df = pd.read_csv('vehicles1.csv')

# Load the Dash app
app = Dash(__name__, external_stylesheets=stylesheet)
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Average Car Price For Each State", style={'text-align': 'center'}),
    html.P(children="Analyze the behavior of avocado prices"
                " and the number of avocados sold in the US"
                " between 2015 and 2018"
            ),

    dcc.Dropdown(id="slct_year",
                 options=[{'label': i, 'value': i}
                          for i in sorted(df.year.unique())],
                 multi=False,
                 value=2015,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='my_bee_map', figure={}),
    html.Br(),
    # html.Center(id='output_table', children=[]),
    # html.Br(),
    # dcc.Graph(id='my_bee_bar', figure={})

    html.Div([
        html.Div([
            html.H5('Pie Chart Showing the Top 5 Most Common\nCar Manufacturers of the Year'),
            dcc.Graph(id='my_bee_bar', figure={})
        ], className="six columns"),

        html.Div([
            html.H5('Sample Data of Search Result'),
            html.Center(id='output_table', children=[])
        ], className="six columns"),
    ], className="row")

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure'),
     Output(component_id='output_table', component_property='children'),
     Output(component_id='my_bee_bar', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)


def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user is: {}".format(option_slctd)

    df_ = df.copy()
    df_ = df_[df_["year"] == option_slctd]
    dff = df_.groupby(['state', 'full_state'])['price'].mean().reset_index()
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig1 = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='price',
        hover_data=['state', 'price'],
        hover_name='full_state',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'price': 'Avg Car Price'},
        template='plotly_dark'
    )

    fig1.add_scattergeo(
        locations=dff['state'],
        locationmode='USA-states',
        text=dff['state'],
        mode='text')

    dff1 = ((df_.groupby('manufacturer')['price'].count().sort_values(ascending=False)[:5] / df_.shape[
        0]) * 100).reset_index()
    dff1 = dff1.append({'manufacturer':'Others', 'price':(100 - dff1['price'].sum())}, ignore_index=True)
    dff1 = dff1.rename({'manufacturer':'Manufacturer', 'price':'Percentage of Occurence'}, axis=1)
    fig2 = px.pie(data_frame=dff1, names='Manufacturer', values='Percentage of Occurence')

    # dff1 = ((df_.groupby('manufacturer')['price'].count().sort_values(ascending=False)[:5]/df_.shape[0]) * 100).reset_index()
    # dff1 = dff1.rename({'manufacturer':'Manufacturer', 'price':'Percentage of Occurence'}, axis=1)
    #
    # fig2 = px.bar(data_frame=dff1, x='Manufacturer', y='Percentage of Occurence')

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )
    df_ = df_.rename({'year':'Year', 'manufacturer':'Manufacturer', 'price':'Price', 'state':'State_Code', 'lat':'Latitude', 'long':'Longitude', 'full_state':'State'}, axis=1)
    df_ = df_[['Year', 'Manufacturer', 'State', 'State_Code', 'Latitude', 'Longitude']]
    return container, fig1, generate_table(df_), fig2


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)'''


def generate_table(dataframe, max_rows=8):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# Load the Data
df = pd.read_csv('vehicles1.csv')

# Load the Dash app
app = Dash(__name__, external_stylesheets=stylesheet)
# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Average Car Price For Each State", style={'text-align': 'center', 'color':'white', 'font-family': 'Times New Roman',
                                                       'border': '5px solid powderblue'}),
    html.P(children="Craigslist is the world's largest collection of used vehicles for sale. "
                    "This dashboard was built using a dataset that includes all used car entry in the United States "
                    "on Craiglist. The map shows the average car price for each state for the selected year. The pie-chart "
                    "shows the top five most common cars on sale for the selected  year.",
           style={'color':'white', 'font-family': 'Times New Roman', 'font-size':20}
            ),

    dcc.Dropdown(id="slct_year",
                 options=[{'label': i, 'value': i}
                          for i in sorted(df.year.unique())],
                 multi=False,
                 value=2015,
                 style={'width': "40%", 'background-color': '#0d0d0d'}
                 ),

    html.Div(id='output_container', children=[], style={'color':'white', 'font-family': 'Times New Roman'}),
    html.Br(),
    dcc.Graph(id='my_bee_map', figure={}),
    #html.Br(),
    # html.Center(id='output_table', children=[]),
    # html.Br(),
    # dcc.Graph(id='my_bee_bar', figure={})

    html.Div([
        html.Div([
            html.H5(''),
            dcc.Graph(id='my_bee_bar', figure={})
        ], className="six columns"),

        html.Div([
            html.H5('Sample Data of Search Result'),
            html.Center(id='output_table', children=[])
        ], className="six columns"),
    ], className="row", style={'color':'white', 'font-family': 'Times New Roman', 'font-size':17})

], style={'background-color': '#0d0d0d'})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure'),
     Output(component_id='output_table', component_property='children'),
     Output(component_id='my_bee_bar', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)


def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user is: {}".format(option_slctd)

    df_ = df.copy()
    df_ = df_[df_["year"] == option_slctd]
    dff = df_.groupby(['state', 'full_state'])['price'].mean().reset_index()
    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig1 = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state',
        scope="usa",
        color='price',
        hover_data=['state', 'price'],
        hover_name='full_state',
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'price': 'Avg Car Price'},
        template='plotly_dark'
    )

    fig1.add_scattergeo(
        locations=dff['state'],
        locationmode='USA-states',
        text=dff['state'],
        mode='text')

    dff1 = ((df_.groupby('manufacturer')['price'].count().sort_values(ascending=False)[:5] / df_.shape[
        0]) * 100).reset_index()
    dff1 = dff1.append({'manufacturer':'Others', 'price':(100 - dff1['price'].sum())}, ignore_index=True)
    dff1 = dff1.rename({'manufacturer':'Manufacturer', 'price':'Percentage of Occurence'}, axis=1)
    fig2 = px.pie(data_frame=dff1, names='Manufacturer', values='Percentage of Occurence',
                  title=f'Pie Chart Showing Top 10 Most Common Cars on Sale in {option_slctd}',
                  template='plotly_dark')

    # dff1 = ((df_.groupby('manufacturer')['price'].count().sort_values(ascending=False)[:5]/df_.shape[0]) * 100).reset_index()
    # dff1 = dff1.rename({'manufacturer':'Manufacturer', 'price':'Percentage of Occurence'}, axis=1)
    #
    # fig2 = px.bar(data_frame=dff1, x='Manufacturer', y='Percentage of Occurence')

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )
    df_ = df_.rename({'year':'Year', 'manufacturer':'Manufacturer', 'price':'Price', 'state':'State_Code', 'lat':'Latitude', 'long':'Longitude', 'full_state':'State'}, axis=1)
    df_ = df_[['Year', 'Manufacturer', 'State', 'State_Code', 'Price', 'Latitude', 'Longitude']]
    return container, fig1, generate_table(df_), fig2


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)