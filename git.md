# Git Workflow Instructions for This Project

This project is designed to help you practice **real-world Git workflows**, even though you are working independently.
You **must not work directly on `main`**.

---

## Rules (Read First)

* ❌ Do **not** commit directly to `main`
* ✅ All work must be done on a feature branch
* ✅ All changes must be merged via a Pull Request (PR)
* ✅ Every PR must request a reviewer
* ✅ PRs must pass checks before merging

---

## Initial Setup (One Time)

### 1. Clone the repository

```bash
git clone <repo-url>
cd <repo-name>
```

### 2. Verify you are on `main`

```bash
git branch
```

You should see:

```text
* main
```

### 3. Pull the latest changes

```bash
git pull origin main
```

---

## Starting New Work

### 1. Create a new branch

Create a branch for each unit of work.

```bash
git checkout -b feature/<short-description>
```

**Examples:**

```bash
git checkout -b feature/add-csv-parser
git checkout -b feature/refactor-utils
git checkout -b bugfix/fix-off-by-one
```

---

## Making Changes

### 1. Edit code locally

Make your changes to the Python files.

### 2. Run tests (if applicable)

```bash
pytest
```

### 3. Stage your changes

```bash
git status
git add .
```

### 4. Commit your work

Write clear commit messages.

```bash
git commit -m "Add CSV parser for input data"
```

**Good commit messages:**

* “Add validation for empty inputs”
* “Refactor data loader for clarity”

**Avoid:**

* “fix”
* “stuff”
* “updates”

---

## Pushing Your Branch

Push your branch to GitHub:

```bash
git push -u origin feature/<branch-name>
```

---

## Opening a Pull Request (Required)

### 1. Open a PR on GitHub

* Base branch: `main`
* Compare branch: your feature branch

### 2. PR Title

Use a clear, descriptive title.

**Examples:**

* `Add CSV parser for data ingestion`
* `Fix indexing bug in preprocessing`

---

### 3. PR Description (Required)

Include:

* What you changed
* Why you changed it
* Any known limitations

**Template:**

```text
## What
Brief summary of the change.

## Why
Why this change is needed.

## Testing
How this was tested (e.g., pytest, manual testing).
```

---

### 4. Request a Reviewer

You **must request a reviewer** before merging.
(Yes, even if you are the only contributor.)

---

## Responding to Review Feedback

If changes are requested:

1. Make updates on the **same branch**
2. Commit the changes
3. Push again

```bash
git add .
git commit -m "Address PR feedback"
git push
```

The PR will update automatically.

---

## Merging the Pull Request

* Ensure all checks pass
* Use **Squash and Merge** (unless instructed otherwise)
* Do **not** delete history manually

---

## After Merging

### 1. Update local `main`

```bash
git checkout main
git pull origin main
```

### 2. Delete the old branch

```bash
git branch -d feature/<branch-name>
git push origin --delete feature/<branch-name>
```

---

## Common Mistakes to Avoid

* ❌ Committing directly to `main`
* ❌ Opening PRs without descriptions
* ❌ Large, unfocused PRs
* ❌ Ignoring review comments
* ❌ Force-pushing without instruction

---

## Goal of This Process

This workflow teaches you:

* Professional Git habits
* Safe collaboration patterns
* How real engineering teams work
* How to review and improve code iteratively

Follow it strictly — correctness matters less than **process discipline**.
