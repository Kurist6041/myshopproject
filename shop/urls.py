from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    
    path('',views.IndexView.as_view(),name='index'),
    
    path('post/', views.CreateItemView.as_view(), name= 'post'),
    
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    path('mypage/', views.MypageView.as_view(), name= 'mypage'),
    
    path('item_list/', views.ItemListView.as_view(), name='item_list'),
    
    path('item/success/', views.BuySuccessView.as_view(), name='item_success'),
    

    path('user-list/<int:user>',
         views.UserView.as_view(),
         name= 'user-list'),
    
   
    
]
