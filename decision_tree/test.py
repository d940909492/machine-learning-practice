import csv
from collections import Counter
import math
import pydot

class Node:
    def __init__(self, feature=None, value=None, outcome=None, left=None, right=None):
        self.feature = feature
        self.value = value
        self.outcome = outcome
        self.left = left
        self.right = right

def load_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

def calculate_entropy(data):
    label_column = [row[-1] for row in data]
    label_counts = Counter(label_column)
    entropy = 0
    total_instances = len(label_column)
    for label, count in label_counts.items():
        probability = count / total_instances
        entropy -= probability * math.log2(probability)
    return entropy

def split_data(data, feature_idx, value):
    left_split = []
    right_split = []
    for row in data:
        if row[feature_idx] == value:
            left_split.append(row)
        else:
            right_split.append(row)
    return left_split, right_split

def find_best_split(data):
    best_entropy = float('inf')
    best_split = None

    for feature_idx in range(len(data[0]) - 1):
        values = set(row[feature_idx] for row in data)
        for value in values:
            left_split, right_split = split_data(data, feature_idx, value)
            if len(left_split) == 0 or len(right_split) == 0:
                continue

            left_entropy = calculate_entropy(left_split)
            right_entropy = calculate_entropy(right_split)
            avg_entropy = (len(left_split) / len(data)) * left_entropy + (len(right_split) / len(data)) * right_entropy

            if avg_entropy < best_entropy:
                best_entropy = avg_entropy
                best_split = (feature_idx, value, left_split, right_split)

    return best_split

def build_tree(data):
    label_column = [row[-1] for row in data]

    if len(set(label_column)) == 1:
        return Node(outcome=label_column[0])

    best_split = find_best_split(data)
    if best_split is None:
        label_counts = Counter(label_column)
        return Node(outcome=label_counts.most_common(1)[0][0])

    feature_idx, value, left_split, right_split = best_split
    left_subtree = build_tree(left_split)
    right_subtree = build_tree(right_split)

    return Node(feature=feature_idx, value=value, left=left_subtree, right=right_subtree)

def visualize_tree(node, graph):
    if node.outcome:
        label = node.outcome
    else:
        label = f"X[{node.feature}] = {node.value}"
        
    graph.add_node(pydot.Node(id(node), label=label))
    
    if node.left:
        visualize_tree(node.left, graph)
        graph.add_edge(pydot.Edge(id(node), id(node.left), label="True"))
    
    if node.right:
        visualize_tree(node.right, graph)
        graph.add_edge(pydot.Edge(id(node), id(node.right), label="False"))

data = load_data('./decision_tree/bank1.csv')
tree = build_tree(data)

graph = pydot.Dot(graph_type='graph')
visualize_tree(tree, graph)
graph.write_png('decision_tree/decision_tree.png')
