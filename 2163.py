import sys
# Augmenter la limite de récursion pour les cas potentiellement profonds
sys.setrecursionlimit(2000)

def solve():
    # Lecture rapide de N et K
    try:
        # La ligne d'entrée unique contient N et K
        # Utiliser input() ou sys.stdin.readline().split()
        line = sys.stdin.readline()
        if not line:
            return
        N, K = map(int, line.split())
    except EOFError:
        return
    except Exception:
        return

    # Implémentation du Fenwick Tree (Binary Indexed Tree)
    # L'arbre stocke 1 pour chaque enfant initialement présent.
    # L'arbre est 1-indexé.
    tree = [0] * (N + 1)
    
    def update(idx, delta):
        # idx doit être >= 1
        while idx <= N:
            tree[idx] += delta
            idx += idx & (-idx) # Aller au prochain indice significatif
            
    def query(idx):
        # Somme de préfixe jusqu'à l'indice idx
        s = 0
        while idx > 0:
            s += tree[idx]
            idx -= idx & (-idx) # Aller à l'indice parent
        return s

    # Initialisation : tous les enfants sont présents
    for i in range(1, N + 1):
        update(i, 1)

    # Fonction pour trouver l'indice de l'enfant restant en position 'k_th'
    # (1-indexé)
    def find_kth(k_th):
        # Recherche binaire pour trouver le plus petit index 'i' tel que
        # le nombre d'enfants restants dans [1, i] est >= k_th.
        low, high = 1, N
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if query(mid) >= k_th:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result

    # Simulation du jeu
    results = []
    current_position = 0 # 0-indexé parmi les *enfants restants*
    remaining_children = N

    for _ in range(N):
        # 1. Calculer la position (0-indexée) de l'enfant à retirer
        # Le nombre d'enfants à sauter est K. Le nombre d'enfants restants est (remaining_children).
        # On commence à compter à partir de la 'current_position'.
        # La nouvelle position est : (position_de_départ + K) % remaining_children
        
        # current_position est la position *après* le dernier enfant retiré.
        # Si c'était le premier tour, on commence au début (position 0).
        # La position de l'enfant à retirer est l'enfant qui est (K+1)-ième depuis le début du compte.
        # 
        # La nouvelle position est calculée par rapport à l'ensemble des enfants restants (0-indexé)
        # La position de l'enfant à retirer (dans l'ensemble des enfants restants)
        # La position est 0-indexée, donc si remaining_children est 5 et K=2, 
        # on veut retirer l'enfant à l'index (0+2)%5=2 si on commence à 0.
        # Mais dans le problème de Josephus, on saute K personnes, on retire la (K+1)-ième.
        # Si on commence à current_position, l'enfant à retirer est à l'index:
        # (current_position + K) % remaining_children
        
        # Si K est grand, le modulo réduit le nombre de sauts
        index_to_remove = (current_position + K) % remaining_children
        
        # 2. Trouver le numéro (1-indexé) du index_to_remove-ième enfant (qui est 0-indexé).
        # find_kth est 1-indexé.
        # L'index 0 (0-indexé) correspond au 1er enfant restant (1-indexé).
        child_number_1_indexed = find_kth(index_to_remove + 1)
        
        # 3. Retirer l'enfant
        update(child_number_1_indexed, -1)
        results.append(str(child_number_1_indexed))
        remaining_children -= 1
        
        # 4. Mettre à jour la position de départ pour la prochaine itération
        if remaining_children > 0:
            # Après la suppression, la prochaine position de départ est la position
            # de l'enfant qui était immédiatement après l'enfant retiré.
            # L'index index_to_remove (0-indexé) vient d'être retiré.
            # Le prochain départ est à cet index.
            current_position = index_to_remove % remaining_children
        else:
            break

    # Affichage du résultat
    sys.stdout.write(" ".join(results) + "\n")

# Lancement de la fonction
solve()