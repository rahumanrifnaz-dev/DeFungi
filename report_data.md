# EN3150 Assignment 03 Report Data

This file is the canonical report source for the completed experiments. Values come from the saved files in `results/metrics/`, `results/figures/`, and `results/confusion_matrices/`.

## 1. Dataset Information

- Dataset: DeFungi, UCI Machine Learning Repository.
- Task: five-class image classification for direct mycological examination images.
- Usable images after verification: 9,114.
- Image format and source resolution: RGB JPEG images, 500 x 500 pixels.
- Unreadable images found during verification: 0.
- Classes and counts:

| Class | Images |
|---|---:|
| H1 | 4,404 |
| H2 | 2,334 |
| H3 | 819 |
| H5 | 818 |
| H6 | 739 |
| Total | 9,114 |

## 2. Preprocessing

- Custom CNN input size: 64 x 64 x 3.
- Custom CNN normalization: pixel values scaled to [0, 1].
- Pretrained input size: 224 x 224 x 3.
- Pretrained preprocessing: model-specific Keras preprocessing functions for MobileNetV2 and EfficientNetB0.
- Label representation: sparse integer labels with sparse categorical crossentropy.
- Reproducibility seed: 42.

## 3. Dataset Split

The verified split is stratified with a 70/15/15 target. Integer rounding gives 6,379 training images, 1,367 validation images, and 1,368 test images. No duplicate paths occur across splits.

| Split | H1 | H2 | H3 | H5 | H6 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Train | 3,082 | 1,634 | 573 | 573 | 517 | 6,379 |
| Validation | 661 | 350 | 123 | 122 | 111 | 1,367 |
| Test | 661 | 350 | 123 | 123 | 111 | 1,368 |

## 4. Model A Architecture

| Layer | Output Shape | Kernel | Filters/Units | Activation | Trainable Parameters |
|---|---|---|---:|---|---:|
| Input | 64 x 64 x 3 | - | - | - | 0 |
| Conv2D | 64 x 64 x 32 | 3 x 3 | 32 | ReLU | 896 |
| MaxPool2D | 32 x 32 x 32 | 2 x 2 | - | - | 0 |
| Conv2D | 32 x 32 x 64 | 3 x 3 | 64 | ReLU | 18,496 |
| MaxPool2D | 16 x 16 x 64 | 2 x 2 | - | - | 0 |
| Conv2D | 16 x 16 x 128 | 3 x 3 | 128 | ReLU | 73,856 |
| MaxPool2D | 8 x 8 x 128 | 2 x 2 | - | - | 0 |
| GlobalAveragePooling2D | 128 | - | - | - | 0 |
| Dense | 64 | - | 64 | ReLU | 8,256 |
| Dense | 5 | - | 5 | Softmax | 325 |
| Total | - | - | - | - | 101,829 |

## 5. Model A Parameter Calculation

Convolution formula: `P_conv = (K_h K_w C_in + 1) C_out`.

- Conv1: `(3 x 3 x 3 + 1) x 32 = 896`
- Conv2: `(3 x 3 x 32 + 1) x 64 = 18,496`
- Conv3: `(3 x 3 x 64 + 1) x 128 = 73,856`
- Dense 64: `(128 + 1) x 64 = 8,256`
- Dense 5: `(64 + 1) x 5 = 325`
- Total: `101,829`

## 6. Model B Architecture

| Layer | Output Shape | Kernel | Filters/Units | Activation | Trainable Parameters |
|---|---|---|---:|---|---:|
| Input | 64 x 64 x 3 | - | - | - | 0 |
| SeparableConv2D | 64 x 64 x 32 | 3 x 3 | 32 | ReLU | 155 |
| MaxPool2D | 32 x 32 x 32 | 2 x 2 | - | - | 0 |
| SeparableConv2D | 32 x 32 x 64 | 3 x 3 | 64 | ReLU | 2,400 |
| MaxPool2D | 16 x 16 x 64 | 2 x 2 | - | - | 0 |
| SeparableConv2D | 16 x 16 x 96 | 3 x 3 | 96 | ReLU | 6,816 |
| MaxPool2D | 8 x 8 x 96 | 2 x 2 | - | - | 0 |
| GlobalAveragePooling2D | 96 | - | - | - | 0 |
| Dense | 48 | - | 48 | ReLU | 4,656 |
| Dense | 5 | - | 5 | Softmax | 245 |
| Total | - | - | - | - | 14,272 |

