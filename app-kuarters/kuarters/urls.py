from unicodedata import name
from django.urls import path
from .views import (
    HomeView,
    TerimakasihView,
    ContactFormView,
    PermohonanCreateView,
    PermohonanListView,
    PermohonanDetailView,
    PermohonanUpdateView,
    PermohonanDeleteView,
)


app_name = "kuarters"
# domain.com/kuarters/pemohon_detail/1
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("terima_kasih/", TerimakasihView.as_view(), name="terima_kasih"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path(
        "create_permohonan/", PermohonanCreateView.as_view(), name="create_permohonan"
    ),
    path("senarai_pemohon", PermohonanListView.as_view(), name="senarai_pemohon"),
    path(
        "pemohon_detail/<int:pk>", PermohonanDetailView.as_view(), name="pemohon_detail"
    ),
    path(
        "update_pemohon/<int:pk>", PermohonanUpdateView.as_view(), name="update_pemohon"
    ),
    path(
        "delete_pemohon/<int:pk>", PermohonanDeleteView.as_view(), name="delete_pemohon"
    ),
]
