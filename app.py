from flask import Flask, render_template, request
from utils.recommender import recommend_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        skills_input = request.form.get("skills")
        domain = request.form.get("domain")

        user_skills = [s.strip().lower() for s in skills_input.split(",")]

        recommendations, match_score = recommend_jobs(user_skills, domain)


        return render_template(
    "index.html",
    recommendations=recommendations,
    match_score=match_score
)



    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
