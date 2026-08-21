from flask import Flask, jsonify

app = Flask(__name__)

# In-memory vote storage. Data resets whenever the application restarts.
votes = {}


@app.route("/")
def home():
    return "Welcome to the App"


@app.route("/health")
def health():
    return "App is running"


@app.route("/vote/<name>")
def vote(name):
    """Record one vote for the candidate in the URL."""
    votes[name] = votes.get(name, 0) + 1
    return jsonify({
        "message": "Vote recorded",
        "candidate": name,
        "votes": votes[name]
    })


@app.route("/results")
def results():
    """Return the current vote count for all candidates."""
    return jsonify(votes)


@app.route("/reset")
def reset():
    """Clear all stored votes."""
    votes.clear()
    return jsonify({"message": "All votes have been reset"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
