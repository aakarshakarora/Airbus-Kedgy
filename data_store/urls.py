from django.urls import path, include

from data_store import views

urlpatterns = [
    path('login/', views.login_index, name="login"),
    path('login_view/', views.login_view, name="login_view"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('operator_fab_form_res/', views.operator_fab_form_res, name="operator_fab_form_res"),
    path('operator_subassembly_form_res/', views.operator_subassembly_form_res, name="operator_subassembly_form_res"),
    path('operator_assembly_form_res/', views.operator_assembly_form_res, name="operator_assembly_form_res"),
    path('approved_request_status/', views.approved_request_status, name="approved_request_status"),
]
