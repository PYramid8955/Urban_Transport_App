import heapq
import networkx as nx

class AStarTransport:
    def __init__(self, graph, heuristic_func=None):
        
        # Dacă graful e NetworkX, îl convertim în dict de dict
        if isinstance(graph, (nx.Graph, nx.DiGraph)):
            self.graph = {n: {nbr: graph[n][nbr]['weight'] for nbr in graph.neighbors(n)} for n in graph.nodes}
        else:
            self.graph = graph

        # Heuristica (estimarea distanței până la destinație)
        self.heuristic_func = heuristic_func if heuristic_func else (lambda n, end: 0)

    def find_path(self, start_node, end_node, traffic_weights=None, max_transfers=None):
    
        open_set = []
        heapq.heappush(open_set, (0, start_node, [start_node], 0))  
        g_scores = {start_node: 0}
        transfers_dict = {start_node: 0}

        while open_set:
            f_score, current, path, transfers = heapq.heappop(open_set)

            if current == end_node:
                return {
                    'path': path,
                    'total_time': g_scores[current],
                    'num_transfers': transfers
                }

            for neighbor, base_cost in self.graph.get(current, {}).items():
                # Ajustăm costul cu trafic dacă e definit
                traffic_cost = traffic_weights.get((current, neighbor), 0) if traffic_weights else 0
                tentative_g = g_scores[current] + base_cost + traffic_cost

                # Penalizare schimburi
                new_transfers = transfers
                if len(path) > 1 and path[-2] != current:
                    new_transfers += 1
                    tentative_g += 5  # penalizare 5 min/schimb

                # Respectăm limita de schimburi, dacă e definită
                if max_transfers is not None and new_transfers > max_transfers:
                    continue

                # Dacă e mai bun sau inca nu a fost vizitat
                if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g
                    transfers_dict[neighbor] = new_transfers
                    f_score_neighbor = tentative_g + self.heuristic_func(neighbor, end_node)
                    heapq.heappush(open_set, (f_score_neighbor, neighbor, path + [neighbor], new_transfers))

        # Dacă nu există cale
        return {'path': [], 'total_time': float('inf'), 'num_transfers': 0}
