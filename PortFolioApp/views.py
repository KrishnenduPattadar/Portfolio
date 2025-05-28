from django.shortcuts import render

def home(request):
    return render(request, 'PortFolioApp/base.html')  # Or change to home.html later
def InquiryView(request):
    return render(request, 'PortFolioApp/inquiry.html')  # Or change to inquiry.html later
