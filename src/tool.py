import pandas as pd 

def inspector (df):
    print("######### DEBUT DE L'ANALYSE #########")

    # fonction permetant de donner le nombres de ligne et de colonnes
    print(f"Le df comprend {df.shape[0]} lignes et {df.shape[1]} colonnes ")
    print('\n---------------------------------------------------------------')

    #fonction comptant le nombre de nulls
    count_null = df.isna().sum()
    print(f"le df contient les nuls suivant ")
    print(count_null)
    print('\n---------------------------------------------------------------')

    #fonction donnant le nom et le type de données 
    print(f"les types et noms de colonnes sont les suivants")
    print(f"{df.dtypes}")
    print('\n---------------------------------------------------------------')

    #fonction donnant le nombre d'unique par colonnes
    print("le nombre d'uniques dans les colonnes sont les suivants")
    print(f"{df.nunique()}")
    print('\n---------------------------------------------------------------')

    #if nb_unique == nb_ligne :
    #    print("il y a une potentiel PK ")

    print("\n######### FIN DE L'ANALYSE #########")


