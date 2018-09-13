def neighborhood(name):
    map = {
        "CollgCr": 1,
        "Veenker": 2,
        "Crawfor": 3,
        "NoRidge": 4,
        "Mitchel": 5,
        "Somerst": 6,
        "NWAmes": 7,
        "OldTown": 8,
        "BrkSide": 9,
        "Sawyer": 10,

        "NridgHt": 11,
        "NAmes": 12,
        "SawyerW": 13,
        "StoneBr": 14,
        "IDOTRR": 15,
        "MeadowV": 16,
        "Edwards": 17,
        "Timber": 18,
        "Gilbert": 19,
        "NPkVill": 20,

        "xxx": 21,
        "xxx": 22,
        "xxx": 23,
        "xxx": 24,
        "xxx": 25,
        "xxx": 26

    }
    return map.get(name, 0)

def housestyle(name):
    map = {
        "1Story": 1,
        "2Story": 2,
        "1.5Fin": 3,
        "1.5Unf": 4,
        "SFoyer": 5,
        "SLvl": 6
    }
    return map.get(name, 0)

def heating(name):
    map = {
        "Ex": 1,
        "Gd": 2,
        "TA": 3,
    }
    return map.get(name, 0)

def ac(name):
    map = {
        "Y": 1,
        "N": 2
    }
    return map.get(name, 0)