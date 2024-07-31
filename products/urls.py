from django.urls import path

from products.views import ProductsListView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    # path('', products, name='index'),  # FBV
    path('', ProductsListView.as_view(), name='index'),  # CBV

    # path('category/<int:category_id>/', products, name='category'),  # FBV
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),  # CBV

    # path('page/<int:page_number>/', products, name='paginator'),  # FBV
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),  # CBV

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]