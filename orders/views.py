import uuid
from http import HTTPStatus

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from orders.forms import OrderForm


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
