# Training Curves And Confusion Matrices

## Model A Training Curve

What is supported by the saved history:

- Training loss decreased from 1.2751 to 0.8014.
- Validation loss decreased from 1.1120 to 0.7832.
- Training accuracy increased from 0.5079 to 0.6658.
- Validation accuracy increased from 0.5647 to 0.6854.
- Best validation loss occurred at epoch 20.

Viva-safe explanation:

Model A showed steady learning across the 20 epochs. Both training and validation loss decreased, so the curve supports that the model was still improving by the end of training. We should not strongly claim overfitting from this alone, because validation loss did not show a clear sustained increase.

## Model B Training Curve

What is supported by the saved history:

- Training loss decreased from 1.3164 to 0.8201.
- Validation loss decreased from 1.1209 to 0.8491.
- Training accuracy increased from 0.4995 to 0.6620.
- Validation accuracy increased from 0.5552 to 0.6372.
- Best validation loss occurred at epoch 19.

Viva-safe explanation:

Model B also learned steadily. Its validation loss improved overall but was slightly better at epoch 19 than epoch 20. This suggests validation performance had started to stabilize near the end. We should not call this strong overfitting without more evidence.

## MobileNetV2 Training Curve

What is supported by the saved history:

- Training loss decreased from 1.0245 to 0.5372.
- Validation loss decreased from 0.7687 to 0.6261.
- Training accuracy increased from 0.5946 to 0.7735.
- Validation accuracy increased from 0.6935 to 0.7666.
- Best validation loss occurred at epoch 18.

Viva-safe explanation:

MobileNetV2 improved substantially and stabilized near the final epochs.

## EfficientNetB0 Training Curve

What is supported by the saved history:

- Training loss decreased from 0.9558 to 0.5686.
- Validation loss decreased from 0.8221 to 0.5756.
- Training accuracy increased from 0.6131 to 0.7678.
- Validation accuracy increased from 0.6811 to 0.7835.
- Best validation loss occurred at epoch 20.

Viva-safe explanation:

EfficientNetB0 continued improving through the final epoch and achieved the strongest validation and test performance among the evaluated models.

## Model A Confusion Matrix

Class order: H1, H2, H3, H5, H6.

```text
[[583,  67,   9,   2,   0],
 [194, 122,  16,  13,   5],
 [ 37,   7,  58,  11,  10],
 [  9,  14,   4,  92,   4],
 [  3,   8,   0,   3,  97]]
```

Supported observations:

- H1 has the largest correct count: 583 correct out of 661 test samples.
- H6 is also strong: 97 correct out of 111.
- The largest off-diagonal confusion is H2 predicted as H1: 194 samples.
- Avoid biological explanations unless the dataset source supports them.

## Model B Confusion Matrix

Class order: H1, H2, H3, H5, H6.

```text
[[521, 124,  13,   2,   1],
 [171, 142,  13,  10,  14],
 [ 24,  37,  40,  11,  11],
 [  8,  13,   1,  86,  15],
 [  2,   6,   0,   5,  98]]
```

Supported observations:

- H1 remains the highest correct count: 521 correct out of 661.
- H6 is strong: 98 correct out of 111.
- H3 is weaker: 40 correct out of 123.
- A major confusion is H2 predicted as H1: 171 samples.

## How To Talk About Overfitting

Only say "overfitting" if training improves while validation clearly gets worse for a sustained period. In our custom-model curves, both training and validation losses decreased overall, so it is safer to say performance improved and began to stabilize near the final epochs.
