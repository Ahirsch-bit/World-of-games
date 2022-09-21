import json

with open("utilities/scores.json") as f:
    scores = json.load(f)


def get_scores(name):
    if scores.get(name) is None:
        return 0
    else:
        return scores[name]


def add_scores(name, score_initial, score_final):
    score_final = 3 if score_final == 0 else score_final
    scores[name] = score_initial + score_final
    sorted_values = sorted(scores.values(), reverse=True)  # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in scores.keys():
            if scores[k] == i:
                sorted_dict[k] = scores[k]
                break
    with open("utilities/scores.json", "w") as s:
        json.dump(sorted_dict, s)
