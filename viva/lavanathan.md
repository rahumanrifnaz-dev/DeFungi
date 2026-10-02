# Lavanathan.J -- 230371R Viva Notes

## Responsibility

Pretrained Lightweight Models + Final Comparison.

## What To Say In 30 Seconds

I worked on MobileNetV2, EfficientNetB0, and the final comparison. We used transfer learning with ImageNet pretrained backbones. The backbones were frozen, and we trained a new classification head for the five DeFungi classes. MobileNetV2 reached 0.7427 test accuracy, and EfficientNetB0 reached 0.7727, the highest accuracy. However, Model B was still the smallest model, so the final choice depends on the accuracy-resource trade-off.

## Transfer Learning Setup

- Input size: 224 x 224 x 3.
- Backbones: ImageNet pretrained MobileNetV2 and EfficientNetB0.
- Backbone status: frozen.
- Head: GlobalAveragePooling2D, Dropout 0.2, Dense 5 Softmax.
- No backbone unfreezing was performed in this project.

## Results

| Metric | MobileNetV2 | EfficientNetB0 |
|---|---:|---:|
| Total parameters | 2,264,389 | 4,055,976 |
| Trainable parameters | 6,405 | 6,405 |
| Saved model size | 9.25 MB | 16.33 MB |
| Test accuracy | 0.7427 | 0.7727 |
| Macro precision | 0.7981 | 0.8227 |
| Macro recall | 0.7420 | 0.7654 |
| Mean epoch time | 100.5135 s | 158.3490 s |

## Key Answers

**What is transfer learning?**  
Using a model pretrained on a large dataset, then adapting it to a new task.

**Why use pretrained models?**  
They already contain useful visual feature extractors, so they can improve accuracy compared with small custom CNNs.

**What is ImageNet?**  
A large natural-image dataset used to pretrain many CNN backbones.

**Why freeze layers first?**  
Freezing keeps pretrained features fixed and reduces trainable parameters.

**Why unfreeze only some layers?**  
That is a common fine-tuning method, but in this project we did not unfreeze; we trained only the new head.

**Why use smaller learning rate for fine-tuning?**  
If fine-tuning pretrained layers, a smaller learning rate avoids damaging useful pretrained weights. In our project, the frozen-backbone head used Adam 0.001.

**What makes MobileNetV2 lightweight?**  
It uses efficient building blocks such as inverted residuals, bottlenecks, and depthwise separable operations.

**What is an inverted residual?**  
A block that expands channels internally but keeps the shortcut between narrow bottleneck representations.

**What is a linear bottleneck?**  
A bottleneck layer without nonlinear activation at the end, used to preserve useful information.

**What is EfficientNet?**  
A model family that scales depth, width, and input resolution in a balanced way.

**What is compound scaling?**  
Scaling model width, depth, and resolution together rather than changing only one dimension.

**Why compare pretrained models with Model B?**  
Model B shows the constrained custom model; pretrained models show what accuracy can be achieved with larger feature extractors.

**Which model had higher accuracy?**  
EfficientNetB0, with test accuracy 0.7727.

**Which had lower memory usage?**  
Model B, with 55.75 KB estimated FP32 parameter storage.

**Which is more suitable for resource-constrained hardware?**  
Model B if memory/compute are strict. EfficientNetB0 if higher accuracy is more important and the hardware can support it.
