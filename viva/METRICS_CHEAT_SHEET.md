# Metrics Cheat Sheet

## Basic Terms

- TP: True positive, predicted a class and it was actually that class.
- TN: True negative, correctly did not predict a class.
- FP: False positive, predicted a class incorrectly.
- FN: False negative, failed to predict a class when it was the true class.

## Accuracy

```text
Accuracy = correct predictions / total predictions
```

Simple meaning: overall percentage correct.

## Precision

```text
Precision = TP / (TP + FP)
```

Simple meaning: when the model predicts a class, how often is it correct?

## Recall

```text
Recall = TP / (TP + FN)
```

Simple meaning: out of all actual samples of a class, how many did the model find?

## F1 Score

```text
F1 = 2 x precision x recall / (precision + recall)
```

Simple meaning: one number balancing precision and recall.

## Confusion Matrix

A table where rows are true classes and columns are predicted classes. Diagonal values are correct predictions. Off-diagonal values are mistakes.

## Macro Average

Calculate the metric separately for each class, then average the class scores equally.

Why useful for DeFungi:

- The dataset counts are uneven: H1 has 4,404 images while H6 has 739.
- Macro metrics prevent large classes from dominating the metric.

## Tiny Example

For one class:

- TP = 8
- FP = 2
- FN = 4

Precision:

```text
8 / (8 + 2) = 0.80
```

Recall:

```text
8 / (8 + 4) = 0.67
```

Accuracy alone would not show this difference between false positives and false negatives.
