# Session 3 Transfer Learning Trade-off Notes

## Accuracy
- Highest measured test accuracy: EfficientNet-B0 (0.7668).
- Model B test accuracy: 0.6484.
- MobileNetV2 improved over Model B by 0.0424 absolute accuracy.
- EfficientNet-B0 improved over Model B by 0.1184 absolute accuracy.

## Memory Footprint
- Smallest serialized model in the measured artifacts: Model B (219.41 KiB).
- Parameter count and serialized model size are related but not identical; saved model metadata and layer state also affect disk footprint.

## Computational Cost
- Lowest included Conv/Dense MAC estimate: Model B (4621040 MACs).
- Lowest measured CPU mean latency: Model B (1.5922 ms).
- A smaller parameter count does not automatically imply lower latency, lower RAM, or lower energy. Only MACs and CPU latency were measured here.

## Limitations
- Single canonical split.
- Single seed for the split/training setup.
- Limited hyperparameter search.
- No physical edge-device or microcontroller energy measurement.
- Possible class imbalance in DeFungi.
- ImageNet transfer learning uses external prior visual knowledge.
- Transfer models were constrained to 64x64 input, which is smaller than standard ImageNet transfer-learning practice.
- CPU benchmark is not equivalent to microcontroller inference and excludes disk I/O and image decoding.
