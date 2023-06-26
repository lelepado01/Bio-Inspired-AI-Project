
class MutationStrategy:
    RANDOM = 0
    """
    Semplicemente prende un valore random 
    all'interno del range della cella
    e lo assegna come nuovo valore
    """
    GAUSSIAN = 1
    """
    Prende un valore random da una distribuzione gaussiana
    e lo aggiunge al valore corrente della cella
    facendo attenzione che non esca dai limiti della cella
    """

class CrossoverStrategy:
    MEAN = 0
    """
    Prende la media dei valori delle due celle, 
    moltiplica il valore della seconda cella per un peso (CROSSOVER_WEIGHT),
    in modo da non fare uscire il valore della prima cella dai limiti
    """

class CrossoverSelectionStrategy:
    
    RANDOM = 0
    """
    Seleziona cella a random
    """

    ADJACENT = 1
    """
    Seleziona cella adiacente
    """

    BEST = 2
    """
    Seleziona sempre cella con valore più alto
    """
    
    GAUSSIAN_BEST = 3
    """
    Seleziona cella con probabilità basata sul valore fitness
    """

class StoppingCriteria:
    GENERATIONS = 0
    """
    Fermo l'algoritmo dopo un numero di generazioni
    """
    
    GENERATIONS_WITHOUT_IMPROVEMENT = 1
    """
    Fermo l'algoritmo dopo un numero di generazioni senza miglioramenti
    (o dopo un numero di generazioni arbitrario)
    """

class FormationType:
    """
    Formazione iniziale degli agenti sulla mappa
    """
    RANDOM = 0
    DEFAULT = 1
    SQUARE = 2


class EA_Config: 
    ### --- parametri generali ---
    DEBUG = False
    NO_DISPLAY = True
    ALLOW_MUTATION = True
    ALLOW_CROSSOVER = True
    USE_ADVERSARIAL_GRID = True

    ### --- parametri di mutation ---
    MUTATION_STRATEGY = MutationStrategy.RANDOM

    ### ---- parametri di crossover ---
    CROSSOVER_STRATEGY = CrossoverStrategy.MEAN
    CROSSOVER_WEIGHT = 0.2

    ### --- parametri di selezione ---
    CROSSOVER_SELECTION_STRATEGY = CrossoverSelectionStrategy.RANDOM

    ### --- parametri di stopping criteria ---
    STOPPING_CRITERIA = StoppingCriteria.GENERATIONS_WITHOUT_IMPROVEMENT
    MAX_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 4
    CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 0

    ### --- parametri di simulazione ---
    INITIAL_FORMATION_TYPE = FormationType.DEFAULT

    ### --- parametri di simulazione ---
    MAX_NUMBER_OF_EPISODES = 1
    MAX_NUMBER_OF_EPOCHS = 10
    
    TOTAL_NUMBER_OF_AGENTS = 100
    AGENT_CLASSES = 2
    CELLS_IN_GRID = 5