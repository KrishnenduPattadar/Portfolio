from django.shortcuts import render, redirect
from .forms import InquiryForm
from django.contrib import messages

def home(request):
    icons = [
        "git", "github", "django", "python", "html5", "bootstrap", "tailwindcss",
        "css3", "javascript", "postgresql", "git", "sqlite", "linkedin"
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

    context = {"icons": icons, "form": form}
    return render(request, "PortFolioApp/base.html", context)
