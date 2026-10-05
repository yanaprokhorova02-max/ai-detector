from flask import Flask, render_template, request
from cliche_detector import check_text_for_ai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Главная")

@app.route("/about")
def about():
    return render_template("about.html", title="О нас")

@app.route("/check-ai", methods=["GET", "POST"])
def check_ai():
    if request.method == "GET":
        return render_template("check_ai_form.html", title="Проверка на ИИ")

    text = request.form.get("text", "").strip()
    if not text:
        return render_template("check_ai_form.html", 
                               title="Проверка на ИИ",
                               error="Текст не может быть пустым.")

    data = check_text_for_ai(text)
    return render_template("check_ai_result.html",
                           title="Результат проверки",
                           original_text=text,
                           ai_prob=data["ai_prob"],
                           human_prob=data["human_prob"],
                           verdict=data["verdict"],
                           result=data["result"])

if __name__ == "__main__":
    print("\n--- ДОСТУПНЫЕ МАРШРУТЫ ---")
    print(app.url_map)
    print("--------------------------\n")
import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)