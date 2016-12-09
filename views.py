
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render
from django.views import View



# def function_view(request):
#     return HttpResponse ('response from function view')

# class ExampleClassBased(View):
#     def get(selfsekf, request):
#         return HttpResponse('response from class based view')
#
# class ExampleView(View):
#     def get(self, request):
#         return render (request, 'example.html', {'my_variable' : 'Этот текст подставится вместо переменной'})
#
# class Basee(View):
#     def get(self, request):
#         return render(request, 'bootstrap.html')

class OrdersView(View):
    orders = [
        {'title': 'Абрикос', 'id': 1,'text': 'Вкуснейший поставщик необходимого человеку бета – каротина.'},
        {'title': 'Авокадо', 'id': 2, 'text': 'Этот фрукт богат множеством полезных витаминов: А, В, С, D.'},
        {'title': 'Айва', 'id': 3, 'text': 'Родиной этого фрукта является Кавказ.'},
        {'title': 'Ананас', 'id': 4, 'text': 'Его употребляют при тромбофлебитах, простуде, заболеваниях суставов.'},
        {'title': 'Апельсин', 'id': 5, 'text': 'Это вечнозеленое плодовое дерево.'},
        {'title': 'Арбуз', 'id': 6, 'text': 'Это однолетнее травянистое растение, относиться к семейству тыквенных.'},
        {'title': 'Бананы', 'id': 7, 'text': 'Этот заграничный фрукт прибыл к нам из Юго-Восточной Азии.'},
        {'title': 'Гранат', 'id': 8, 'text': 'Это небольшое дерево или кустарник, высотой не больше 6 метров. '},
        {'title': 'Груша', 'id': 9, 'text': 'Это дерево семейства розовые.'},
        {'title': 'Дыня', 'id': 10, 'text': 'Это однодомное травянистое растение, с плодом круглой или овальной формы. '},
        {'title': 'Инжир', 'id': 11, 'text': 'Это дерево высотой до 12 метров.'},
    ]
    def get(self, request):
        data = {
            'orders': OrdersView.orders,
            'count' : len(OrdersView.orders),
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {

            'order': {
                'id': id,
                'title': OrdersView.orders[int(id)-1].get('title'),
                'text': OrdersView.orders[int(id)-1].get('text'),
            }
        }
        return render(request, 'order.html', data)

