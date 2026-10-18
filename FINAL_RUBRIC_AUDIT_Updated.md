# EN3150 Assignment 03 — Final Rubric Audit

**Project:** Resource-Constrained CNN Design and Transfer Learning for DeFungi Image Classification  
**Report:** [`RandomGuess_A03_EN3150.pdf`](RandomGuess_A03_EN3150.pdf)  
**Audit basis:** Submitted final report and existing project evidence inventory  
**Overall assessment:** All five graded sections are addressed in the report; grading and repository/submission verification remain external.

> This is an evidence-coverage audit, **not an awarded grade** or an independent rerun of experiments. File paths below are taken from the supplied project audit and final report; only the uploaded report and audit were reviewed here.

## Rubric Coverage at a Glance

| Graded section | Maximum marks | Report coverage | Status |
|---|---:|---|---|
| Custom Architecture Design | 20 | §3; Tables 2–4; Appendix A | Addressed |
| Optimizer Selection & Tuning | 15 | §4; Table 5; Figure 2 | Addressed |
| Custom Model Training & Evaluation | 25 | §5; Tables 6–7; Figures 3–4 | Addressed |
| SOTA Fine-Tuning & Evaluation | 20 | §6; Tables 8–9; Figures 5–6 | Addressed |
| Final Comparison & Discussion | 20 | §§7–9; Table 10; Figures 7–8 | Addressed |
| **Total available** | **100** | **All graded sections covered** | **Not a grade prediction** |

## Detailed Rubric-to-Evidence Mapping

| Section | Requirement | Evidence / report location | Status | Qualification or remaining risk |
|---|---|---|---|---|
| Custom Architecture Design (20) | Model A standard Conv2D CNN, pooling, architecture details, shapes and activation rationale | `src/models.py`; `results/tables/model_a_architecture.csv`; §3.1, §3.5, Table 2, Appendix A | Addressed | Assessment of design quality remains with lecturer |
| Custom Architecture Design (20) | Model B depthwise-separable CNN with fewer than 100,000 trainable parameters | `src/models.py`; `results/tables/model_b_architecture.csv`; §3.2, Table 3, Appendix A; **14,272** trainable parameters | Addressed | No identified threshold violation |
| Custom Architecture Design (20) | Parameter formulas and layer-wise calculations | `results/tables/depthwise_parameter_comparison.csv`; §§3.3–3.4, Table 4, Equations (1)–(4) | Addressed | Model B has **85.98% fewer** parameters than Model A |
| Optimizer Selection & Tuning (15) | Compare SGD, SGD with momentum and selected Adam, including learning rates | `results/tables/optimizer_comparison.csv`; `results/metrics/optimizer_experiment_results.json`; §4, Table 5, Figure 2 | Addressed | Pilot used **30 training batches per epoch** for five epochs, not full final training |
| Optimizer Selection & Tuning (15) | Explain momentum and convergence | §4.2, Equations (5)–(6), §§4.4–4.5 | Addressed | Results support the specific controlled pilot only |
| Custom Model Training & Evaluation (25) | Train both custom CNNs for at least 20 epochs | `results/raw/model_a/history.csv`; `results/raw/model_b/history.csv`; §5.1 | Addressed | Both reported as **20 epochs**, batch size 32 |
| Custom Model Training & Evaluation (25) | Training/validation curves, accuracy, precision, recall and confusion matrices | `results/figures/`; `results/raw/model_a/`; `results/raw/model_b/`; §5, Table 6, Figures 3–4 | Addressed | H1/H2 confusion and lower H3 recall are discussed |
| Custom Model Training & Evaluation (25) | Compare parameters, serialized size, epoch time, accuracy and computation | `results/tables/custom_models.csv`; `results/tables/custom_latency.csv`; `results/tables/custom_model_macs.csv`; §5.5, Table 7 | Addressed | Serialized model size is not equivalent to FP32-only weight storage |
| SOTA Fine-Tuning & Evaluation (20) | Evaluate two lightweight pretrained architectures | `src/session3_transfer.py`; `results/raw/mobilenetv2/`; `results/raw/efficientnetb0/`; §6 | Addressed | **64×64** transfer-learning input is smaller than typical ImageNet practice |
| SOTA Fine-Tuning & Evaluation (20) | Same split, two-stage fine-tuning, test metrics, parameter counts and model sizes | `data/splits/`; `results/tables/pretrained_transfer_models.csv`; §6.3–6.4, Tables 8–9, Figures 5–6; §7, Table 10 | Addressed | Three frozen-head epochs and eight fine-tuning epochs are documented |
| Final Comparison & Discussion (20) | Compare Model B against MobileNetV2 and EfficientNet-B0, with all-four-model context | `results/tables/final_comparison.csv`; §7, Table 10, Figures 7–8 | Addressed | Model B is resource leader; EfficientNet-B0 is accuracy leader |
| Final Comparison & Discussion (20) | Discuss accuracy, memory, computational cost, limitations and errors | `results/tables/session3_transfer_tradeoff_notes.md`; §§7.5–9 | Addressed | No physical edge-device energy or RAM measurement; CPU timings are machine-specific |

