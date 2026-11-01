# ISM2411 — Python for Business

**Name:** Amanda Grossi Ferreira  
**Semester:** Fall 2026  
**Instructor:** Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411. Each folder corresponds to one module and keeps the related Python files together.

## Modules

- `week07/` — Functions: `calculate_tax`, `apply_discount`, and `final_price`
- Lab 8 — Git and GitHub setup, documentation, and version-control practice

## How to Run

Each Python script is standalone. Open a terminal in the repository and run:

```bash
python3 week07/functions.py
```

## Reflection

### 1. Commit History

```text
1739ab3 add README with module listing and run instructions
610ab02 add module 7 functions: calculate_tax, apply_discount, final_price
79824f2 add .gitignore for Python and OS files
```

If I were hiring someone and saw this history, it would tell me that they work in an organized way and separate a project into clear steps. The messages explain what changed, so another person could understand the progress without opening every file.

### 2. How Git Changes My Editing Process

Git should make me test a working script and commit it before making a major change. Before this module, I might have edited the same file repeatedly or created several confusing copies, but now I can make smaller changes, commit each working version, and return to an earlier version if something breaks.

### 3. One Additional `.gitignore` Entry

I added `.venv/` because I may use a local Python virtual environment in VS Code. That folder contains machine-specific installed packages, can become large, and can be recreated when needed, so it should not be tracked in the repository.
