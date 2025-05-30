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
        {"name": "Jai", "username": "@jaikumar", "body": "I've never seen anything like this before. It's amazing. I love it.", "photo": "jai.jpg"},
        {"name": "Roshan", "username": "@roshan", "body": "I don't know what to say. I'm speechless. This is amazing.", "photo": "roshan.jpg"},
        {"name": "Shreeya", "username": "@shreeya", "body": "The animation is slick. Beautiful job.", "photo": "shreeya.jpg"},
        {"name": "Raj", "username": "@rajkumar", "body": "I'm at a loss for words. This is amazing. I love it.", "photo": "raj.jpg"},
        {"name": "Parth", "username": "@parth", "body": "So smooth and elegant. Just wow!", "photo": "parth.jpg"},
        {"name": "Ankita", "username": "@ankita", "body": "I could watch this scroll all day.", "photo": "ankita.jpg"},
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
