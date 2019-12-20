import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
import dash_table
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

patri_neg = pd.read_csv(DATA_PATH.joinpath("patrimônio_negativo.csv"))

patri_neg.rename(columns={"house": "House",
                          "patrimônio": "Patrimônio"}, inplace=True)
patri_neg['Dívida'] = patri_neg['Dívida'].map(lambda x: 'R$ {0:.2f}'.format(x))
patri_neg['Capacidade de pagamento anual'] = patri_neg['Capacidade de pagamento anual'].map(lambda x: 'R$ {0:.2f}'.format(x))
patri_neg['Patrimônio'] = patri_neg['Patrimônio'].map(lambda x: 'R$ {0:.2f}'.format(x))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Correntistas renda negativa"], className="subtitle padded"
                                    ),
                                    dash_table.DataTable(
                                        id='patri_pos',
                                        columns=[{"name": i, "id": i} for i in patri_neg.columns],
                                        data=patri_neg.to_dict("rows"),
                                        fixed_rows={'headers': True, 'data': 0},
                                        style_table={
                                            'height': '50vh',
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
                                className="Row",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H5("Resultado"),
                                            html.Br([]),
                                            html.P(
                                                "Todas essas famílias possuem renda anual negativa, ou seja, suas dívidas"
                                                "são maiores que a capacidade anual de pagamento, sendo assim famílias "
                                                "automaticamente caracterizadas como péssimas famílias a se investir.",
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
                        className="row ",
                    ),


                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
