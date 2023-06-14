from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from todo import views

urlpatterns = [

    path('', views.index, name="todo"),

    path('del/<str:item_id>', views.remove, name="del"),

    path('update_is_done/', views.update_is_done_field, name="update_is_done"),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
