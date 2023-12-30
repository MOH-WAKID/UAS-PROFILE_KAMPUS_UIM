from django.shortcuts import render

def index(request):
    my_data = {'key1': 'value1', 'key2': 'value2'}
    return render(request, 'index.html', {'my_data': my_data})

def sejarahkampus(request):
    return render(request, 'sejarahkampus.html') 

def visimisi(request):
    return render(request, 'visimisi.html')

def hubungikami(request):
    return render(request, 'hubungikami.html')

def fakultasteknik(request):
    return render(request, 'fakultasteknik.html')

def fakultasmipa(request):
    return render(request, 'fakultasmipa.html')
