# Peranavan.K -- 230474K Viva Notes

## Responsibility

Optimizer Comparison + Training/Evaluation.

## What To Say In 30 Seconds

I worked on optimizer comparison and evaluation. We compared Adam, SGD, and SGD with momentum using a controlled Model B experiment. Adam had the lowest final validation loss, 1.2509, so we used Adam with learning rate 0.001 for final custom training. I also evaluated Model A and Model B using test accuracy, macro precision, macro recall, F1-score, and confusion matrices.

## Optimizer

- Compared: Adam, SGD, SGD with momentum.
- Controlled setup: Model B, 5 epochs, 30 training batches per epoch, full validation split.
- Selected optimizer: Adam.
- Reason: Lowest final validation loss.
- Final validation losses:
  - Adam: 1.2509.
  - SGD: 1.4039.
  - SGD + Momentum: 1.3385.

## Training Setup

- Epochs: 20 for final custom models.
- Batch size: 32.
- Optimizer: Adam.
- Learning rate: 0.001.
- Loss: sparse categorical crossentropy.
- Environment: CPU only.

## Evaluation Results

| Metric | Model A | Model B |
|---|---:|---:|
| Test accuracy | 0.6959 | 0.6484 |
| Macro precision | 0.7057 | 0.6430 |
| Macro recall | 0.6648 | 0.6202 |
| Macro F1 | 0.6750 | 0.6209 |
| Mean epoch time | 12.8958 s | 7.8730 s |

## Key Answers

**What is an optimizer?**  
An optimizer updates model weights to reduce the loss.

**What is learning rate?**  
It controls the step size of each weight update.

**If learning rate is too high?**  
Training can become unstable and may miss good minima.

**If learning rate is too low?**  
Training can become very slow or get stuck improving too little.

**What is SGD?**  
Stochastic gradient descent updates weights using gradients from batches.

**What is momentum?**  
Momentum keeps a velocity term so updates can continue in consistent gradient directions.

**Why select Adam?**  
It had the lowest final validation loss in the controlled optimizer experiment.

**Why minimum 20 epochs?**  
The assignment required at least 20 epochs for final custom model training, and both Model A and B were trained for 20.

**Training vs validation vs test?**  
Training data updates weights, validation data guides choices, and test data gives final unbiased evaluation.

**What is a confusion matrix?**  
It shows true classes versus predicted classes, so we can see which classes are confused.

**Accuracy vs precision vs recall?**  
Accuracy is overall correct predictions. Precision asks how many predicted positives are correct. Recall asks how many actual positives are found.

**Why macro precision/recall?**  
Macro averaging treats each class equally, useful because DeFungi class counts are uneven.

**How did Model A compare with Model B?**  
Model A was more accurate. Model B was much smaller and faster.
