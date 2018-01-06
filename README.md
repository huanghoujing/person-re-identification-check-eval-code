I create this simple project to check if different versions of evaluation codes generate identical results, for person re-identification. So it's just a test case for evaluation codes.

Here I compare the results by [Tong Xiao](https://github.com/Cysu/open-reid) and [Zhun Zhong](https://github.com/zhunzhong07/person-re-ranking).

# Files

## ./data

It contains an example case for computing CMC and mAP scores, where 100 query images and 5332 gallery images are involved. Their identities, cameras and query-gallery distance matrix are provided.

## ./python_version

- `ranking.py`, copied from open-reid, [link](https://github.com/Cysu/open-reid/blob/master/reid/evaluation_metrics/ranking.py)
- `main.py`, computing CMC and mAP

## ./matlab_version

- `evaluation.m`, copied from person-re-ranking, [link](https://github.com/zhunzhong07/person-re-ranking/blob/master/evaluation/utils/evaluation.m)
- `compute_AP.m`, copied from person-re-ranking, [link](https://github.com/zhunzhong07/person-re-ranking/blob/master/evaluation/utils/compute_AP.m). This is also the same as provided by Market1501, [link](http://www.liangzheng.org/Project/project_reid.html).
- `main.m`, computing CMC and mAP

# Usage

To run the python version, `numpy` and `scikit-learn` is required.

```bash
cd python_version
python main.py
```

To run the matlab version, change working directory to `matlab_version` in Matlab and run `main.m`.

You can compare results of two versions.

# Note

The CMC scores by two versions are identical.

As for mAP, the python version is implemented using `sklearn.metrics.average_precision_score`. This function has changed its behavior [since version 0.19](http://scikit-learn.org/stable/whats_new.html#version-0-19). My installed version (0.18.1) generates mAP identical to the matlab version, i.e. `64.03%`, while version 0.19.1 generates `66.52%`. Since the [Market1501 paper](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Scalable_Person_Re-Identification_ICCV_2015_paper.pdf) introduces mAP into person re-identification, I stick to the matlab version of mAP.

You can check your installed version of scikit-learn by `pip freeze | grep scikit-learn`. To install `scikit-learn` with version `0.18.1`, try this:

```bash
pip uninstall scikit-learn
pip install scikit-learn==0.18.1
```
