# Panuharan.S -- 230462X Viva Notes

## Responsibility

Model B + Efficiency Analysis.

## What To Say In 30 Seconds

I worked on the lightweight Model B. The goal was to reduce the parameter count and make the model more suitable for resource-constrained devices. Model B uses depthwise separable convolution instead of normal convolution. It has only 14,272 trainable parameters and 55.75 KB estimated FP32 parameter storage, which is far below the 100,000-parameter limit.

## Model B Architecture

- Input: 64 x 64 x 3.
- SeparableConv2D 32, 3 x 3, ReLU.
- MaxPooling 2 x 2.
- SeparableConv2D 64, 3 x 3, ReLU.
- MaxPooling 2 x 2.
- SeparableConv2D 96, 3 x 3, ReLU.
- MaxPooling 2 x 2.
- GlobalAveragePooling2D.
- Dense 48, ReLU.
- Dense 5, Softmax.
- Total parameters: 14,272.

## Key Answers

**What is depthwise convolution?**  
It applies one spatial filter separately to each input channel.

**What is pointwise convolution?**  
It is a 1 x 1 convolution that mixes information across channels.

**Why 1 x 1 convolution?**  
It combines channel information with very few parameters compared with a full spatial convolution.

**How is SeparableConv2D different from Conv2D?**  
Conv2D does spatial filtering and channel mixing together. SeparableConv2D separates them into depthwise spatial filtering and pointwise channel mixing.

**Why does it reduce parameters?**  
A standard convolution has `Kh x Kw x Cin x Cout` style weights. A separable convolution uses `Kh x Kw x Cin` plus `Cin x Cout`, which is usually much smaller.

**Simple parameter example from Model B:**  
First separable layer from 3 channels to 32 filters:
`3 x 3 x 3 + 3 x 32 + 32 = 155` parameters.

Equivalent standard Conv2D:
`(3 x 3 x 3 + 1) x 32 = 896` parameters.

**Why must Model B be <=100,000 parameters?**  
The assignment asks for a resource-constrained model. Our Model B has 14,272 parameters, so it satisfies the constraint.

**How much smaller is Model B than Model A?**  
Model A has 101,829 parameters. Model B has 14,272, which is 87,557 fewer parameters, about 85.98% lower.

**Does fewer parameters always mean better accuracy?**  
No. Model B is smaller, but its test accuracy is 0.6484, while Model A reaches 0.6959.

**Why is Model B suitable for edge devices?**  
It has low parameter count, small theoretical FP32 storage, and lower measured epoch time than Model A.
