# Depthwise Separable Convolution: Simple Explanation

## Analogy

Imagine a team processing colored images.

Standard convolution is like one worker doing two jobs at the same time:

1. Looking for spatial patterns such as edges.
2. Mixing red, green, and blue channel information.

Depthwise separable convolution splits the job:

1. First, each channel is filtered separately.
2. Then, a 1 x 1 convolution mixes the channels.

This usually needs far fewer parameters.

## Technical Explanation

Standard Conv2D learns filters that cover all input channels and produce all output channels together.

Depthwise separable convolution uses:

- Depthwise convolution: one spatial filter per input channel.
- Pointwise convolution: 1 x 1 filters to combine channels.

## Actual Model B Example

First layer, input 3 channels and output 32 channels:

SeparableConv2D:

```text
3 x 3 x 3 + 3 x 32 + 32 = 155
```

Equivalent standard Conv2D:

```text
(3 x 3 x 3 + 1) x 32 = 896
```

So the separable version uses much fewer parameters for this layer.
