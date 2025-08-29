import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from collections import Counter
import re

# Loading data
filepath = "data/dataset.csv"
df = pd.read_csv(filepath, encoding="utf-8")

# ------------------------
# Preprocessing for learning_goal
# ------------------------

# Minimal Spanish stopwords list (only connectors, articles, pronouns)
spanish_stopwords = {
    "de", "del", "la", "el", "los", "las", "un", "una", "unos", "unas",
    "y", "o", "u", "pero", "porque", "como", "que", "al", "a", "en", "con", "por", "para", 
    "su", "sus", "mi", "mis", "tu", "tus", "nuestro", "nuestra", "nuestros", "nuestras",
    "yo", "tú", "vos", "usted", "ustedes", "nosotros", "nosotras", "ellos", "ellas", "lo", "le",
    "es", "son", "ser", "se", "más", "tener", "nuevas", "sobre", "me"
}

def preprocess_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text, re.UNICODE)
    filtered_words = [w for w in words if w not in spanish_stopwords]
    return filtered_words

all_words = []
for goal in df["learning_goal"].dropna():
    all_words.extend(preprocess_text(goal))

word_counts = Counter(all_words).most_common(10)
words, counts = zip(*word_counts) if word_counts else ([], [])

# ------------------------
# Create plots
# ------------------------

fig_age = px.histogram(df, x="age_range", title="Age Distribution")
fig_gender = px.histogram(df, x="gender", title="Gender Distribution")
fig_edu = px.histogram(df, x="education_level", title="Education Level")
fig_working = px.histogram(df, x="currently_working", title="Currently Working?")
fig_python = px.histogram(df, x="python_level", title="Python Level")
fig_git = px.histogram(df, x="uses_git", title="Uses Git?")
fig_linkedin = px.histogram(df, x="has_linkedin", title="Has LinkedIn?")

# Knowledge of frontend, backend, db
df_skills = df.melt(
    value_vars=["knows_frontend", "knows_backend", "knows_databases"],
    var_name="Skill", value_name="Knows"
)
fig_skills = px.histogram(
    df_skills, x="Skill", color="Knows", barmode="group", title="Knowledge of Frontend, Backend, and Databases"
)

# Learning goal word frequency (horizontal, sorted descending)
fig_learning_goal = px.bar(
    x=counts,
    y=words,
    orientation="h",
    title="Most Frequent Words in Learning Goals",
    text=counts
)

fig_learning_goal.update_traces(textposition="outside")
fig_learning_goal.update_layout(
    yaxis={'categoryorder': 'total ascending'}
)


# How did you hear (horizontal bar chart, sorted descending)
hear_counts = df["how_did_you_hear"].value_counts().reset_index()
hear_counts.columns = ["how_did_you_hear", "count"]

fig_hear = px.bar(
    hear_counts,
    x="count",
    y="how_did_you_hear",
    orientation="h",
    title="How Did You Hear About the Course?",
    text="count"
)

fig_hear.update_traces(textposition="outside")
fig_hear.update_layout(
    yaxis={'categoryorder': 'total ascending'}
)


# ------------------------
# Build Dashboard
# ------------------------

app = dash.Dash(__name__)

app.layout = html.Div(
    style={"width": "96%", "margin": "auto"},
    children=[
        html.H1("Course Survey Dashboard", style={"textAlign": "center"}),

        html.Div([
            dcc.Graph(figure=fig_age),
            dcc.Graph(figure=fig_gender),
        ], style={"display": "flex", "flexWrap": "wrap"}),


        html.Div([
            dcc.Graph(figure=fig_edu),
            dcc.Graph(figure=fig_working),
        ], style={"display": "flex", "flexWrap": "wrap"}),

        html.Div([
            dcc.Graph(figure=fig_python),
            dcc.Graph(figure=fig_git),
        ], style={"display": "flex", "flexWrap": "wrap"}),

        html.Div([
            dcc.Graph(figure=fig_linkedin),
            dcc.Graph(figure=fig_skills, style={"width": "100%"}) 
        ]),

        html.Div([
            dcc.Graph(figure=fig_hear),
            dcc.Graph(figure=fig_learning_goal),
        ], style={"display": "flex", "flexWrap": "wrap"})
    ]
)


if __name__ == "__main__":
    app.run(debug=True, port=8050)
