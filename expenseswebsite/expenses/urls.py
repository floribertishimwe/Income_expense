from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    
    path('',views.index, name="expenses"),
    path('add-expense',views.add_expense, name="add_expenses"),
    path('edit-expense/<int:id>', views.edit_expense, name="edit_expense"),
    path('delete-expense/<int:id>', views.delete_expense, name="delete_expense"),
    path('search-expenses', csrf_exempt(views.search_expenses), name="search-expenses"),
    path('expense_category_summary',views.expense_category_summary,name="expense_category_summary"),
    path('expenses_stats',views.stats_View,name="stats"),
    path('export_csv',views.export_csv,name="export-csv"),   
    path('export_excel',views.export_excel,name="export-excel"), 
    path('export_pdf',views.export_pdf,name="export-pdf"),
]
