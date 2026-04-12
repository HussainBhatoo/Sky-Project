from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class UserSignupForm(UserCreationForm):
    """
    Custom Signup Form that includes the mandatory email field 
    required by the Sky Engineering Portal specifications.
    """
    email = forms.EmailField(
        required=True,
        help_text='Enter a valid Sky corporate email address.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        """Ensure email is unique across the registry."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered in the Sky Registry.")
        return email