## Dataset and Experimental Protocol

| Item | Reported value |
|---|---|
| Dataset | UCI DeFungi |
| Usable images | **9,114** RGB JPEG images |
| Classes | H1, H2, H3, H5, H6 |
| Input resolution | **64 × 64 × 3** |
| Split method | Deterministic stratified split, seed 42 |
| Training / validation / test | **6,379 / 1,367 / 1,368** |
| Test-set usage | Final evaluation, not checkpoint selection |
| Custom training | 20 epochs per model; batch size 32 |
| Chosen custom-model optimizer | Adam, learning rate 0.001 |
| Transfer learning | 3 head-training epochs at LR 0.001 + 8 fine-tuning epochs at LR 0.0001 |

## Verified Results Reported in the Final PDF

| Model | Parameters | Test accuracy | Macro precision | Macro recall | Macro F1 | Serialized size (KiB) | MAC estimate | CPU batch-1 mean (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Model A | 101,829 | 0.6959 | 0.7057 | 0.6648 | 0.6750 | 1,241.37 | 41,296,192 | 2.8241 |
| **Model B** | **14,272** | 0.6484 | 0.6430 | 0.6202 | 0.6209 | **219.41** | **4,621,040** | **1.5922** |
| MobileNetV2 | 2,264,389 | 0.6908 | 0.7232 | 0.6478 | 0.6672 | 22,000.13 | 24,454,912 | 170.1065 |
| **EfficientNet-B0** | 4,055,976 | **0.7668** | **0.8099** | **0.7856** | **0.7895** | 32,650.04 | 31,972,992 | 322.2855 |

**Interpretation:** Model B reduces parameter count by **85.98%**, serialized size by **82.33%**, the included MAC estimate by **88.81%**, and measured CPU latency by **43.62%** compared with Model A. Its test accuracy is lower by approximately **4.75 percentage points**. EfficientNet-B0 has the highest reported accuracy, at the cost of the largest saved model and slowest measured CPU inference.

### Optimizer Pilot (Model B)

| Optimizer | Learning rate | Momentum | Final validation loss | Final validation accuracy |
|---|---:|---:|---:|---:|
| **Adam** | 0.001 | 0.0 | **1.2509** | **0.5091** |
| SGD | 0.010 | 0.0 | 1.4039 | 0.4835 |
| SGD + momentum | 0.010 | 0.9 | 1.3385 | 0.4835 |

These are **optimizer-selection pilot** results, not the final test-set metrics.

## Reproducibility and Report Deliverables

The final PDF contains the dataset breakdown, architecture tables, parameter calculations, optimizer experiment, training curves, confusion matrices, four-model resource comparison, limitations, references, and reproducibility appendix.

- Final report: [`RandomGuess_A03_EN3150.pdf`](RandomGuess_A03_EN3150.pdf)
- Alternate report location documented in project: `report/main.pdf`
- LaTeX source: `report/main.tex`
- Reproducibility evidence: `results/tables/`, `results/raw/`, `results/figures/`, `results/verification/`
- Self-contained notebook listed in project inventory: `RandomGuess_A03_EN3150.ipynb`
- Assignment question paper: [`EN3150_Assignment_03_In23.pdf`](EN3150_Assignment_03_In23.pdf) (link works when this file is present in repository root)

## Risks, Limitations, and Final Checks

1. **Hardware scope:** CPU latency is measured for saved Keras models on the experiment machine, not on a Raspberry Pi or microcontroller. Energy consumption and peak device RAM were not measured.
2. **Methodology:** One stratified split and seed, limited hyperparameter search, class imbalance, and 64×64 pretrained inputs limit generalization of conclusions.
3. **MAC interpretation:** The reported MAC estimates omit activation, pooling, normalization, data movement, and other overhead; they should not be treated as complete hardware cost.
4. **Repository publishing:** The earlier audit states GitHub authentication/push may still need human verification. Do not mark the remote push as complete without checking the live repository.
5. **Moodle submission:** Confirm that the report and code were actually uploaded and can be reopened; this audit cannot confirm Moodle submission.
6. **Evidence links:** Ensure every referenced path is committed to the repository. Trained `.keras` files and raw dataset files may be intentionally excluded, as described in the project README.

## Overall Status

**Rubric coverage: COMPLETE IN FINAL REPORT**  
**Experimental outcomes: DOCUMENTED IN FINAL REPORT**  
**Independent code rerun: NOT PERFORMED IN THIS AUDIT**  
**GitHub remote and Moodle submission: REQUIRE EXTERNAL CONFIRMATION**

The assignment report addresses the rubric's five graded sections. Final marks depend on the lecturer's evaluation; the audit does not guarantee a score.
