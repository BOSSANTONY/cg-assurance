from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Profile,
    QuoteRequest,
    Claim,
    ContactMessage
)


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100
    )

    last_name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=100
    )

    last_name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    class Meta:
        model = Profile

        fields = [
            "phone",
            "address",
            "city",
            "country",
            "date_of_birth",
        ]


class QuoteForm(forms.ModelForm):

    class Meta:
        model = QuoteRequest

        fields = [
            "product",
            "message",
        ]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Expliquez votre besoin..."
                }
            )
        }


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim

        fields = [
            "policy",
            "title",
            "description",
            "incident_date",
            "location",
            "amount_requested",
        ]

        widgets = {
            "incident_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6
                }
            )
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 6
                }
            )
        }