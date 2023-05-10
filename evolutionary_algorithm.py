
class MutationStrategy:
    # semplicemente prendo un valore random 
    # all'interno del range della cella
    # e lo assegno come nuovo valore
    RANDOM = 0
    # prendo un valore random da una distribuzione gaussiana
    # e lo aggiungo al valore corrente della cella
    # facendo attenzione ceh non esca dai limiti della cella
    GAUSSIAN = 1

# TODO: implementare altri tipi di crossover
class CrossoverStrategy:
    # prendo la media dei valori delle due celle, 
    # dove moltiplico il valore della seconda cella per un peso (CROSSOVER_WEIGHT),
    # in modo da non fare uscire il valore della prima cella dai limiti
    MEAN = 0

# TODO: implementare altri tipi di selezione
class CrossoverSelectionStrategy:
    # seleziono cella a random
    RANDOM = 0
    # seleziono cella adiacente
    ADJACENT = 1
    # seleziono cella con valore più alto
    BEST = 2



class EA_Config: 
    ### --- parametri generali ---
    ALLOW_MUTATION = True
    ALLOW_CROSSOVER = True

    ### --- parametri di mutation ---
    MUTATION_STRATEGY = MutationStrategy.RANDOM

    ### ---- parametri di crossover ---
    CROSSOVER_STRATEGY = CrossoverStrategy.MEAN
    CROSSOVER_WEIGHT = 0.2

    ### --- parametri di selezione ---
    CROSSOVER_SELECTION_STRATEGY = CrossoverSelectionStrategy.RANDOM
