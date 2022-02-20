from django.urls import path
from rental import views

app_name = 'rental'


urlpatterns = [
    path('students', views.StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/purchases', views.StudentPurchaseView.as_view(), name='student-purchase'),
    
    path('tickets', views.TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>', views.TicketDetailView.as_view(), name='ticket-detail'),
    
    path('purchases', views.PurchaseListView.as_view(), name='purchase-list'),
]
