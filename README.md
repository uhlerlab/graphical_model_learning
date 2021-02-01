[![Build Status](https://travis-ci.com/uhlerlab/graphical_model_learning.svg?branch=main)](https://travis-ci.com/uhlerlab/graphical_model_learning)
[![codecov](https://codecov.io/gh/uhlerlab/graphical_model_learning/branch/main/graph/badge.svg?token=ZGC1RZUFOH)](https://codecov.io/gh/uhlerlab/graphical_model_learning)

`graphical_model_learning` is a Python package for learning the structure (and parameters) of graphical models, including
directed acyclic graphs (DAGs), (maximal) ancestral graphs (MAGs), and undirected graphs. This includes
classical structure learning algorithms, Bayesian methods, and active learning methods.

Structure learning algorithms include:
* PC algorithm
* Greedy Sparsest Permutation (GSP) algorithm
* Interventional and Unknown-Target Interventional GSP (IGSP and UT-IGSP)

We plan to include:
* Greedy Equivalence Search (GES) algorithm
* Minimal IMAP MCMC

`graphical_model_learning` is a part of the [causaldag](https://github.com/uhlerlab/causaldag) ecosystem of packages.

### Install
Install the latest version of `graphical_model_learning`:
```
$ pip3 install graphical_model_learning
```

### Documentation
Documentation is available at https://graphical_model_learning.readthedocs.io/en/latest/


### Simple Example

```
>>> from graphical_model_learning import pcalg
>>> from graphical_models.rand import directed_erdos, rand_weights
>>> from conditional_independence import MemoizedCI_Tester
>>> from conditional_independence import partial_correlation_suffstat, partial_correlation_test
>>> import numpy as np
>>> np.random.seed(1221)
>>> nnodes = 10
>>> d = directed_erdos(nnodes, .2)
>>> g = rand_weights(d)
>>> samples = g.sample(300)
>>> suffstat = partial_correlation_suffstat(samples)
>>> ci_tester = MemoizedCI_Tester(partial_correlation_test, suffstat)
>>> estimated_graph = pcalg(set(range(nnodes)), ci_tester)
>>> d.shd_skeleton(estimated_graph)
1
```

### License

Released under the 3-Clause BSD license (see LICENSE.txt):
```
Copyright (C) 2021
Chandler Squires <csquires@mit.edu>
```
