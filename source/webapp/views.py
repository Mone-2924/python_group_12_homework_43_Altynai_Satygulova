from django.shortcuts import render


# Create your views here.

def index_view(request):
    context = {}
    return render(request, "index.html", context)

def article_create_view(request):
    icon = ''
    if request.method == 'GET':
        return render(request, "index.html")
    elif request.method == 'POST':
        context = {
            'number': request.POST.get('number'),
            'number_two': request.POST.get('number_two'),
            'sum': request.POST.get('sum'),
        }

        if context['sum'] == 'add':
            context['icon'] = '+'
            result = int(context['number']) + int(context['number_two'])
            context['result'] = result
        elif context['sum'] == 'subtract':
            context['icon'] = '-'
            result = int(context['number']) - int(context['number_two'])
            context['result'] = result
        elif context['sum'] == 'multiply':
            context['icon'] = '*'
            result = int(context['number']) * int(context['number_two'])
            context['result'] = result
        elif context['sum'] == 'divide':
            context['icon'] = '/'
            result = int(context['number']) / int(context['number_two'])
            context['result'] = result
        print(context)
        return render(request, 'index.html', context)
