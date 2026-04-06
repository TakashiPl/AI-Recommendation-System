from data import DATA
import heapq

def classify_age(age):
    if age < 13:
        return "kid"
    elif age < 18:
        return "teen"
    return "adult"

def get_recommendations(age, interest, debug=False):
    group = classify_age(age)
    interests = [i.lower().strip() for i in interest.split(",")]
    recommendations = []

    if debug:
        print("DEBUG age group:", group)
        print("DEBUG interests:", interests)
    

    for d in DATA:
        recommendations.append({"name": d["name"], "points" : 0})
        if debug:
            print(recommendations)
            print(d["category"])
        if d["category"] in interests:
            for obj in recommendations:
                if obj["name"] == d["name"]:
                    obj["points"] += 3
        if d["age_group"] == group:
            for obj in recommendations:
                if obj["name"] == d["name"]:
                    obj["points"] += 2

    
    return heapq.nlargest(3, recommendations, key=lambda x: x['points'])