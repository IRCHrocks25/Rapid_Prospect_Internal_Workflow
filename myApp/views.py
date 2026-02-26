from django.shortcuts import render

def home(request):
    return render(request, 'cheat_sheet.html')

def sales_pitch(request):
    return render(request, 'sales_pitch.html')
