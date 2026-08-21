# Submission Guide

## What is included
- `app.py` — complete Flask voting application.
- `requirements.txt` — Flask dependency.
- `README.md` — required project documentation.
- `.gitignore` — standard Python exclusions.
- `.git/` — local Git history with Version 1 and Version 2 development/merge workflow.
- `screenshots/` — folder for the three mandatory GitHub/browser screenshots.

## Before submitting

1. Create a new empty GitHub repository, for example `flask-voting-app`.
2. Add the GitHub remote:
   ```bash
   git remote add origin https://github.com/<YOUR_USERNAME>/flask-voting-app.git
   ```
3. Push both branches:
   ```bash
   git push -u origin main
   git push -u origin dev
   ```
4. Run the application locally and capture a browser screenshot of `/health` or `/results`.
5. Open GitHub and capture the Branches page showing `main` and `dev`.
6. Open GitHub's commit history and capture the Version 1 and Version 2 merge history.
7. Save those three screenshots in the `screenshots` folder and update the image paths in `README.md` if necessary.
8. Push the screenshots and README changes to GitHub from `main` after verifying everything.

## Quick test

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then test:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/health`
- `http://127.0.0.1:5000/vote/Alice`
- `http://127.0.0.1:5000/vote/Alice`
- `http://127.0.0.1:5000/vote/Bob`
- `http://127.0.0.1:5000/results`
- `http://127.0.0.1:5000/reset`
- `http://127.0.0.1:5000/results`
