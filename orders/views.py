from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


# class OrderCreateView(CreateView):
#     template_name = 'orders/order-create.html'
class OrderCreateView(TemplateView):
    template_name = 'orders/order-create.html'
