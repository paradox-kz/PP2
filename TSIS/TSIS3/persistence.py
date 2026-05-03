import json

def save_score(score, distance):
    data = load_scores()
    data.append({"score": score, "distance": distance})

    data = sorted(data, key=lambda x: x["score"], reverse=True)

    with open("leaderboard.json", "w") as f:
        json.dump(data, f)

def load_scores():
    try:
        with open("leaderboard.json") as f:
            return json.load(f)
    except:
        return []

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"difficulty": "normal"}