import csv


def save_as_csv(lod, headers, fname):
    with open(fname + '.csv', 'w') as f:
        fobj = csv.DictWriter(f, fieldnames=headers)
        fobj.writeheader()
        fobj.writerows(lod)
