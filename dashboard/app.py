# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'pages')

import procedimento_resumo, corr_positive, corr_negative

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dashboard/procedimento-resumo":
        return procedimento_resumo.create_layout(app)
    elif pathname == "/dashboard/correntista-positivo":
        return corr_positive.create_layout(app)
    elif pathname == "/dashboard/correntista-negativo":
        return corr_negative.create_layout(app)

    elif pathname == "/dashboard/full-view":
        return (
            procedimento_resumo.create_layout(app),
            corr_positive.create_layout(app),
            corr_negative.create_layout(app),

        )
    else:
        return procedimento_resumo.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
