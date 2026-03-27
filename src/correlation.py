"""
Outils d'analyse de corrélations.

Choisir le bon test selon les types de variables :

+------------------+--------------------+------------------+----------------------+
| Type             | Test               | Indicateur       | Visualisation        |
+------------------+--------------------+------------------+----------------------+
| Quali / Quali    | Chi²               | χ², p-value      | Heatmap / Barplot    |
| Quanti / Quanti  | Pearson / Spearman | R², p-value      | Nuage de points      |
| Quanti / Quali   | ANOVA (ou KS)      | η², F, p-value   | Boxplot              |
+------------------+--------------------+------------------+----------------------+

Exemples :
    - Chi²    : Genre ↔ Catégories
    - Pearson : Âge ↔ Montant total
    - ANOVA   : Âge ↔ Catégories

Notes :
    - Pearson   : corrélation linéaire, sensible aux outliers.
    - Spearman  : version robuste basée sur les rangs, à préférer si distribution non normale.
    - KS (Kolmogorov-Smirnov) : alternative non-paramétrique à l'ANOVA.
    - p-value < 0.05 → corrélation statistiquement significative (seuil classique).
"""
import pandas as pd
import scipy as stats 

def correlation_quanti_quanti(df, col1, col2, plot=True, test= True, report=True):
    #veriefier que df est bien un dataframe
    if not isinstance(df, pd.DataFrame):
        print(f"Erreur: l'entrée {df} n'est pas un dataframe")
        return
    # verification que col1 et col2 sont bien des colonnes 
    for col in [col1, col2]:
        if col not in df.columns:
            print(f"Erreur l' entrée '{col}' est introuvable dans le dataframe")
            return
    # verification du types des colonnes 
        if df[col].dtype.kind not in ('i', 'f'): 
            print(f"Erreur : La colonne '{col}' n'est pas numérique ({df[col].dtype}).")
            return
    print('###### Tout est OK ✅#######')


#Step 2 : normalité 
# col1 et col2 normal --> ok test de pearson si KO Spearman
stats, p_shapiro = p_shapiro()

#Step 3 : le test
    # test
    #p-value , R²

#step 4 : plot
    #scatter plot (x,y)

#step 5 : report
    #reporting 