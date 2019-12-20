import pandas as pd
import pdpipe as pdp
import ETL_func
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups', category=FutureWarning)


def main():
    coor_banco = pd.read_csv('correntistas_banco_bravos (3).csv', encoding="ISO-8859-1", sep=";",
                             usecols= ['name', 'male', 'house', 'Dívida', 'Capacidade de pagamento anual'])
    coor_obito = pd.read_csv('correntistas_obito (2).csv', encoding = "ISO-8859-1", sep=";")

    # Pipeline para um tratamento inicial
    col_apply = ["Capacidade de pagamento anual", "Dívida"]
    pipeline = pdp.DropNa(how='all')  # Drop linha que tem todos valores nan
    pipeline += pdp.ApplyByCols(col_apply, ETL_func.convert_money)  # apply função convert_money nas colunas em col_apply
    pipeline += pdp.ApplyByCols('house', ETL_func.correct_names)
    coor_banco = pipeline(coor_banco)  # aplica pipeline do dataframe

    pipeline2 = pdp.ApplyByCols('Allegiances', ETL_func.allegiances_correction)
    coor_obito = pipeline2(coor_obito)

    # 1 para pessoa morta e 0 para não morta
    for n, ally in zip(coor_obito.Name, coor_obito.Allegiances):
        if coor_banco.name.str.contains(n).sum() > 0:
            coor_banco.loc[coor_banco.name == n, 'Óbito'] = 1
            coor_banco.loc[coor_banco.name == n, 'Allegiances'] = ally

    coor_banco.loc[coor_banco.Óbito.isna(), "Óbito"] = 0
    coor_banco.loc[coor_banco.Allegiances.isna(), "Allegiances"] = "None"
    ETL_func.divida_split(coor_banco)

    treated_data = coor_banco[coor_banco.Óbito == 0].reset_index(drop=True)

    treated_data['patrimônio'] = treated_data['Capacidade de pagamento anual'] - treated_data['Dívida']
    data_grouped = treated_data.groupby(by='house').sum().sort_values(by='patrimônio',
                                                                      ascending=False).drop(columns=['male', 'Óbito'])
    data_grouped_positive = data_grouped[data_grouped.patrimônio > 0]
    data_grouped_positive['patrimônio_percent'] = round(data_grouped_positive['patrimônio']/data_grouped_positive['patrimônio'].sum()*100, 2)
    data_grouped_positive['cumulative_patri_percent'] = data_grouped_positive['patrimônio_percent'].cumsum()
    data_grouped_positive['Class'] = data_grouped_positive['cumulative_patri_percent'].apply(ETL_func.ABC_segmentation)

    data_grouped_negative = data_grouped[data_grouped.patrimônio < 0]

    data_grouped_negative.to_csv("../dashboard/data/patrimônio_negativo.csv")
    data_grouped_positive.to_csv("../dashboard/data/patrimônio_positivo.csv")


if __name__ == "__main__":
    main()
