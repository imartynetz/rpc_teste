import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [html.H5("Análise Dataset Banco Bravos e curva ABC")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Procedimento & Resumo",
                href="/dashboard/procedimento-resumo",
                className="tab first",
            ),
            dcc.Link(
                "Correntistas renda anual positiva",
                href="/dashboard/correntista-positivo",
                className="tab",
            ),
            dcc.Link(
                "Correntistas renda anual negativa",
                href="/dashboard/correntista-negativo",
                className="tab",
            ),

        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
