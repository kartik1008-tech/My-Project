# Flask Voting Application with Git Versioning Workflow

## Project Description
This project is a small voting application built with Python and Flask. Users can vote for a candidate by visiting a URL. The application keeps the vote counts in memory and provides a page to view the current results. A reset feature was added in Version 2 to clear all votes. The project also demonstrates a `dev` and `main` Git branching workflow.

## Installation and Setup

### 1. Clone the repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd flask-voting-app
```

### 2. Create a virtual environment

Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:
```cmd
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The application will be available at:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health

## API Endpoint Reference

| Endpoint | Method | Description | Example Response |
|---|---|---|---|
| `/` | GET | Displays the welcome message. | `Welcome to the App` |
| `/health` | GET | Confirms that the application is running. | `App is running` |
| `/vote/<name>` | GET | Records one vote for the candidate. | `{"candidate":"Alice","message":"Vote recorded","votes":1}` |
| `/results` | GET | Returns the current vote count for all candidates as JSON. | `{"Alice":2,"Bob":1}` |
| `/reset` | GET | Clears all vote counts. | `{"message":"All votes have been reset"}` |

### Example Usage

Vote for Alice twice:
```text
http://127.0.0.1:5000/vote/Alice
http://127.0.0.1:5000/vote/Alice
```

Vote for Bob once:
```text
http://127.0.0.1:5000/vote/Bob
```

View results:
```text
http://127.0.0.1:5000/results
```

Expected result:
```json
{
  "Alice": 2,
  "Bob": 1
}
```

Reset all votes:
```text
http://127.0.0.1:5000/reset
```

After reset, `/results` returns an empty JSON object:
```json
{}
```

## Git Workflow

The project follows the required `dev` and `main` workflow.

```text
main  ────────────────● Version 1 ────────────────● Version 2
                       ▲                             ▲
                       │ merge                       │ merge
                       │                             │
dev   ─────●───────────┘               ─────●───────┘
         Version 1 work                      Version 2 work
```

### Version 1 workflow
```bash
git init
git branch -M main
git checkout -b dev
git add .
git commit -m "feat: add basic Flask voting application"
git push -u origin dev
git checkout main
git merge --no-ff dev -m "release: merge Version 1 into main"
git push -u origin main
```

### Version 2 workflow
```bash
git checkout main
git checkout -b dev
git add app.py README.md
git commit -m "feat: add vote reset endpoint"
git push -u origin dev
git checkout main
git merge --no-ff dev -m "release: merge Version 2 into main"
git push origin main
```

`main` contains only stable, working versions. New development is completed in `dev` and merged into `main` after testing.

## Version History

| Version | Features |
|---|---|
| Version 1 | Flask application, `/`, `/health`, `/vote/<name>`, and `/results`; Git `dev` and `main` workflow. |
| Version 2 | Added `/reset` endpoint to clear all stored vote counts and updated documentation. |

## Screenshots

The assignment requires these screenshots to be embedded directly in this README. Add the real screenshots from your own GitHub repository before final submission.

### 1. Application running in browser
Replace the placeholder below with a screenshot showing a working endpoint such as `/health` or `/results`.

`![Application running](screenshots/application-running.png)`

### 2. GitHub repository showing dev and main branches
Replace the placeholder below with a screenshot of your GitHub repository's Branches page showing both `dev` and `main`.

`![GitHub branches](screenshots/github-branches.png)`

### 3. Version 1 and Version 2 commit/merge history
Replace the placeholder below with a screenshot of the GitHub commit history showing the Version 1 and Version 2 commits/merges.

`![Git history](screenshots/github-history.png)`

## Testing Checklist

- `/` returns `Welcome to the App`.
- `/health` returns `App is running`.
- `/vote/Alice` records Alice's vote.
- Repeating `/vote/Alice` increases Alice's vote count.
- `/results` returns JSON vote counts.
- `/reset` clears all votes.
- `/results` returns `{}` after reset.
- Version 1 and Version 2 have separate commits and merge history.

## Notes

The assignment specifies an in-memory voting system, so vote data is intentionally not stored in a database. All vote counts are lost when the Flask application is restarted.
