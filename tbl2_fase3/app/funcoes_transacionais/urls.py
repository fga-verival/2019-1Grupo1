from django.urls import path

from . import views

urlpatterns = [
    path('', views.FTransacionalList.as_view(), name='ftrans_list'),
    path('view/<int:pk>', views.FTransacionalView.as_view(), name='ftrans_view'),
    path('new', views.FTransacionalCreate.as_view(), name='ftrans_new'),
    path('edit/<int:pk>', views.FTransacionalUpdate.as_view(), name='ftrans_edit'),
    path('delete/<int:pk>', views.FTransacionalDelete.as_view(), name='ftrans_delete'),
]