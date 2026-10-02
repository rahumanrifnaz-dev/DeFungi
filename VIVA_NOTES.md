# EN3150 Assignment 03 Viva Notes

## 60-Second Explanation

Our assignment was to build and compare image-classification models for a resource-constrained setting. We used the UCI DeFungi dataset, which has five classes: H1, H2, H3, H5, and H6. We verified 9,114 usable RGB images and created one stratified 70/15/15 split so every model was evaluated fairly on the same data membership.

Model A was our standard CNN baseline using normal Conv2D layers, max pooling, global average pooling, and dense layers. Model B was our lightweight model using depthwise separable convolutions, which split convolution into spatial filtering and channel mixing to reduce parameters. Model B had only 14,272 parameters, much smaller than Model A's 101,829.

We selected Adam after comparing it with SGD and SGD with momentum. Then we trained Model A and Model B for 20 epochs. Model A had better accuracy, but Model B was smaller and faster. We also tested MobileNetV2 and EfficientNetB0 with frozen ImageNet backbones. EfficientNetB0 had the highest accuracy, while Model B had the smallest memory footprint. So the final conclusion is a trade-off: Model B is best for strict resource limits, while EfficientNetB0 is better when accuracy is more important.

## 3-Minute Explanation

The problem was five-class image classification on the DeFungi image dataset. The dataset has microscopic fungi images in classes H1, H2, H3, H5, and H6. We verified 9,114 usable RGB JPEG images. The dataset is imbalanced, for example H1 has 4,404 images while H6 has 739 images, so we used a stratified split to preserve class proportions. The final split was 6,379 training images, 1,367 validation images, and 1,368 test images.

For custom CNNs, all images were resized to 64 x 64 x 3 and normalized to [0, 1]. Model A was a baseline standard CNN: Conv2D 32, Conv2D 64, Conv2D 128, max pooling after each convolution, global average pooling, Dense 64, and a five-class Softmax output. It had 101,829 trainable parameters. It was useful as a stronger baseline, even though it was not the constrained model.

Model B was the resource-constrained CNN. It replaced standard Conv2D layers with SeparableConv2D layers: 32, 64, and 96 filters, followed by global average pooling and Dense 48. It had 14,272 parameters and 55.75 KB estimated FP32 parameter storage, so it satisfied the under-100,000-parameter requirement.

For optimizer selection, we compared Adam, SGD, and SGD with momentum in a controlled limited-batch experiment using Model B. Adam had the lowest final validation loss, 1.2509, so we used Adam with learning rate 0.001 for final custom model training.

Both custom models were trained for 20 epochs with batch size 32. Model A reached test accuracy 0.6959, macro precision 0.7057, and macro recall 0.6648. Model B reached test accuracy 0.6484, macro precision 0.6430, and macro recall 0.6202. Model B was less accurate but much smaller and faster per epoch: 7.8730 seconds compared with 12.8958 seconds for Model A.

We also evaluated MobileNetV2 and EfficientNetB0 using transfer learning. The ImageNet backbones were frozen, and only a new classification head was trained. MobileNetV2 reached 0.7427 test accuracy, and EfficientNetB0 reached 0.7727, the best accuracy. However, their saved model sizes were 9.25 MB and 16.33 MB, much larger than Model B's 55.75 KB theoretical FP32 parameter storage.

The final result is not one universal best model. EfficientNetB0 is best for accuracy, MobileNetV2 is a good pretrained compromise, and Model B is best for tight edge-device constraints.

## 1. Project Overview

- What we did: Built and compared custom CNNs and pretrained lightweight CNNs for DeFungi image classification.
- Why: The assignment focuses on edge image classification, where accuracy, memory, and compute all matter.
- Important numbers: 9,114 images; 5 classes; 70/15/15 split; 4 evaluated models.
- Simple explanation: We tested a normal CNN, a small CNN, and pretrained models to see the trade-off between size and accuracy.
- Likely question: What is the main goal?
- Short answer: To classify DeFungi images while studying how compact models compare with higher-accuracy pretrained models.

## 2. Dataset

- What we did: Used the UCI DeFungi dataset.
- Why: It is an image dataset suitable for CNN classification, unlike tabular datasets.
- Important numbers: H1 4,404; H2 2,334; H3 819; H5 818; H6 739.
- Simple explanation: Each image belongs to one of five fungi classes.
- Likely question: Why not CIFAR-10?
- Short answer: The assignment uses our selected image dataset; this project uses DeFungi, not CIFAR-10.

## 3. Data Preparation

- What we did: Verified images, resized custom inputs to 64 x 64 x 3, normalized pixels, and created stratified splits.
- Why: Fixed input size is required for CNN training, normalization stabilizes learning, and stratification keeps class proportions similar.
- Important numbers: Train 6,379; validation 1,367; test 1,368; seed 42.
- Simple explanation: We prepared one fair split and reused it everywhere.
- Likely question: What prevents data leakage?
- Short answer: Each image path appears in only one split, and test data was not used for training or optimizer selection.

## 4. Model A

- What we did: Built a baseline CNN with Conv2D, MaxPooling, GlobalAveragePooling, Dense 64, and Softmax.
- Why: It gives a standard CNN reference before the constrained design.
- Important numbers: 101,829 parameters; 397.77 KB FP32 storage; test accuracy 0.6959.
- Simple explanation: Model A learns features using normal convolution layers.
- Likely question: Why Global Average Pooling?
- Short answer: It reduces parameters compared with Flatten because it averages each feature map into one value.

