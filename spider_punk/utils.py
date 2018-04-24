"""
    Module, for all utilities required for the project
"""

import csv
import json


def save_as_csv(lod, headers, fname):
    """
    :param lod: list of dictionaries, containing row wise data, key being column,
                value being the relevant data in the for that row
    :param headers: column names
    :param fname: file name of the csv
    """
    with open(fname + '.csv', 'w') as f:
        fobj = csv.DictWriter(f, fieldnames=headers)
        fobj.writeheader()
        fobj.writerows(lod)


def save_as_json(lod, fname, pk=None):
    """
    :param pk: check if key values is to be used from the dict or not, else use auto incrementing numbers
    :param lod: list of dictionaries to be saved as JSON
    :param fname: file name of the JSON
    """
    rdict = dict()
    anum = 1

    for vdict in lod:
        if pk is None:
            rdict[anum] = vdict
            anum += 1
        else:
            rdict[vdict.get(pk)] = vdict

    with open(fname + '.json', 'w') as f:
        json.dump(rdict, f)