## 7. Model B Parameter Calculation

Separable convolution formula with bias: `P_sep = K_h K_w C_in + C_in C_out + C_out`.

- SepConv1: `3 x 3 x 3 + 3 x 32 + 32 = 155`
- SepConv2: `3 x 3 x 32 + 32 x 64 + 64 = 2,400`
- SepConv3: `3 x 3 x 64 + 64 x 96 + 96 = 6,816`
- Dense 48: `(96 + 1) x 48 = 4,656`
- Dense 5: `(48 + 1) x 5 = 245`
- Total: `14,272`
- FP32 parameter storage: 55.75 KB.
- Parameter limit: 100,000.
- Reduction relative to Model A: 87,557 fewer parameters, or about 85.98% lower.

## 8. Optimizer Comparison

Controlled optimizer experiment settings:

- Model: Model B.
- Epochs: 5.
- Training batches per epoch: 30.
- Validation: full validation split.
- Selection criterion: lowest final validation loss.

| Optimizer | Learning Rate | Momentum | Final Validation Accuracy | Final Validation Loss |
|---|---:|---:|---:|---:|
| Adam | 0.001 | 0.0 | 0.509144127368927 | 1.2508898973464966 |
| SGD | 0.010 | 0.0 | 0.4835405945777893 | 1.4039305448532104 |
| SGD + Momentum | 0.010 | 0.9 | 0.4835405945777893 | 1.3384947776794434 |

Selected optimizer: Adam with learning rate 0.001. These optimizer metrics are controlled optimizer-selection evidence and are not the final full-training model results.

## 9. Model A Results

- Epochs: 20.
- Batch size: 32.
- Optimizer: Adam.
- Learning rate: 0.001.
- Loss: sparse categorical crossentropy.
- Environment: CPU only.
- Trainable parameters: 101,829.
- FP32 parameter storage: 397.77 KB.
- Mean epoch time: 12.8958 seconds.
- Test accuracy: 0.695906432748538.
- Macro precision: 0.7057296614536502.
- Macro recall: 0.6647908943697292.
- Macro F1-score: 0.6749622895035646.
- Confusion matrix:

```text
[[583,  67,   9,   2,   0],
 [194, 122,  16,  13,   5],
 [ 37,   7,  58,  11,  10],
 [  9,  14,   4,  92,   4],
 [  3,   8,   0,   3,  97]]
```

## 10. Model B Results

- Epochs: 20.
- Batch size: 32.
- Optimizer: Adam.
- Learning rate: 0.001.
- Loss: sparse categorical crossentropy.
- Environment: CPU only.
- Trainable parameters: 14,272.
- FP32 parameter storage: 55.75 KB.
- Mean epoch time: 7.8730 seconds.
- Test accuracy: 0.6483918128654971.
- Macro precision: 0.6430123008645605.
- Macro recall: 0.6202374219855493.
- Macro F1-score: 0.6209343583512273.
- Confusion matrix:

```text
[[521, 124,  13,   2,   1],
 [171, 142,  13,  10,  14],
 [ 24,  37,  40,  11,  11],
 [  8,  13,   1,  86,  15],
 [  2,   6,   0,   5,  98]]
```

## 11. Model A vs Model B Comparison

| Metric | Model A | Model B |
|---|---:|---:|
| Test accuracy | 0.695906432748538 | 0.6483918128654971 |
| Macro precision | 0.7057296614536502 | 0.6430123008645605 |
| Macro recall | 0.6647908943697292 | 0.6202374219855493 |
| Macro F1-score | 0.6749622895035646 | 0.6209343583512273 |
| Parameters | 101,829 | 14,272 |
| FP32 parameter storage | 397.77 KB | 55.75 KB |
| Mean epoch time | 12.8958 s | 7.8730 s |

Model B is smaller and faster, while Model A has higher accuracy and macro scores on this split.

## 12. MobileNetV2 Setup

- Input size: 224 x 224 x 3.
- Backbone: MobileNetV2 initialized with ImageNet weights.
- Backbone training status: frozen.
- Added head: GlobalAveragePooling2D, Dropout 0.2, Dense 5 Softmax.
- No fine-tuning/unfreezing beyond the new classification head.
- Optimizer: Adam, learning rate 0.001.
- Epochs: 20.
- Batch size: 32.

