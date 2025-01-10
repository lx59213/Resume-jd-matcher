from flask import Flask, render_template
import os
import random

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# 幽默语录列表
SLOGANS = [
    "HR问我擅长什么，我说大实话。她说这不是实话吧？我说对，这是大实话。",
    '面试者问我的专长是什么，我说长相。他很惊讶地说："马上好？"我说："不，是从一家公司跳到另一家公司。"',
    "面试官：你的优点是什么？我：我说话直接！面试官：这不是优点！我：我说了我说话直接！",
]


@app.route("/")
def home():
    return render_template("base.html", slogan=random.choice(SLOGANS))


@app.route("/health")
def health():
    return "OK"
