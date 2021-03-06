from clustering.lib import mean_vector_of_matrix, euclidean_distance_between_vectors
import numpy as np


class Cluster(object):
    """
    Represents a clustering of data points and its corresponding centroid
    """

    def __init__(self, array: np.ndarray):
        self.points = array
        self.centroid = None

    def compute_centroid(self):
        """
        Calculate the centroid of the data
        """
        self.centroid = mean_vector_of_matrix(self.points)

    def get_centroid(self):
        """
        Safety check to ensure that the centroid is computed.

        :return: the centroid
        """
        if self.centroid is None:
            self.compute_centroid()
        return self.centroid

    def euclidean_distance(self, other: np.array) -> float:
        """
        Calculate euclidean distance between the centroids of this cluster and the inserted vector.

        :param other: the vector that should be compared.
                        This could be a data point or a centroid of a different cluster.
        :return: euclidean distance
        """
        assert other.shape == self.get_centroid().shape

        return euclidean_distance_between_vectors(self.get_centroid(), other)
