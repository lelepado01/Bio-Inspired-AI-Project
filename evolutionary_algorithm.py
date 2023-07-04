
class MutationStrategy:
    """
    Selezione di strategie di mutazione, le opzioni sono:
    - RANDOM: prende un valore random all'interno del range della cella
    e lo assegna come nuovo valore
    - GAUSSIAN: prende un valore random da una distribuzione gaussiana
    e lo aggiunge al valore corrente della cella
    """

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
    """
    Selezione di strategie di crossover, le opzioni sono:
    - MEAN: prende la media dei valori delle due celle e la assegna alla prima cella
    """

    MEAN = 0
    """
    Prende la media dei valori delle due celle, 
    moltiplica il valore della seconda cella per un peso (CROSSOVER_WEIGHT),
    in modo da non fare uscire il valore della prima cella dai limiti
    """

class CrossoverSelectionStrategy:
    """
    Selezione di strategie di selezione per il crossover, le opzioni sono:
    - RANDOM: seleziona due celle random
    - ADJACENT: seleziona due celle adiacenti
    - BEST: seleziona due celle con valore più alto
    - GAUSSIAN_BEST: seleziona due celle con probabilità basata sul valore fitness
    """
    
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
    """
    Selezione di criteri di stop, le opzioni sono:
    - GENERATIONS: fermo l'algoritmo dopo un numero di generazioni
    - GENERATIONS_WITHOUT_IMPROVEMENT: fermo l'algoritmo dopo un numero di generazioni senza miglioramenti
    (o dopo un numero di generazioni arbitrario)
    """

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
    Formazione iniziale degli agenti sulla mappa, le opzioni sono:
    - RANDOM: posiziona gli agenti in posizioni random
    - DEFAULT: posiziona gli agenti in posizioni di default (a righe)
    - SQUARE: posiziona gli agenti in una griglia quadrata
    """

    RANDOM = 0
    DEFAULT = 1
    SQUARE = 2


class EA_Config: 
    ### --- parametri generali ---
    DEBUG = False
    ALLOW_MUTATION = True
    ALLOW_CROSSOVER = True
    USE_ADVERSARIAL_GRID = True
    """
     - Se *True* utilizza due griglie, una per ogni agente a comando delle formazioni
     - Se *False* utilizza una sola griglia, con i due agenti che usano le stesse formazioni
    (la stessa combinazione di melee e ranged agents)
    """

    ### --- parametri di mutation ---
    MUTATION_STRATEGY = MutationStrategy.GAUSSIAN
    MUTATION_INCENTIVE = 1 
    """
    Valore che viene aggiunto al valore della cella dopo la mutazione 

    Allarga il range di mutazione, per renderla più probabile, visto quanto è lento il training
    """

    ### ---- parametri di crossover ---
    CROSSOVER_STRATEGY = CrossoverStrategy.MEAN
    CROSSOVER_WEIGHT = 0.2

    ### --- parametri di selezione ---
    CROSSOVER_SELECTION_STRATEGY = CrossoverSelectionStrategy.GAUSSIAN_BEST

    ### --- parametri di stopping criteria ---
    STOPPING_CRITERIA = StoppingCriteria.GENERATIONS
    MAX_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 4
    CURRENT_NUMBER_OF_EPOCHS_WITHOUT_IMPROVEMENT = 0

    ### --- parametri di battaglia ---
    INITIAL_FORMATION_TYPE = FormationType.RANDOM

    ### --- parametri di simulazione ---
    MAX_NUMBER_OF_EPISODES = 1 
    """
    Numero di episodi per ogni generazione
    
    Non ha molto senso fare tanti episodi, visto che è come aggiungere epoche ma MAP elites non puù interagire 
    Il senso di questo parametro è se ci serve una simulation più stabile, quindi viene fatta un'average su più episodi
    """
    MAX_NUMBER_OF_EPOCHS = 500
    
    TOTAL_NUMBER_OF_AGENTS = 100
    # AGENT_CLASSES = 2
    CELLS_IN_GRID = 20