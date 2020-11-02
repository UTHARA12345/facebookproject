from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_fb/', FbAddView.as_view(), name='add_fb'),
    path('edit_fb/<str:id>/', FbUpdateView.as_view(), name='edit_fb'),
    path('details_fb/<str:id>', FbDetails.as_view(), name='details_fb'),
    path('delete_fb/<str:id>', DeleteFb.as_view(), name='delete_fb'),

]