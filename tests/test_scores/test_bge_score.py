from unittest import TestCase
import sys
import unittest
import numpy as np
import subprocess
from graphical_model_learning.scores import local_gaussian_bge_score, MemoizedDecomposableScore
from conditional_independence import partial_correlation_suffstat
from graphical_models import DAG
# import ipdb


class TestBGEScore(TestCase):
    def test_1(self):
        samples = np.load("tests/data/bge_data/samples.npy")
        dag_amat = np.load("tests/data/bge_data/dag_amat.npy")
        dag = DAG.from_amat(dag_amat)
        r_score = np.load("tests/data/bge_data/r_bge.npy")[0]
        suffstat = partial_correlation_suffstat(samples, invert=False)
        scorer = MemoizedDecomposableScore(local_gaussian_bge_score, suffstat)
        score = scorer.get_score(dag)
        print(" R:", r_score)
        print("us:", score)
        self.assertTrue(np.isclose(r_score, score))


if __name__ == '__main__':
    unittest.main()
