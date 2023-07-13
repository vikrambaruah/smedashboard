from django.urls import path

from dashboard_app_main.views import IndexView, Dashboard, DashboardAxis, DashboardPosition, RegisterView, LoginView, LogoutView, DownloadCSV, DownloadCSVPosition, DownloadCSVTime

app_name='dashboard_app_main'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('downloadcsvtime/', DownloadCSVTime.as_view(), name='download_csv_time'),
    path('downloadcsv/', DownloadCSV.as_view(), name='download_csv'),
    path('downloadcsvposition/', DownloadCSVPosition.as_view(), name='download_csv_position'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('dashboardaxis/',DashboardAxis.as_view(),name='dashboardaxis'),
    path('dashboardposition/',DashboardPosition.as_view(),name='dashboardposition'),
    
]