from django.urls import path,include
from .views import addproductView,deleteView,editView,editsaveView
app_name='app'

urlpatterns = [
    path('product/',addproductView,name='addproduct_url'),
    path('delete/',deleteView,name='delete_url'),
    path('edit/',editView,name='edit_url'),
    path('editsave/',editsaveView,name='editsave_url'),

]
