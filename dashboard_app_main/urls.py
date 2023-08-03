from django.urls import path

from dashboard_app_main.views import IndexView, Dashboard, DashboardAxis,DashboardAxis2, DashboardPosition, RegisterView, LoginView, LogoutView, DownloadCSV,DownloadCSV2, DownloadCSVPosition, DownloadCSVTime, DashboardData,DashboardTemperature

app_name='dashboard_app_main'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('downloadcsvtime/', DownloadCSVTime.as_view(), name='download_csv_time'),
    path('downloadcsv/', DownloadCSV.as_view(), name='download_csv'),
    path('downloadcsv2/', DownloadCSV2.as_view(), name='download_csv2'),
    path('downloadcsvposition/', DownloadCSVPosition.as_view(), name='download_csv_position'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('dashboardaxis/',DashboardAxis.as_view(),name='dashboardaxis'),
    path('dashboardaxis2/',DashboardAxis2.as_view(),name='dashboardaxis2'),
    path('dashboardposition/',DashboardPosition.as_view(),name='dashboardposition'),
    path('dashboardtemperature/',DashboardTemperature.as_view(),name='dashboardtemperature'),
    path('dashboarddata/',DashboardData.as_view(),name='dashboarddata'),
]