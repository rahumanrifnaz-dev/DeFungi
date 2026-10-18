# Member Git Instructions

These instructions are for real contributions from the four EN3150 Assignment 03 group members. Do not impersonate another member, do not fake old dates, and do not create meaningless commits just to generate activity.

## Common Workflow For Every Member

```bash
git clone <repository-url>
cd EN3150-Assignment-03
git config user.name "REAL MEMBER NAME"
git config user.email "REAL MEMBER EMAIL"
git pull origin main
```

Then:

1. Review the files related to your actual contribution.
2. Make genuine improvements, corrections, or documentation updates if needed.
3. Stage only the files you changed.

```bash
git status
git add <specific-files>
git commit -m "meaningful commit message"
git pull --rebase origin main
git push origin main
```

Never run `git push --force` unless there is an exceptional reason and the whole team understands the consequences.

## RIFNAZ.K.R.M -- 230550P

Main contribution:

- DeFungi dataset preparation
- Canonical split
- Model A
- Dataset/report section

Suggested genuine tasks:

- Review `src/data_prepare.py`.
- Review Model A code in `src/models.py`.
- Check `data/README.md` and dataset documentation.
- Verify Model A parameter count.
- Improve comments or documentation only if needed.

Suggested commit messages, only if they match actual changes:

- `Add DeFungi preprocessing and canonical split`
- `Add standard CNN Model A`

Relevant files:

- `src/data_prepare.py`
- `src/datasets.py`
- `src/config.py`
- `src/models.py`
- `data/README.md`
- `data/processed/`
- `report/sections/02_dataset.tex`
- `report/sections/03_model_a.tex`
- `report/figures/class_distribution.png`

## PANUHARAN.S -- 230462X

Main contribution:

- Model B
- Depthwise separable CNN
- Efficiency analysis

Suggested genuine tasks:

- Review Model B architecture in `src/models.py`.
- Confirm Model B is within the 100,000-parameter limit.
- Verify depthwise-separable parameter calculations.
- Improve Model B comments or report section only if needed.

Suggested commit messages, only if they match actual changes:

- `Add lightweight depthwise separable CNN Model B`
- `Add Model B parameter and efficiency analysis`

Relevant files:

- `src/models.py`
- `src/model_checks.py`
- `results/metrics/model_parameter_checks.json`
- `results/metrics/model_b_summary.txt`
- `report/sections/04_model_b.tex`
- `report/figures/model_b_history.png`
- `report/figures/model_b_confusion_matrix.png`

## PERANAVAN.K -- 230474K

Main contribution:

- Optimizer experiments
- Training
- Evaluation
- Confusion matrices
- Model A/B comparison

Suggested genuine tasks:

- Review optimizer configuration.
- Check training scripts.
- Verify evaluation metrics.
- Verify confusion matrices.
- Review Model A/B comparison table.

Suggested commit messages, only if they match actual changes:

- `Add optimizer comparison experiments`
- `Add custom model training and evaluation`
- `Add Model A and Model B comparison results`

Relevant files:

- `src/optimizer_experiment.py`
- `src/train_custom.py`
- `src/smoke_test.py`
- `src/verify_pipeline.py`
- `src/utils.py`
- `results/metrics/optimizer_experiment_results.json`
- `results/metrics/model_a_adam_metrics.json`
- `results/metrics/model_b_adam_metrics.json`
- `results/figures/model_a_adam_history.png`
- `results/figures/model_b_adam_history.png`
- `results/confusion_matrices/model_a_adam_confusion_matrix.png`
- `results/confusion_matrices/model_b_adam_confusion_matrix.png`
- `report/sections/05_optimizer.tex`
- `report/sections/06_training_evaluation.tex`

## LAVANATHAN.J -- 230371R

Main contribution:

- MobileNetV2
- EfficientNetB0
- Pretrained evaluation
- Final trade-off analysis

Suggested genuine tasks:

- Review transfer-learning setup.
- Verify frozen backbone configuration.
- Verify pretrained-model metrics.
- Review final comparison section.

Suggested commit messages, only if they match actual changes:

- `Add MobileNetV2 transfer learning`
- `Add EfficientNetB0 transfer learning`
- `Add final lightweight model comparison`

Relevant files:

- `src/train_pretrained.py`
- `results/metrics/mobilenetv2_transfer_metrics.json`
- `results/metrics/efficientnetb0_transfer_metrics.json`
- `results/figures/mobilenetv2_transfer_history.png`
- `results/figures/efficientnetb0_transfer_history.png`
- `results/confusion_matrices/mobilenetv2_transfer_confusion_matrix.png`
- `results/confusion_matrices/efficientnetb0_transfer_confusion_matrix.png`
- `report/sections/07_pretrained_models.tex`
- `report/sections/08_final_comparison.tex`

## Conflict Prevention

Members should preferably edit different files:

- Rifnaz: dataset preparation, Model A, `report/sections/02_dataset.tex`, `report/sections/03_model_a.tex`
- Panuharan: Model B and `report/sections/04_model_b.tex`
- Peranavan: optimizer/training/evaluation source, `report/sections/05_optimizer.tex`, `report/sections/06_training_evaluation.tex`
- Lavanathan: pretrained model source, `report/sections/07_pretrained_models.tex`, `report/sections/08_final_comparison.tex`

Shared files such as `README.md`, `report/main.tex`, and `report/references.bib` should be modified carefully and only after pulling the latest changes.

## If A Merge Conflict Occurs

If pull or rebase causes a conflict:

1. Run `git status`.
2. Open the conflicted file.
3. Inspect the conflict markers:

```text
<<<<<<<
=======
>>>>>>>
```

4. Preserve the correct combined content.
5. Remove the conflict markers.
6. Stage the resolved file:

```bash
git add <resolved-file>
```

7. Continue the rebase:

```bash
git rebase --continue
```

If uncertain, stop and ask the team to inspect the conflict. Do not guess and overwrite another member's work.

## Final Team Sync

After all real member contributions are pushed, the repository owner should run:

```bash
git pull origin main
git status
git log --oneline --decorate --all
```

Do not alter authorship. Do not squash member commits unless the team has a clear reason.
