# Final Results Cheat Sheet

| Model | Parameters | Model Size | Test Accuracy | Macro Precision | Macro Recall | Training Time / Computational Indicator |
|---|---:|---|---:|---:|---:|---:|
| Model A | 101,829 trainable | 397.77 KB FP32 parameter storage | 0.6959 | 0.7057 | 0.6648 | 12.8958 s/epoch |
| Model B | 14,272 trainable | 55.75 KB FP32 parameter storage | 0.6484 | 0.6430 | 0.6202 | 7.8730 s/epoch |
| MobileNetV2 | 2,264,389 total; 6,405 trainable | 9.25 MB saved model | 0.7427 | 0.7981 | 0.7420 | 100.5135 s/epoch |
| EfficientNetB0 | 4,055,976 total; 6,405 trainable | 16.33 MB saved model | 0.7727 | 0.8227 | 0.7654 | 158.3490 s/epoch |

## 3 Key Observations

1. Model B is much smaller than Model A: 14,272 parameters versus 101,829.
2. Model A is more accurate than Model B among custom CNNs: 0.6959 versus 0.6484 test accuracy.
3. EfficientNetB0 has the best accuracy, 0.7727, but it also has the largest saved model size and slowest measured epoch time.

## Final Trade-Off

- Choose Model B when memory and compute are strict.
- Choose EfficientNetB0 when accuracy is more important and the device can support the larger model.
- MobileNetV2 is between them: better accuracy than Model B and smaller than EfficientNetB0.
