from django.shortcuts import render
def home(request):
    icons = [
        "git","github", "django", "python", "html5", "bootstrap", "tailwindcss",
        "css3", "javascript", "postgresql", "git", "sqlite"
    ]
    return render(request, "PortFolioApp/base.html", {"icons": icons})
def about(request):
    email = "nurulhuda@gmail.com"
    return render(request, "PortFolioApp/base.html", {"email": email})