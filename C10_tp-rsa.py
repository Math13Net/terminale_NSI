# coding: utf-8

##
## TP 1 du chapitre 10 (Le chiffrement RSA)
##


# Tous les calculs sont effectués modulo un entier n contenu dans 
# la variable MODULE_RSA. La clef publique est un entier e contenu
# dans la variable EXPOSANT_PUBLIC et la clef privée associée est 
# un entier d contenu dans la variable EXPOSANT_PRIVE.

MODULE_RSA = 21404482288767167215320101672577097978662557461928839522662399518240548406820333206011111465481615306696307196861908775916510886003838613099441333573727126099170746079086423920276749988193888828284625531266257293298285607049048989281323967926856422713938382882189870380716740198804756021400728712023136660241526957243213646234389202636591619173144149409148054708765930675411087667523111533458036474724809290207921748722353977255848636815602935192253193052089870367947610854991660982024653929215907957840775081240305444745939375439605886334837505721640050486730430804642854344118323259079641240830673554091227312814943

EXPOSANT_PUBLIC = 65537

EXPOSANT_PRIVE = 14009244599148250156918083542785327993297705720005121419733600331650977056657329028466982242097874589398834260069803546609744387815259372114796779869561489645510627314590736036686923630828214098912686383846298126840359839918853584177382398954095845032449959493853125716930342464371747330240365860102238794946175219782156076561355135223879515024154339100828344894350707493878524433221648462813944590620839053539611355536956549551569052871850508588789491336361633606521012904737513194972339699967689803215787566576178138158224046841135740232379707583140158111345351583652576786441063482402129491372130532218257098870433

# Le chiffrement d'un entier m consiste à élever m à la puissance 
# EXPOSANT_PUBLIC modulo l'entier MODULE_RSA. En Python, cette opération 
# est effectuée par la fonction pow.

def chiffrement(m):
    return(pow(...)) # À COMPLÉTER
    
# Le déchiffrement d'un entier c consiste à élever c à la puissance 
# EXPOSANT_PRIVE modulo l'entier MODULE_RSA. En Python, cette opération 
# est effectuée par la fonction pow.

def dechiffrement(c):
    return(pow(...)) # À COMPLÉTER
    
# On peut utiliser la fonction suivante pour vérifier que 
# dechiffrement(chiffrement(m)) = m pour un entier m plus petit 
# que MODULE_RSA.

def verification(m):
    print(m)
    c = chiffrement(m)
    print(c)
    m2 = dechiffrement(c)
    print(m2)
    return(m==m2)

print(verification(1234))

# Pour chiffrer un message textuel, on utilise les deux fonctions 
# chaine_vers_entier et entier_vers_chaine, qu'il n'est pas nécessaire
# de comprendre ou de modifier.

def chaine_vers_entier(s):
    # Transformons d'abord la chaîne de caractères (de type str) en
    # une suite d'octets (de type bytes)
    octets = s.encode()

    # Convertissons ensuite cette suite d'octets en un grand entier
    i = int.from_bytes(octets, byteorder="big")

    return i

def entier_vers_chaine(i):
    # Déterminons le nombre d'octets nécessaire pour transformer
    # l'entier en chaîne de caractères. n_octets est la partie entière
    # supérieure de n_bits / 8
    n_bits = int.bit_length(i)
    n_octets = (n_bits + 7) // 8

    # Convertissons l'entier en bytes
    octets = int.to_bytes(i, n_octets, byteorder="big")

    # Décodons les octets pour produire une chaîne de caractères
    s = octets.decode()

    return s

# On souhaite chiffrer le message suivant.

MESSAGE_A_CHIFFRER = "QUEL JOUR DE LA SEMAINE DEVONS-NOUS ATTAQUER ?"
m = # À COMPLÉTER
print(m)
c = chiffrement(m)
print(c)
m2 = dechiffrement(c)
print(m2)
message2 = entier_vers_chaine(m2)
print(message2)

REPONSE_CHIFFREE = 11657018119508503881530646661602015044477063868869390712374052144251703839491225203567031826495911791709792439271647623487635467694673548583482116921066369478540085802571148274118151315208377266612755906856640744266912758947793102346114514302138507735443751126168040428197408797634825794804867200759070724394968844582358199426423751467242640911177458220138615283409554155116799471376594705076219061136627211419466936826936964333562765506055172224430960217464864171684666597535917691018991223985611330402834701837966182351322336031003778825262150704880537949527074190138528671156806845495333078554857981246787039849020

JOURS_DE_LA_SEMAINE = [
    "LUNDI",
    "MARDI",
    "MERCREDI",
    "JEUDI",
    "VENDREDI",
    "SAMEDI",
    "DIMANCHE"
]

# On chiffre les sept jours de la semaine.
for jour in JOURS_DE_LA_SEMAINE:
    m = ... # À COMPLÉTER
    c = chiffrement(m)
    if c == ...: # À COMPLÉTER
        print(jour)












