from chembl_webresource_client.new_client import new_client
import h5py
import pandas as pd


def chembl_to_smiles(chembl_id):
    # Fetch data from website and returns the smiles notation. Input = Chembl Id, Output = Smiles notation
    molecule = new_client.molecule
    return molecule.get(chembl_id)['molecule_structures']['canonical_smiles']


def retrieve_chembl(filepath):
    # Retrieves the chembl ids from the molecules in the h5 file
    f = h5py.File(filepath, 'r')
    return f['chembl_id']


def chembl_list_to_smiles(chembl_list):
    # Input = list of chembl ids output = dictionary {chembl_id : smiles notation}
    my_dict = {}
    i = 0
    with open('log.log', 'w') as file:
        print('Retrieving data on database, please wait')
        for item in chembl_list:
            item_str = str(item)
            chembl_str = item_str[2:len(item_str) - 1]

            try:
                my_dict[chembl_str] = chembl_to_smiles(chembl_str)
            except Exception as e:
                print(e)
                my_dict[chembl_str] = 'data not retrieved'
            i = i + 1
            text = 'Molecule: {} : Smiles: {}, progress {}/{}'.format(item, my_dict[chembl_str], i + 1,
                                                                      len(chembl_list))
            file.write(text + '\n')
            print(text)
    return my_dict


def generate_dict_chembid_smiles(filepath):
    # Input is the filepath of the h5 file, must contain the chembl_id column
    # Creates a dictionary {chembl_id : smiles notation} by web scraping on the chembl database
    chembl_list = retrieve_chembl(filepath)
    print(len(chembl_list), 'items')
    return chembl_list_to_smiles(chembl_list)


def save_as_csv(dataset, dict_chembid_smiles, directory='../data/'):
    csv = {'chembid': [], 'smiles_notation': []}
    for chembid, smiles_notation in dict_chembid_smiles.items():
        csv['chembid'].append(chembid)
        csv['smiles_notation'].append(smiles_notation)
    df_result = pd.DataFrame(csv)
    output_filepath = directory + dataset + '_chemid_smiles.csv'
    df_result.to_csv(output_filepath)


if __name__ == '__main__':
    filepath = '../data/egfr_erbB1.h5'
    chembid_smiles = generate_dict_chembid_smiles(filepath)
    save_as_csv(dataset='egfr_erbB1', dict_chembid_smiles=chembid_smiles)
