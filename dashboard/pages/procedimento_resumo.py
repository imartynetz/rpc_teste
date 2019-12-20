import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Resumo"),
                                    html.Br([]),
                                    html.P(
                                        "Dataset contém correntista do banco Bravos, bem como quais correntista tiveram "
                                        "óbito, com isso a idéia é analisar esses dados e determinar quais correntistas "
                                        "são melhores de se investir, a partir de uma curva ABC, ou como é chamada "
                                        "também, de análise de Paretto",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Procedimento"),
                                    html.Br([]),
                                    html.P(
                                        "Para essa análise, primeiramente foi feito um tratamento de dados, corrigindo "
                                        "nomes errados (Starrkk para Stark por exemplo), removido das colunas numéricas "
                                        "tudo que não seja relacionado com float, removido linhas na qual continha "
                                        "somente valores com Nan para depois poder ser feito cálculos",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            ),
                        ],
                        className="row",
                        #style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Procedimento matemático"),
                                    html.Br([]),
                                    html.P(
                                        "Para fazer os cálculos algumas coisas foram assumidas. Primeiro: As pessoas que "
                                        "constam como óbito foram removidas da análise, pois elas não geram renda mais, "
                                        "e suas dívidas foram divididas igualmente entre todos os membros de sua famílias "
                                        "e da família aliada, caso tenha. Não foi assumido que se uma pessoa possui uma "
                                        "família aliada todas pessoas de sua família também são aliadas dessa outra família, "
                                        "pois somente algumas pessoas de uma família possuia aliados em alguns casos. Segundo: "
                                        "Para calculo de curva ABC (ou análise de Paretto), foi utilizado somente a renda "
                                        "anual de cada familia, que consiste em subtrair a dívida de todos membros de sua "
                                        "família, pela capacidade de pagamento anual total dessa família. Terceiro: Foi "
                                        "somente analisado famílias que possuem rendas acima de zero, pois famílias com "
                                        "renda anual abaixo de zero já são famílias na qual não valem a pena investir.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
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
