# Rouault et al. (2019) Replication Analyses
Python replication of key analyses from Rouault, Dayan, & Fleming (2019), *Forming global estimates of self-performance from local confidence*, Nature Communications.
[Full write-up](https://ninaedgley.github.io/rouault-exp3-replication/)

The replication focused on Experiment 3's core analyses, originally implemented in MATLAB, but reimplemented in Python. These incude:
- Confidence x difficulty interaction (paired t-tests)
- Logistic regression: confidence predicts task choice beyond accuracy and RT (ΔBIC = 22.4)
- Meta-d' MLE fitting (Maniscalco & Lau, 2012) translated from MATLAB to Python
- Metacognitive efficiency (M-ratio) correlation with global self-performance estimates

The Python MLE M-ratio estimates match the paper's precomputed values to the third decimal place (Easy: 0.858 vs 0.858; Difficult: 0.738 vs 0.740).

## Structure
```
data/
  Exp3.mat
  perf_data_for_jasp.csv
docs/
  figures/
    02_fig5a_confidence_accuracy_difficulty.png
    02_fig5b_logistic_regression.png
    02_fig5c_task_choice_performance.png
    02_fig5ed_metacog_scatter.png
  _config.yml
  index.md
notebooks/
  01_load_data.ipynb
  02_replication.ipynb
  03_metad.ipynb
src/
  utils.py

```

## Data Source

Original data and MATLAB code: https://github.com/marionrouault/RouaultDayanFleming

## Reference
Rouault, M., Dayan, P., & Fleming, S. M. (2019). Forming global estimates of self-performance from local confidence. *Nature Communications*, 10(1), 1141.