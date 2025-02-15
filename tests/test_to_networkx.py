import numpy as np


def test_to_networkx():
    import pyclesperanto_prototype as cle
    labels = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))
    # extract centroid positions
    centroids = cle.centroids_of_labels(labels)

    # determine a distance matrix
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)

    # threshold the distance matrix
    adjacency_matrix = cle.generate_proximal_neighbors_matrix(distance_matrix, max_distance=50)

    nx_graph = cle.to_networkx(adjacency_matrix, centroids)
    assert len(nx_graph.nodes) == 3


def test_to_networkx_without_centroids():
    import pyclesperanto_prototype as cle
    labels = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))
    # extract centroid positions
    centroids = cle.centroids_of_labels(labels)

    # determine a distance matrix
    distance_matrix = cle.generate_distance_matrix(centroids, centroids)

    # threshold the distance matrix
    adjacency_matrix = cle.generate_proximal_neighbors_matrix(distance_matrix, max_distance=50)

    nx_graph = cle.to_networkx(adjacency_matrix, centroids)
    assert len(nx_graph.nodes) == 3


def test_proximal_labels_to_networkx():
    import pyclesperanto_prototype as cle
    labels = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))

    nx_graph = cle.proximal_labels_to_networkx(labels, maximum_distance=50)
    assert len(nx_graph.nodes) == 3


def test_n_nearest_labels_to_networkx():
    import pyclesperanto_prototype as cle
    labels = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))

    nx_graph = cle.n_nearest_labels_to_networkx(labels, n=1)
    assert len(nx_graph.nodes) == 3


def test_touching_labels_to_networkx():
    import pyclesperanto_prototype as cle
    labels = cle.push(np.asarray([
        [0, 1],
        [2, 3]
    ]))

    nx_graph = cle.touching_labels_to_networkx(labels)
    assert len(nx_graph.nodes) == 3


