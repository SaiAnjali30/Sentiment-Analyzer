from django.shortcuts import render
from textblob import TextBlob

def home(request):
    sentiment = None
    score = 0

    if request.method == "POST":
        text = request.POST.get("text")

        analysis = TextBlob(text)
        score = analysis.sentiment.polarity

        if score > 0:
            sentiment = "Positive 😊"
        elif score < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render(request, "index.html", {
        "sentiment": sentiment,
        "score": score
    })