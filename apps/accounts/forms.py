from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from apps.core.forms import AccessibleFormMixin


class EmailAuthenticationForm(AccessibleFormMixin, AuthenticationForm):
    """Login form for staff/clinician accounts. Django names the login field `username`."""

    username = forms.EmailField(
        label="Email address",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "autofocus": True}),
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password"].widget.attrs["autocomplete"] = "current-password"
