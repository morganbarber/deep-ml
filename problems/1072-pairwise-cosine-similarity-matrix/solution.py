import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X)
    dot = np.dot(X, X.T)

    norms = np.linalg.norm(X, keepdims=True, axis=1)

    prod = np.dot(norms, norms.T)

    return dot / (prod + 1e-9)