from django.contrib import admin
from django.urls import path
from EmployeeApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.Employee_create),
    path('id/<int:emp_id>/', views.Employee_id),
    path('update/', views.Employee_update),
    path('pagination/', views.EmployeeListPagination.as_view()),
    ]
    # path('pagewise/', views.page_view),