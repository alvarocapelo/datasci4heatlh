#Este script recebe o csv com Chembl e Smiles e retorna uma lista com as posições não nulas
#do sparse bit vector da Fingerprint farmacofórica
#Cria um json chebl : lista de não nulos
from rdkit import Chem
import pandas as pd
from rdkit.Chem.Pharm2D import Gobbi_Pharm2D, Generate
import json

def convert_to_fp(mol_smiles):
    molecule = Chem.MolFromSmiles(mol_smiles)
    fp = Generate.Gen2DFingerprint(molecule, Gobbi_Pharm2D.factory)
    if len(fp) != 39972:
        print("FATAL ERROR!")
    return list(fp.GetOnBits()) #lists position of number one
    #return fp #rdkit.DataStructs.cDataStructs.SparseBitVect
    
def from_df_to_json(df):
    # Receives de Dataset and converts the smiles structures to 2D pharmacophore fingerprints
    # Returns Dictionary k = chembl_id, v = list of 1 from Sparse Bit Vect
    # The fp is a Sparse Bit Vect
    my_dict = {}
    my_dict['molecules'] = []
    length = len(df['chembid'])
    i = 1
    with open('error.log', 'w') as file:
        for mol_id, mol_smiles in zip(df['chembid'], df['smiles_notation']):
            key = mol_id
            try:
                values = convert_to_fp(mol_smiles)
                my_dict['molecules'].append({
                    'chembl_id': key,
                    'fingerprint':values
                })
                print('Fingerprint generated for: {}. Progress: {}%'.format(key, str((i/length)*100)))
            except Exception as e:
                file.write(str(e)+'\n')
                print('Fingerprint not generated for: {}. Progress: {}%'.format(key, str((i/length)*100)))
            i = i + 1

    with open('../data/egfr_erbB1_pharmacophore.json', 'w') as outfile:
        json.dump(my_dict, outfile)

    print('Fingerprint json completed')

    return my_dict

if __name__ == '__main__':
    filepath = '../data/egfr_erbB1_smiles.csv'
    df = pd.read_csv(filepath, index_col=0)
    my_dict = from_df_to_json(df)
