# Rifnaz.K.R.M -- 230550P Viva Notes

## Responsibility

Dataset Preparation + Model A.

## What To Say In 30 Seconds

I handled the DeFungi dataset preparation and Model A. I verified the image dataset, created the canonical stratified split, resized custom-model images to 64 x 64 x 3, normalized pixel values, and made sure the same split was reused. For Model A, I implemented the standard CNN with three Conv2D blocks, max pooling, global average pooling, and dense layers. Model A has 101,829 trainable parameters and reached 0.6959 test accuracy.

## Dataset Preparation

- Dataset: UCI DeFungi.
- Classes: H1, H2, H3, H5, H6.
- Usable images: 9,114.
- Split: train 6,379, validation 1,367, test 1,368.
- Preprocessing for custom CNNs: resize to 64 x 64 x 3 and scale pixels to [0, 1].
- Split strategy: stratified with seed 42.

## Model A Architecture

- Input: 64 x 64 x 3.
- Conv2D 32, 3 x 3, same padding, ReLU.
- MaxPooling 2 x 2.
- Conv2D 64, 3 x 3, same padding, ReLU.
- MaxPooling 2 x 2.
- Conv2D 128, 3 x 3, same padding, ReLU.
- MaxPooling 2 x 2.
- GlobalAveragePooling2D.
- Dense 64, ReLU.
- Dense 5, Softmax.
- Total parameters: 101,829.

## Key Answers

**Why DeFungi?**  
It is the verified image dataset used in our assignment pipeline, with five classes suitable for CNN classification.

**Why resize to 64 x 64?**  
The custom CNNs were designed for small edge-style inputs. Resizing to 64 x 64 reduces memory and computation while keeping a fixed input shape.

**Why RGB?**  
The verified images are RGB. Keeping three channels preserves color information available in the original images.

**Why normalize?**  
Scaling pixel values to [0, 1] makes optimization more stable than training directly on 0-255 pixel values.

**Why stratified split?**  
The class counts are uneven, so stratification keeps similar class proportions in train, validation, and test splits.

**Why 70/15/15?**  
It gives most images to training while still reserving validation data for model selection and test data for final evaluation.

**Why same split for every model?**  
It makes comparisons fair because each model is tested on the same images.

**What is data leakage?**  
Data leakage happens when information from validation or test data influences training. We avoid it by keeping split memberships separate.

**Why three convolution blocks?**  
They progressively learn simple to more complex features while downsampling the feature maps with pooling.

**Why max pooling?**  
It reduces spatial size and keeps strong activations, lowering computation in later layers.

**Why Global Average Pooling instead of Flatten?**  
Flatten would create many dense parameters. Global Average Pooling averages each feature map, reducing parameter count.

**How are convolution parameters calculated?**  
Use `(Kh x Kw x Cin + 1) x Cout`. The `+1` is the bias per output channel.

**Why ReLU?**  
ReLU is simple and hardware-friendly because it is basically `max(0, x)`.

**Why Softmax?**  
Softmax converts final logits into probabilities across the five classes.

**Why does Model A exceed 100,000 parameters but still satisfy the assignment?**  
Model A is the baseline standard CNN. The strict resource-constrained requirement applies to Model B, which has 14,272 parameters.