## 13. MobileNetV2 Results

- Total parameters: 2,264,389.
- Trainable parameters: 6,405.
- Saved model size: 9.25 MB.
- Mean epoch time: 100.5135 seconds.
- Test accuracy: 0.7426900584795322.
- Macro precision: 0.7981119904272388.
- Macro recall: 0.7419555816682123.
- Macro F1-score: 0.766795935240905.
- Confusion matrix:

```text
[[534, 120,   7,   0,   0],
 [123, 209,  13,   2,   3],
 [ 12,  29,  78,   3,   1],
 [  7,  12,   2,  98,   4],
 [  4,  10,   0,   0,  97]]
```

## 14. EfficientNetB0 Setup

- Input size: 224 x 224 x 3.
- Backbone: EfficientNetB0 initialized with ImageNet weights.
- Backbone training status: frozen.
- Added head: GlobalAveragePooling2D, Dropout 0.2, Dense 5 Softmax.
- No fine-tuning/unfreezing beyond the new classification head.
- Optimizer: Adam, learning rate 0.001.
- Epochs: 20.
- Batch size: 32.

## 15. EfficientNetB0 Results

- Total parameters: 4,055,976.
- Trainable parameters: 6,405.
- Saved model size: 16.33 MB.
- Mean epoch time: 158.3490 seconds.
- Test accuracy: 0.7726608187134503.
- Macro precision: 0.8226531718072583.
- Macro recall: 0.7653911731210724.
- Macro F1-score: 0.7825692545633167.
- Confusion matrix:

```text
[[617,  32,  11,   1,   0],
 [184, 146,  15,   4,   1],
 [ 12,  14,  93,   2,   2],
 [ 15,   2,   1, 103,   2],
 [  4,   6,   2,   1,  98]]
```

## 16. Final Model Comparison

| Metric | Model B | MobileNetV2 | EfficientNetB0 |
|---|---:|---:|---:|
| Test accuracy | 0.6483918128654971 | 0.7426900584795322 | 0.7726608187134503 |
| Macro precision | 0.6430123008645605 | 0.7981119904272388 | 0.8226531718072583 |
| Macro recall | 0.6202374219855493 | 0.7419555816682123 | 0.7653911731210724 |
| Total parameters | 14,272 | 2,264,389 | 4,055,976 |
| Trainable parameters | 14,272 | 6,405 | 6,405 |
| Memory/model size | 55.75 KB FP32 parameter storage | 9.25 MB saved model | 16.33 MB saved model |
| Computational-cost indicator | 7.8730 s/epoch | 100.5135 s/epoch | 158.3490 s/epoch |

EfficientNetB0 gives the highest test accuracy and macro scores. Model B gives the smallest memory footprint and fastest training epoch time.

## 17. Figure Paths

- Class distribution: `report/figures/class_distribution.png`
- Model A training history: `report/figures/model_a_history.png`
- Model A confusion matrix: `report/figures/model_a_confusion_matrix.png`
- Model B training history: `report/figures/model_b_history.png`
- Model B confusion matrix: `report/figures/model_b_confusion_matrix.png`
- MobileNetV2 training history: `report/figures/mobilenetv2_history.png`
- MobileNetV2 confusion matrix: `report/figures/mobilenetv2_confusion_matrix.png`
- EfficientNetB0 training history: `report/figures/efficientnetb0_history.png`
- EfficientNetB0 confusion matrix: `report/figures/efficientnetb0_confusion_matrix.png`

## 18. Member Contributions

| Member | Registration Number | Contribution |
|---|---|---|
| Rifnaz.K.R.M | 230550P | Dataset Preparation + Model A |
| Panuharan.S | 230462X | Model B + Efficiency Analysis |
| Peranavan.K | 230474K | Optimizer Comparison + Training/Evaluation |
| Lavanathan.J | 230371R | Pretrained Lightweight Models + Final Comparison |

## 19. References Required

- UCI Machine Learning Repository entry for DeFungi.
- MobileNetV2 paper: Sandler et al., "MobileNetV2: Inverted Residuals and Linear Bottlenecks", CVPR 2018.
- EfficientNet paper: Tan and Le, "EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks", ICML 2019.
