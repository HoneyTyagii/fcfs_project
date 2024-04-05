# from fcfs_app.views import llm_view

# from django.urls import path
# from fcfs_app.views import fcfs_view

# urlpatterns = [
#     path('process/', fcfs_view, name='fcfs_process'),
# ]


# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from fcfs_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('process/', views.FcfsHandler.as_view()),
    path('', views.index_view),
]