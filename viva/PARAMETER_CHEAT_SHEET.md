# Parameter Calculation Cheat Sheet

## Standard Conv2D

Formula:

```text
Parameters = (Kh x Kw x Cin + 1) x Cout
```

Where:

- `Kh`: kernel height.
- `Kw`: kernel width.
- `Cin`: input channels.
- `Cout`: output channels or filters.
- `+1`: bias term for each output channel.

## Model A Examples

Conv1:

```text
(3 x 3 x 3 + 1) x 32 = 896
```

Conv2:

```text
(3 x 3 x 32 + 1) x 64 = 18,496
```

Conv3:

```text
(3 x 3 x 64 + 1) x 128 = 73,856
```

## Dense Layer

Formula:

```text
Parameters = (input_units + 1) x output_units
```

Model A Dense 64:

```text
(128 + 1) x 64 = 8,256
```

Model A output layer:

```text
(64 + 1) x 5 = 325
```

Model A total:

```text
101,829 parameters
```

## Depthwise Separable Convolution

Formula with bias:

```text
Parameters = depthwise + pointwise + bias
Depthwise = Kh x Kw x Cin
Pointwise = Cin x Cout
Bias = Cout
```

Model B first SeparableConv2D:

```text
3 x 3 x 3 + 3 x 32 + 32 = 155
```

Equivalent standard convolution:

```text
(3 x 3 x 3 + 1) x 32 = 896
```

Why smaller:

- Standard convolution combines spatial filtering and channel mixing at once.
- Separable convolution splits this into cheaper steps.
- For this layer, 155 is much smaller than 896.
