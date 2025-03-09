import pickle
from graph import HomiePointsGraph

def save_graph(graph, filename='homie_points.pkl'):
    """Save the graph to a Pickle file."""
    with open(filename, 'wb') as f:
        pickle.dump(graph, f)

def load_graph(filename='homie_points.pkl'):
    """Load the graph from a Pickle file."""
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, return a new graph
        return HomiePointsGraph()