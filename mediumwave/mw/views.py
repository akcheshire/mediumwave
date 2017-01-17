from django.shortcuts import render

def freq_list(request):
        return render(request, 'mw/freq_list.html', {})
