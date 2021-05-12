import json
import h5py
import numpy as np
import pandas as pd

def get_morgan_fingerprints(fp_filepath='../data/egfr_erbB1_morgan_2048.npy',
                            labels_filepath='../data/egfr_erbB1_labels.csv'):
    return np.load(fp_filepath), pd.read_csv(labels_filepath, index_col=0)

def get_morgan_fingerprints_from_json(filepath='../data/egfr_erbB1_pharmacophore_and_morgan_2048.json'):
    with open(filepath, 'r') as file:
        data = json.load(file)

    morgan_fp = [item['morgan'] for item in data['molecules']]
    return np.vstack(morgan_fp)

def get_chembl_to_label_map(h5_filepath='../data/egfr_erbB1.h5'):
    data = h5py.File(h5_filepath, "r")
    labels = list(data["label"])
    chembl_ids = [c.decode("utf-8") for c in list(data["chembl_id"])]
    return {chembl: label for label, chembl in zip(labels, chembl_ids)}


def extract_fp_and_labels():
    filepath = '../data/egfr_erbB1_pharmacophore_and_morgan_2048.json'
    with open(filepath, 'r') as file:
        data = json.load(file)

    morgan_fp = [item['morgan'] for item in data['molecules']]
    morgan_fp = np.vstack(morgan_fp)
    chembl_ids = [item['chembl_id'] for item in data['molecules']]

    chembl_to_label = get_chembl_to_label_map()
    labels = [chembl_to_label[chembl] for chembl in chembl_ids]
    n = len(labels)
    df_labels = pd.DataFrame({'labels': labels, 'chembl_ids': chembl_ids,
                              'fingerprint_id': list(range(n))})
    df_labels.to_csv('../data/egfr_erbB1_labels.csv')

    with open('../data/egfr_erbB1_morgan_2048.npy', 'wb') as f:
        np.save(f, morgan_fp)

extract_fp_and_labels()