from enum import Enum

import enum_tools.documentation

enum_tools.documentation.INTERACTIVE = True


@enum_tools.documentation.document_enum
class TunisianCityType(int, Enum):
    """
    Enumeration of Tunisian city types.

    This enumeration represents the different types of cities in Tunisia.
    Each city type is assigned a unique integer value, and the list is ordered in ascending order by name.

    """

    AA = 1  # doc: Ariana
    BJ = 2  # doc: Béja
    BA = 3  # doc: Ben Arous
    BZ = 4  # doc: Bizerte
    GB = 5  # doc: Gabès
    GF = 6  # doc: Gafsa
    JB = 7  # doc: Jendouba
    KR = 8  # doc: Kairouan
    KS = 9  # doc: Kasserine
    KL = 10  # doc: Kébili
    LM = 11  # doc: La Manouba
    LK = 12  # doc: Le Kef
    MH = 13  # doc: Mahdia
    MD = 14  # doc: Médenine
    MS = 15  # doc: Monastir
    NB = 16  # doc: Nabeul
    SF = 17  # doc: Sfax
    SB = 18  # doc: Sidi Bouzid
    SI = 19  # doc: Siliana
    SU = 20  # doc: Sousse
    TT = 21  # doc: Tataouine
    TZ = 22  # doc: Tozeur
    TN = 23  # doc: Tunis
    ZG = 24  # doc: Zaghouan

    def __str__(self):
        return self.name
