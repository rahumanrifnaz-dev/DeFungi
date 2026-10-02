# 50 Likely Viva Questions

1. Question: What is the task in this project?  
Short Answer: Five-class image classification on DeFungi.  
Extra Detail: The classes are H1, H2, H3, H5, and H6.

2. Question: How many usable images were verified?  
Short Answer: 9,114.  
Extra Detail: No unreadable images were found.

3. Question: What split did you use?  
Short Answer: Stratified 70/15/15 target split.  
Extra Detail: Train 6,379, validation 1,367, test 1,368.

4. Question: Why stratified splitting?  
Short Answer: To preserve class proportions.  
Extra Detail: DeFungi class counts are uneven.

5. Question: What is data leakage?  
Short Answer: When training indirectly uses validation or test information.  
Extra Detail: We avoided split overlap by using one canonical split.

6. Question: Why use the same split for every model?  
Short Answer: Fair comparison.  
Extra Detail: All models are evaluated on the same test membership.

7. Question: What input size did custom CNNs use?  
Short Answer: 64 x 64 x 3.  
Extra Detail: This reduces computation for custom models.

8. Question: Why normalize images?  
Short Answer: To stabilize training.  
Extra Detail: Pixel values were scaled to [0, 1] for custom CNNs.

9. Question: Describe Model A.  
Short Answer: A standard CNN baseline.  
Extra Detail: It uses Conv2D, MaxPooling, GAP, Dense, and Softmax.

10. Question: How many parameters does Model A have?  
Short Answer: 101,829.  
Extra Detail: It is the baseline, not the constrained model.

11. Question: What is the first Conv2D parameter calculation?  
Short Answer: `(3 x 3 x 3 + 1) x 32 = 896`.  
Extra Detail: The `+1` is the bias term.

12. Question: Why ReLU?  
Short Answer: It is simple and hardware-friendly.  
Extra Detail: It mainly computes `max(0, x)`.

13. Question: Why Softmax?  
Short Answer: It gives class probabilities.  
Extra Detail: The output has five units for five classes.

14. Question: Why Global Average Pooling?  
Short Answer: It reduces parameters.  
Extra Detail: It avoids flattening a large feature map.

15. Question: Describe Model B.  
Short Answer: A lightweight CNN using SeparableConv2D.  
Extra Detail: It has 14,272 parameters.

16. Question: Why is Model B under the parameter limit?  
Short Answer: It uses depthwise separable convolutions and a smaller dense layer.  
Extra Detail: Its total is well below 100,000.

17. Question: What is depthwise convolution?  
Short Answer: Spatial filtering per input channel.  
Extra Detail: It does not mix channels yet.

18. Question: What is pointwise convolution?  
Short Answer: A 1 x 1 convolution that mixes channels.  
Extra Detail: It follows depthwise filtering in separable convolution.

19. Question: Why does separable convolution reduce parameters?  
Short Answer: It splits spatial filtering and channel mixing.  
Extra Detail: This replaces one expensive operation with two cheaper ones.

20. Question: Give a Model B parameter example.  
Short Answer: First separable layer has 155 parameters.  
Extra Detail: `3 x 3 x 3 + 3 x 32 + 32 = 155`.

21. Question: How much smaller is Model B than Model A?  
Short Answer: 87,557 fewer parameters.  
Extra Detail: About 85.98% lower.

22. Question: What optimizer was selected?  
Short Answer: Adam.  
Extra Detail: It had the lowest final validation loss in the optimizer comparison.

23. Question: Which model was used for optimizer comparison?  
Short Answer: Model B.  
Extra Detail: It was a controlled 5-epoch limited-batch experiment.

24. Question: What was Adam's final validation loss in that experiment?  
Short Answer: 1.2509.  
Extra Detail: SGD was 1.4039 and SGD with momentum was 1.3385.

25. Question: What is learning rate?  
Short Answer: The optimizer step size.  
Extra Detail: Final training used 0.001 for Adam.

26. Question: What is momentum?  
Short Answer: A velocity term for gradient updates.  
Extra Detail: It helps continue in consistent update directions.

27. Question: What loss function was used?  
Short Answer: Sparse categorical crossentropy.  
Extra Detail: Labels were integer class IDs.

28. Question: How many epochs for final custom models?  
Short Answer: 20.  
Extra Detail: Both Model A and Model B used 20 epochs.

29. Question: What is batch size?  
Short Answer: Number of samples processed per update.  
Extra Detail: We used batch size 32.

30. Question: What is a confusion matrix?  
Short Answer: A table of true versus predicted classes.  
Extra Detail: Diagonal values are correct predictions.

31. Question: Model A test accuracy?  
Short Answer: 0.6959.  
Extra Detail: Macro precision 0.7057 and macro recall 0.6648.

32. Question: Model B test accuracy?  
Short Answer: 0.6484.  
Extra Detail: Macro precision 0.6430 and macro recall 0.6202.

33. Question: Which custom model was more accurate?  
Short Answer: Model A.  
Extra Detail: Model B traded accuracy for smaller size.

34. Question: Which custom model was faster per epoch?  
Short Answer: Model B.  
Extra Detail: 7.8730 s/epoch versus 12.8958 s/epoch.

35. Question: What is macro precision?  
Short Answer: Precision averaged equally over classes.  
Extra Detail: Useful for uneven class counts.

36. Question: Why not only accuracy?  
Short Answer: Accuracy can hide class-level weakness.  
Extra Detail: Macro metrics show performance across classes.

37. Question: What pretrained models were used?  
Short Answer: MobileNetV2 and EfficientNetB0.  
Extra Detail: Both used ImageNet weights.

38. Question: What is transfer learning?  
Short Answer: Reusing pretrained features for a new task.  
Extra Detail: We trained a new five-class head.

39. Question: Were pretrained backbones frozen?  
Short Answer: Yes.  
Extra Detail: Only the new head was trainable.

40. Question: MobileNetV2 test accuracy?  
Short Answer: 0.7427.  
Extra Detail: Saved model size 9.25 MB.

41. Question: EfficientNetB0 test accuracy?  
Short Answer: 0.7727.  
Extra Detail: It was the highest accuracy model.

42. Question: Which model had the smallest memory footprint?  
Short Answer: Model B.  
Extra Detail: 55.75 KB estimated FP32 parameter storage.

43. Question: Which model had the largest saved model size?  
Short Answer: EfficientNetB0.  
Extra Detail: 16.33 MB.

44. Question: Why can pretrained models perform better?  
Short Answer: They reuse rich visual features learned from large datasets.  
Extra Detail: Even if ImageNet is different, early visual features can transfer.

45. Question: What is MobileNetV2 known for?  
Short Answer: Lightweight efficient architecture.  
Extra Detail: It uses inverted residuals and bottlenecks.

46. Question: What is EfficientNet known for?  
Short Answer: Compound scaling.  
Extra Detail: It balances width, depth, and resolution.

47. Question: Which model is best for edge devices?  
Short Answer: Model B under strict memory/compute limits.  
Extra Detail: EfficientNetB0 is best for accuracy if resources allow.

48. Question: Did you retrain during final audit?  
Short Answer: No.  
Extra Detail: Final checks used saved metrics and quick validation commands.

49. Question: What is the main limitation of the project?  
Short Answer: Epoch time is only a rough computational indicator.  
Extra Detail: Actual edge inference time would need deployment testing.

50. Question: What is the final conclusion?  
Short Answer: There is a clear accuracy-resource trade-off.  
Extra Detail: Small Model B is efficient; EfficientNetB0 is most accurate.
