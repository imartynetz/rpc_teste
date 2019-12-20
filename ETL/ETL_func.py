import re
import pandas as pd


# Converter colunas de valores que estão em string para float
def convert_money(value):
    """

    :param value: Valor específico de cada linha do dataframe
    :return: Seu valor somente, removido qualquer caracter especial (Ex: R$)
    """
    value = value.split()[-1]
    value = re.sub("[,.]", "", value)
    return float(value)


def correct_names(value):
    """

    :param value: Valor específico de cada linha do dataframe
    :return: Nomes corrigidos e aplicados title
    """
    if pd.isnull(value):
        return "None"
    elif value == 'House Starrkk':
        return "House Stark"
    elif value == 'House Lannnister':
        return 'House Lannister'
    else:
        return value.title()


def allegiances_correction(value):
    """

    :param value: Valor específico de cada linha do dataframe
    :return: Nomes que deviam ter House na frente corrigidos
    """
    if value in ["Wildling", "None"]:
        return value
    elif len(value.split())>1:
        return value
    else:
        return f"House {value}"


def divida_split(df):
    """
    Existem algumas pessoas no dataset principal que tb estão na lista de óbito, essas pessoas serão removidas do
    dataset (pois pessoa morta não contribui em renda), e sua dívida será igualmente distribuida entre todas pessoas
    da sua casa e aliança (se ouver alguma).
    :param df: DataFrame

    """

    for n in df.loc[df.Óbito == 1, 'name']:
        house = df.loc[df.name == n, 'house'].values[0]
        ally = df.loc[df.name == n, 'Allegiances'].values[0]
        divida = df.loc[df.name == n, 'Dívida'].values[0]

        # primeiramente checar se tem casa ou aliança
        if (house == "None") & (ally == "None"):
            pass
        # dívida distribuida igualmente em todas pessoas vivas dos aliados e casa

        # caso pessoa não tenha casa mas aliado
        elif house == "None":
            total = len(df[(df.house == ally) & (df.Óbito == 0)])
            d = divida / total
            df.loc[(df.house == ally) & (df.Óbito == 0), 'Dívida'] += d

        # caso pessoa não tenha aliado mas tenha casa
        elif ally == "None":
            total = len(df[(df.house == house) & (df.Óbito == 0)])
            d = divida / total
            df.loc[(df.house == house) & (df.Óbito == 0), 'Dívida'] += d

        # caso pessoa tenha ambos
        else:
            total = len(df[(df.house == house) & (df.house == ally) & (df.Óbito == 0)])
            d = divida / total
            df.loc[(df.house == house) & (df.house == ally) & (df.Óbito == 0), 'Dívida'] += d


def ABC_segmentation(perc):
    """
    Cria as 3 classes A, B, and C baseado
    na quantidade :
    - A: >= 50%;
    - B: >= 20% e < 50%;
    - C: <20%;

    :param perc: Valores de percentual acumulado
    :return: Classe que pertence
    """
    if perc > 0 and perc < 50:
        return 'A'
    elif perc >= 50 and perc < 80:
        return 'B'
    elif perc >= 80:
        return 'C'