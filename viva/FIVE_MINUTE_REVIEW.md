# Five-Minute Review

## Dataset

DeFungi from UCI. Five classes: H1, H2, H3, H5, H6. Verified usable images: 9,114. Split: train 6,379, validation 1,367, test 1,368.

## Model A

Standard CNN with Conv2D, MaxPooling, GlobalAveragePooling, Dense 64, and Softmax. Parameters: 101,829. Test accuracy: 0.6959.

## Model B

Lightweight CNN using SeparableConv2D. Parameters: 14,272. FP32 storage: 55.75 KB. Test accuracy: 0.6484. Meets the under-100,000-parameter target.

## Optimizer

Compared Adam, SGD, and SGD with momentum using Model B. Adam selected because it had the lowest final validation loss: 1.2509.

## Main A/B Result

Model A is more accurate. Model B is smaller and faster per epoch.

## MobileNetV2

Frozen ImageNet backbone with new five-class head. Accuracy: 0.7427. Saved model size: 9.25 MB.

## EfficientNetB0

Frozen ImageNet backbone with new five-class head. Accuracy: 0.7727. Saved model size: 16.33 MB.

## Final Trade-Off

Model B is best for strict resource constraints. EfficientNetB0 is best for accuracy. MobileNetV2 is a pretrained middle option.

## 5 Formulas To Remember

1. Conv2D parameters: `(Kh x Kw x Cin + 1) x Cout`
2. Dense parameters: `(input_units + 1) x output_units`
3. SeparableConv2D parameters: `Kh x Kw x Cin + Cin x Cout + Cout`
4. Precision: `TP / (TP + FP)`
5. Recall: `TP / (TP + FN)`

## 10 Words/Concepts To Remember

1. Stratified split
2. Data leakage
3. Conv2D
4. SeparableConv2D
5. Global Average Pooling
6. Adam
7. Confusion matrix
8. Macro average
9. Transfer learning
10. Accuracy-resource trade-off

## 10 Likely Questions

1. Why did you use a stratified split?
2. Why resize to 64 x 64 for custom CNNs?
3. How is Model A's parameter count calculated?
4. Why is Model B smaller?
5. What is depthwise separable convolution?
6. Why did you select Adam?
7. What is macro precision?
8. Which model had the best accuracy?
9. Which model is best for edge deployment?
10. Why compare pretrained models with Model B?
