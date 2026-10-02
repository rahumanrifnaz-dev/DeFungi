# Session 2 Custom Model Interpretation Notes

- Parameter reduction from Model A to Model B: 87,557 fewer parameters (85.98% reduction).
- Theoretical FP32 storage reduction: 397.77 KiB to 55.75 KiB.
- MAC reduction: 41,296,192 to 4,621,040 included Conv/Dense MACs.
- Test accuracy difference: Model A 0.6959, Model B 0.6484; Model A is higher by 0.0475.
- Mean epoch-time difference: Model A 12.8958 s, Model B 7.8730 s.
- CPU batch-1 latency on this machine: Model A mean 2.8241 ms, p95 3.2042 ms; Model B mean 1.5922 ms, p95 2.2656 ms.
- Do not assume fewer MACs always means lower latency. Actual latency depends on hardware, TensorFlow kernels, memory access, and operation optimization.
