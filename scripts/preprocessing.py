import pandas as pd
import numpy as np


def list_indexes_to_drop(dataframe, threshold):
    # INTPUT:
    # Dataframe calculado - índice e % de incidência ou variância
    # Threshold - % de indidência mínimo ou variância mínima

    # OUTPUT:
    # Lista de índices dos bits a serem remodidos da Fingerprint

    sorted_df = dataframe.sort_values(by='calculation', ascending=False, ignore_index=True)

    row = 0

    indexes_to_drop = []

    while row < len(sorted_df) and sorted_df.iloc[row, 1] >= threshold:
        row = row + 1

    while row < len(sorted_df):
        indexes_to_drop.append(sorted_df.iloc[row, 0])
        row = row + 1

    return indexes_to_drop


def selection_by_threshold(method, np_array, threshold):
    # INPUT:
    # Método:
    # 'variance' - retirar valores a partir de uma var mínima
    # 'incidence'- retirar valores a partir de uma indidência mínima [0,1]
    # np_array - fingerprints
    # Threshold - % de indidência mínimo ou variância mínima

    # OUTPUT:
    # Clean_array - fingerprint com as colunas de baixa variância ou incidência removida
    # Dropped_indexes - lista de índices (bits) desconsiderados

    indexes = range(0, np_array.shape[1])

    if method == 'variance':
        # Variância de cada bit
        method_calculation = np.var(np_array, axis=0)

    if method == 'incidence':
        # Percentual incidente de um determinado bit
        method_calculation = np.sum(np_array, axis=0)
        method_calculation = method_calculation / np_array.shape[0]

    method_df = pd.DataFrame({'index': indexes, 'calculation': method_calculation})

    indexes_to_drop = list_indexes_to_drop(method_df, threshold)

    clean_array = np.delete(np_array, indexes_to_drop, 1)
    dropped_indexes = indexes_to_drop

    return clean_array, dropped_indexes
