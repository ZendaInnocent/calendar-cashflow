import logging

from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from accounts import forms

logger = logging.getLogger(__name__)


class UserRegistrationView(CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         logger.info(
    #             "New signup for email=%s through SignupView", email
    #         )
    #         form.send_email()
    #     return super().form_valid(form)
