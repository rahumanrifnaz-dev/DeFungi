# Difficult Viva Questions

1. Question: Why does parameter count not directly equal computational cost?  
Answer: Computation also depends on input resolution, feature-map sizes, operation types, memory access, and hardware acceleration.

2. Question: Why can a model with fewer parameters sometimes be slower?  
Answer: Some operations are less optimized on specific hardware, and feature-map operations can dominate runtime even with fewer weights.

3. Question: Why is model-file size different from theoretical FP32 parameter size?  
Answer: Saved model files include metadata, architecture information, optimizer state or serialization overhead depending on format.

4. Question: Why can pretrained networks outperform small custom CNNs?  
Answer: They start with useful visual features learned from large datasets, so the classifier head benefits from stronger representations.

5. Question: What is total parameters vs trainable parameters?  
Answer: Total parameters include all weights in the model. Trainable parameters are the weights updated during training. Frozen backbone weights count as total but not trainable.

6. Question: Why must test data not be used during optimizer selection?  
Answer: It would leak final evaluation information into model selection and make test results optimistic.

7. Question: Why is using the exact same split important?  
Answer: It ensures each model is tested on the same samples, so differences are due to model behavior rather than easier or harder data.

8. Question: Why is accuracy alone insufficient?  
Answer: If classes are uneven, a model can get good accuracy by doing well on large classes while performing poorly on smaller classes.

9. Question: Why does Global Average Pooling reduce parameters?  
Answer: It converts each feature map to one value, so the dense classifier receives far fewer inputs than it would after Flatten.

10. Question: Why can depthwise convolution reduce computation dramatically?  
Answer: It avoids applying a full spatial filter for every input-output channel pair, then uses cheaper 1 x 1 channel mixing.

11. Question: Why might 64 x 64 resizing reduce classification information?  
Answer: Downsampling can remove fine texture or microscopic detail that may help distinguish classes.

12. Question: Why is ImageNet pretraining still useful for microscopic fungi images?  
Answer: Early CNN layers often learn general visual patterns like edges and textures, which can transfer even when domains differ.

13. Question: What happens if validation influences too many decisions?  
Answer: The model-selection process can overfit to validation data, making validation performance less reliable.

14. Question: What is the limitation of measuring only training time per epoch?  
Answer: It is not the same as inference latency, memory usage during deployment, or energy consumption on edge hardware.

15. Question: What would quantization change for deployment?  
Answer: Quantization can reduce model size and speed up inference by using lower-precision weights, but it may slightly reduce accuracy.
