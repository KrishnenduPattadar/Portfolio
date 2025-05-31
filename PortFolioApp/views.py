from django.shortcuts import render, redirect
from .forms import InquiryForm
from django.contrib import messages

def home(request):
    icons = [
        "git", "github", "django", "python", "html5", "bootstrap", "tailwindcss",
        "css3", "javascript", "postgresql", "git", "sqlite", "linkedin"
    ]

    # ✨ Add your reviews here
    reviews = [
        {"name": "Jai", "username": "@jaikumar", "body": "I'm working with Krishnendu — he's one of the most dedicated and focused people I’ve ever met.", "photo": "jai.jpg"},
        {"name": "Roshan", "username": "@roshan", "body": "Krishnendu handles the backend brilliantly, but what really surprised me is his eye for design.", "photo": "roshan.jpg"},
        {"name": "Shreeya", "username": "@shreeya", "body": "His creativity is unmatched. He blends technical skill with stunning design ideas effortlessly.", "photo": "shreeya.jpg"},
        {"name": "Raj", "username": "@rajkumar", "body": "Working with Krishnendu is inspiring. He’s reliable, efficient, and always full of smart solutions.", "photo": "raj.jpg"},
        {"name": "Parth", "username": "@parth", "body": "Not only a great backend developer but also a surprisingly strong sense. Total package.", "photo": "parth.jpg"},
        {"name": "Ankita", "username": "@ankita", "body": "Krishnendu is a rare talent. Detail-oriented, creative, and super passionate about his work.", "photo": "ankita.jpg"},
    ]

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error. Please fix it below.")
    else:
        form = InquiryForm()

    context = {
        "icons": icons,
        "form": form,
        "reviews": reviews,  # 🔁 Added this
    }
    return render(request, "PortFolioApp/base.html", context)
