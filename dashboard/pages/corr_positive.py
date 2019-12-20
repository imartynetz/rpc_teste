import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import sys
sys.path.insert(1, '../')
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import dash_table

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

patri_pos = pd.read_csv(DATA_PATH.joinpath("patrimônio_positivo.csv"))
patri_pos['Dívida'] = patri_pos['Dívida'].map(lambda x: '{0:.2f}'.format(x))
patri_pos['Capacidade de pagamento anual'] = patri_pos['Capacidade de pagamento anual'].map(lambda x: '{0:.2f}'.format(x))
patri_pos['patrimônio'] = patri_pos['patrimônio'].map(lambda x: '{0:.2f}'.format(x))
patri_pos['patrimônio_percent'] = patri_pos['patrimônio_percent'].map(lambda x: '{0:.2f}%'.format(x))
patri_pos['cumulative_patri_percent'] = patri_pos['cumulative_patri_percent'].map(lambda x: '{0:.2f}%'.format(x))

patri_pos.rename(columns={"house": "House",
                          "Dívida": "Dívida (R$)",
                          "patrimônio": "Patrimônio (R$)",
                          "Capacidade de pagamento anual": 'Capacidade de pagamento anual (R$)',
                          "patrimônio_percent": "Patrimônio Percentual",
                          "cumulative_patri_percent": "Patrimônio Percentual cumulativo",
                          "Class": "Classe"}, inplace=True)



a_percent = round(len(patri_pos[patri_pos.Classe == "A"])/len(patri_pos)*100, 2)
b_percent = round(len(patri_pos[patri_pos.Classe == "B"])/len(patri_pos)*100, 2)
c_percent = round(len(patri_pos[patri_pos.Classe == "C"])/len(patri_pos)*100, 2)


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    # Row 1
                    dcc.Graph(
                        id='basic-interactions',
                        figure={
                            'data': [
                                go.Bar(
                                    x=patri_pos.loc[patri_pos.Classe == "A", "House"].values,
                                    y=patri_pos.loc[patri_pos.Classe == "A", 'Patrimônio (R$)'].values,
                                    marker={"color": "rgb(0,100,0)"},
                                    name=f"Classe A:"
                                ),
                                go.Bar(
                                    x=patri_pos.loc[patri_pos.Classe == "B", "House"].values,
                                    y=patri_pos.loc[patri_pos.Classe == "B", 'Patrimônio (R$)'].values,
                                    marker={"color": "rgb(34,163,192)"},
                                    name=f"Classe B:"
                                ),
                                go.Bar(
                                    x=patri_pos.loc[patri_pos.Classe == "C", "House"].values,
                                    y=patri_pos.loc[patri_pos.Classe == "C", 'Patrimônio (R$)'].values,
                                    marker={"color": "rgb(255,105,97)"},
                                    name=f"Classe C:"
                                ),
                                go.Scatter(
                                    name="Cumulative Percentage",
                                    x=patri_pos.House.values,
                                    y=patri_pos["Patrimônio Percentual cumulativo"].values,
                                    yaxis="y2",
                                    line={"color": "rgb(243,158,115)", "width": 2.4},
                                )
                            ],
                            'layout': {
                                "font": {
                                    "size": 12,
                                    "color": "rgb(128,128,128)",
                                    "family": "Balto, sans-serif"
                                },
                                "title": "Curva ABC",
                                "width": "100vh",
                                "xaxis": {"tickangle": -90},
                                "yaxis": {
                                    "title": "Patrimônio Acumulado (R$)",
                                    "tickfont": {"color": "rgba(34,163,192,.75)"},
                                    "titlefont": {
                                        "size": 13,
                                        "color": "rgba(34,163,192,.75)",
                                        "family": "Balto, sans-serif"
                                    }
                                },
                                "height": "40vh",
                                "legend": {
                                    "x": 0.83,
                                    "y": 2,
                                    "font": {
                                        "size": 13,
                                        "color": "rgba(128,128,128,.75)",
                                        "family": "Balto, sans-serif"
                                    }
                                },
                                "margin": {
                                    "b": 155,
                                    "l": 100,
                                    "r": 60,
                                    "t": 65
                                },
                                "yaxis2": {
                                    "side": "right",
                                    "range": [0, 101],
                                    "tickfont": {"color": "rgba(243,158,115,.9)"},
                                    "tickvals": [0, 20, 40, 60, 80, 100],
                                    "overlaying": "y"
                                },
                                "hovermode": "compare",
                                "titlefont": {
                                    "size": 0,
                                    "color": "",
                                    "family": ""
                                },
                                "showlegend": True,
                                "annotations": [
                                    {
                                        "x": 1.1,
                                        "y": 1,
                                        "font": {
                                            "size": 13,
                                            "color": "rgba(243,158,115,.9)",
                                            "family": "Balto, sans-serif"
                                        },
                                        "text": "Percentual Cumulativo (%)",
                                        "xref": "paper",
                                        "yref": "paper",
                                        "showarrow": False,
                                        "textangle": 90
                                    }
                                ],
                                "plot_bgcolor": "rgb(240, 240, 240)",
                                "paper_bgcolor": "rgb(240, 240, 240)"
                            }
                        }
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Dados correntistas"], className="subtitle padded"
                                    ),
                                    dash_table.DataTable(
                                        id='patri_pos',
                                        columns=[{"name": i, "id": i} for i in patri_pos.columns],
                                        data=patri_pos.to_dict("rows"),
                                        fixed_rows={'headers': True, 'data': 0},
                                        style_table={
                                            'height': '40vh',
                                            'width': '70vh',
                                            'overflowY': 'scroll',
                                            'border': 'thin lightgrey solid'
                                        },
                                        style_data_conditional=[
                                            {
                                                'if': {'row_index': 'odd'},
                                                'backgroundColor': 'rgb(248, 248, 248)'
                                            },
                                            {'if': {'column_id': 'House'},
                                             'width': '10px'},
                                            {'if': {'column_id': 'Dívida (R$)'},
                                             'width': '50px'},
                                            {'if': {'column_id': 'Capacidade de pagamento anual (R$)'},
                                             'width': '110px'},
                                            {'if': {'column_id': 'Patrimônio (R$)'},
                                             'width': '40px'},
                                            {'if': {'column_id': 'Patrimônio Percentual'},
                                             'width': '110px'},
                                            {'if': {'column_id': 'Patrimônio Percentual cumulativo'},
                                             'width': '110px'},
                                            {'if': {'column_id': 'Classe'},
                                             'width': '30px'},
                                        ],
                                        style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'},
                                        virtualization=True,
                                    )
                                ],
                                className="row",
                            ),
                        ]),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Resultado"),
                                    html.Br([]),
                                    html.P(
                                        "As famílias foram divididas em 3 grupos: Grupo A que que detêm 50% de toda a "
                                        "renda total e consiste em torno de 11% do total de famílias, Grupo B que detêm "
                                        "30% de toda a renda e consiste em torno de 30% do total de família, e o grupo C "
                                        "que detêm 20% de toda a renda e consiste em torno de 58% de todas as famílias, "
                                        "sendo essas famílias somente as famílias com renda positiva. Com isso as "
                                        "famílias do grupo A são as melhores para se investir, pois são as famílias, que "
                                        "sozinhas conseguem ter, juntas, um lucro anual correspondente a 50% de todas as "
                                        "famílias. Famílias do grupo B podem ser possíveis investidor, e famílias do grupo"
                                        "C são famílias no grupo de risco.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            ),
                        ],
                        className="row",
                        # style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
