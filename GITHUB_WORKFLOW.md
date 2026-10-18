# GitHub Workflow

This workflow is for a shared repository with four real group members. Each member should use their own GitHub account and local Git identity. Do not impersonate another member, do not create fake dates, and do not rewrite history to simulate contribution activity.

## 1. Create The Shared Repository

1. One member creates a new empty GitHub repository.
2. Do not initialize the GitHub repository with a README, `.gitignore`, or license if the local project already contains them.
3. Keep the repository private or public according to the course submission requirement.

## 2. Add Collaborators

1. Open the GitHub repository settings.
2. Add the other three members as collaborators.
3. Each member accepts the GitHub invitation from their own account.

## 3. First Local Push

The initial member should push only after the local repository has been inspected:

```bash
git status
git add README.md requirements.txt .gitignore PROJECT_STATUS.md FINAL_AUDIT.md report_data.md data/README.md data/processed src results report GITHUB_FILE_AUDIT.md MEMBER_FILES.md GITHUB_WORKFLOW.md
git status
git commit -m "Initialize EN3150 Assignment 03 project"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```

Before committing, confirm that `data/raw/`, `.venv/`, and `results/models/*.keras` are not staged.

## 4. Clone And Pull

Each other member should clone the shared repository:

```bash
git clone <repository-url>
cd <repository-folder>
git pull origin main
```

If the repository is already cloned, pull before editing:

```bash
git pull origin main
```

## 5. Member-Specific Commits

Each member should commit only files they actually worked on or reviewed. Suggested authentic commit messages:

### Initial / Rifnaz

- `Initialize EN3150 Assignment 03 project`
- `Add DeFungi preprocessing and canonical dataset split`
- `Add standard CNN Model A`

### Panuharan

- `Add lightweight depthwise separable CNN Model B`
- `Add Model B efficiency analysis`

### Peranavan

- `Add optimizer comparison experiments`
- `Add custom model training and evaluation`
- `Add confusion matrices and Model A-B comparison`

### Lavanathan

- `Add MobileNetV2 transfer learning`
- `Add EfficientNetB0 transfer learning`
- `Add final lightweight model comparison`

### Shared Final Work

- `Add final LaTeX report`
- `Update README and final project documentation`

These are suggested messages only. Each real member should use their own Git identity and should commit only the relevant files.

## 6. Resolve Simple Conflicts

1. Run `git pull origin main` before starting work.
2. If Git reports a conflict, open the conflicting file and keep the correct combined content.
3. After resolving:

```bash
git status
git add <resolved-files>
git commit
```

4. Ask the relevant member before changing their owned report section or source file.

## 7. Push

After a member commits their own work:

```bash
git push origin main
```

If push is rejected because the remote has new commits:

```bash
git pull origin main
git push origin main
```

Resolve conflicts if Git asks.

## 8. Final Pull Before Submission

Before submitting:

```bash
git pull origin main
git status
```

Confirm:

- `report/main.pdf` is present.
- `README.md` describes dataset setup and commands.
- `data/raw/` is not tracked.
- `.venv/` is not tracked.
- `results/models/*.keras` is not tracked unless the group intentionally decides otherwise.
- Each member's visible commits were made from that member's own account and identity.