## 5. Model B

- What we did: Built a compact CNN using SeparableConv2D layers.
- Why: Depthwise separable convolutions reduce parameters and memory.
- Important numbers: 14,272 parameters; 55.75 KB FP32 storage; test accuracy 0.6484.
- Simple explanation: Model B processes each channel spatially first, then mixes channels with 1 x 1 convolution.
- Likely question: Did fewer parameters improve accuracy?
- Short answer: No. Model B was smaller and faster, but less accurate than Model A.

## 6. Optimizer Comparison

- What we did: Compared Adam, SGD, and SGD with momentum on Model B in a controlled 5-epoch limited-batch experiment.
- Why: To select an optimizer before final training.
- Important numbers: Adam final validation loss 1.2509; SGD 1.4039; SGD with momentum 1.3385.
- Simple explanation: Adam performed best by the selected validation-loss criterion.
- Likely question: Why not use test data for optimizer selection?
- Short answer: Test data must remain unseen until final evaluation.

## 7. Training

- What we did: Trained custom models for 20 epochs, batch size 32, Adam, learning rate 0.001.
- Why: Same training setup allows fair comparison.
- Important numbers: Model A mean epoch time 12.8958 s; Model B 7.8730 s.
- Simple explanation: Training learns weights from training data while validation monitors generalization.
- Likely question: What is an epoch?
- Short answer: One full pass through the training dataset.

## 8. Evaluation Metrics

- What we did: Reported test accuracy, macro precision, macro recall, macro F1, and confusion matrices.
- Why: Accuracy alone can hide class-level behavior, especially with uneven class counts.
- Important numbers: Model A macro recall 0.6648; Model B macro recall 0.6202.
- Simple explanation: Macro metrics average class performance equally.
- Likely question: Why macro averaging?
- Short answer: It prevents large classes from dominating the reported metric.

## 9. MobileNetV2

- What we did: Used MobileNetV2 with ImageNet weights, frozen backbone, and a new five-class head.
- Why: It is designed as a lightweight pretrained model.
- Important numbers: 2,264,389 total parameters; 6,405 trainable; 9.25 MB saved model; accuracy 0.7427.
- Simple explanation: It reuses general visual features learned from ImageNet.
- Likely question: Why freeze the backbone?
- Short answer: Freezing reduces trainable parameters and avoids over-updating pretrained features with limited data.

## 10. EfficientNetB0

- What we did: Used EfficientNetB0 with ImageNet weights, frozen backbone, and a new five-class head.
- Why: EfficientNet balances width, depth, and resolution using compound scaling.
- Important numbers: 4,055,976 total parameters; 6,405 trainable; 16.33 MB saved model; accuracy 0.7727.
- Simple explanation: It was the most accurate model but also the largest and slowest here.
- Likely question: What is compound scaling?
- Short answer: Scaling model width, depth, and input resolution together in a balanced way.

## 11. Final Comparison

- What we did: Compared Model B with MobileNetV2 and EfficientNetB0.
- Why: Model B is the constrained custom model, while pretrained models show accuracy alternatives.
- Important numbers: Model B 0.6484 accuracy; MobileNetV2 0.7427; EfficientNetB0 0.7727.
- Simple explanation: Accuracy increased with pretrained models, but memory and epoch time also increased.
- Likely question: Which model is best?
- Short answer: EfficientNetB0 for accuracy; Model B for strict memory and compute constraints.

## 12. Edge-Device Relevance

- What we did: Measured parameters, FP32 storage or saved size, and epoch-time indicator.
- Why: Edge devices have limited memory and compute.
- Important numbers: Model B has only 14,272 parameters and 55.75 KB FP32 parameter storage.
- Simple explanation: Smaller models are easier to deploy on constrained hardware.
- Likely question: Is epoch time the same as inference time?
- Short answer: No. It is only a computational-cost indicator from our training environment.

## 13. Main Conclusions

- Model A was more accurate than Model B among custom CNNs.
- Model B met the resource constraint and was much smaller.
- Adam was selected by lowest validation loss in the controlled optimizer comparison.
- EfficientNetB0 had the highest test accuracy, but the largest model size and slowest epoch time.
- The final decision depends on whether accuracy or resource use matters more.

## Each Member's 30-Second Answer

### Rifnaz.K.R.M

I worked on dataset preparation and Model A. I verified the DeFungi dataset, created the stratified train-validation-test split, handled resizing and normalization, and implemented the standard CNN baseline. I also checked the Model A parameter calculation and wrote the dataset and Model A report sections.

### Panuharan.S

I worked on Model B and the efficiency analysis. My part focused on using depthwise separable convolutions to reduce the parameter count below 100,000. I verified the parameter calculations, memory estimate, and explained why Model B is more suitable for constrained devices.

### Peranavan.K

I worked on the optimizer comparison and training/evaluation. I compared Adam, SGD, and SGD with momentum, selected Adam based on validation loss, trained the custom models, and evaluated them using accuracy, precision, recall, F1-score, and confusion matrices.

### Lavanathan.J

I worked on pretrained lightweight models and the final comparison. I used MobileNetV2 and EfficientNetB0 with frozen ImageNet backbones, trained new classification heads, reported their metrics, and compared them with Model B in terms of accuracy, memory, and computation.
