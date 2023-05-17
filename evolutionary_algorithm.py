
class MutationStrategy:
    # semplicemente prendo un valore random 
    # all'interno del range della cella
    # e lo assegno come nuovo valore
    RANDOM = 0
    # prendo un valore random da una distribuzione gaussiana
    # e lo aggiungo al valore corrente della cella
    # facendo attenzione che non esca dai limiti della cella
    GAUSSIAN = 1

# TODO: implementare altri tipi di crossover
class CrossoverStrategy:
    # prendo la media dei valori delle due celle, 
    # dove moltiplico il valore della seconda cella per un peso (CROSSOVER_WEIGHT),
    # in modo da non fare uscire il valore della prima cella dai limiti
    MEAN = 0

class CrossoverSelectionStrategy:
    # seleziono cella a random
    RANDOM = 0
    # seleziono cella adiacente
    ADJACENT = 1
    # seleziono sempre cella con valore più alto
    BEST = 2
    # seleziono cella con probabilità basata sul valore fitness
    GAUSSIAN_BEST = 3

class StoppingCriteria:
    # fermo l'algoritmo dopo un numero di generazioni
    GENERATIONS = 0
    # fermo l'algoritmo dopo un numero di generazioni senza miglioramenti
    # (o dopo un numero di generazioni arbitrario)
    GENERATIONS_WITHOUT_IMPROVEMENT = 1

# formazione iniziale degli agenti sulla mappa
class FormationType:
    RANDOM = 0
    DEFAULT = 1
    SQUARE = 2


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
    CROSSOVER_SELECTION_STRATEGY = CrossoverSelectionStrategy.BEST

    ### --- parametri di stopping criteria ---
    STOPPING_CRITERIA = StoppingCriteria.GENERATIONS_WITHOUT_IMPROVEMENT
    MAX_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 5
    CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 0

    ### --- parametri di simulazione ---
    INITIAL_FORMATION_TYPE = FormationType.RANDOM

    ### --- parametri di simulazione ---
    MAX_NUMBER_OF_EPISODES = 1
    MAX_NUMBER_OF_EPOCHS = 20
    
    TOTAL_NUMBER_OF_AGENTS = 100
    AGENT_CLASSES = 2
    CELLS_IN_GRID = 5