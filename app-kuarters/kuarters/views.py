from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from kuarters.forms import ContactForm

from kuarters.models import Pemohon

# Create your views here.


class HomeView(TemplateView):
    template_name = "kuarters/home.html"


class TerimakasihView(TemplateView):
    template_name = "kuarters/terima_kasih.html"


class PermohonanCreateView(CreateView):
    model = Pemohon
    # cipta templates guna nama model_form.html
    fields = "__all__"
    success_url = reverse_lazy("kuarters:terima_kasih")


class PermohonanListView(ListView):
    # cipta template gunakan nama model_list.html
    model = Pemohon
    queryset = Pemohon.objects.order_by("nama")
    context_object_name = "pemohon_list"


class PermohonanDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # template gunakan nama model_detail.html
    model = Pemohon
    # PK --> {{pemohon}}


class PermohonanUpdateView(UpdateView):
    # SHARE model_form.html --- PK
    model = Pemohon
    fields = "__all__"
    success_url = reverse_lazy("kuarters:senarai_pemohon")


class PermohonanDeleteView(DeleteView):
    # Form --> Confirm Delete button
    # default template name :
    # model_confirm_delete.html
    model = Pemohon

    success_url = reverse_lazy("kuarters:senarai_pemohon")


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "kuarters/contact.html"

    # URL dan bukan template.html
    success_url = reverse_lazy("kuarters:terima_kasih")

    # apa yang nak dibuat dengan form?

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
