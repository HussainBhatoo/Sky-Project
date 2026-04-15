from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class UserSignupForm(UserCreationForm):
    """
    Custom Signup Form that includes the mandatory email field 
    required by the Sky Engineering Portal specifications.
    """
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    email = forms.EmailField(
        required=True,
        help_text='Must be an official @sky.com or @sky.uk email'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def clean_email(self):
        """Ensure email is unique across the registry and has a valid corporate domain."""
        email = self.cleaned_data.get('email')
        
        if not email.endswith('@sky.com') and not email.endswith('@sky.uk'):
            raise forms.ValidationError("Please use a valid Sky corporate email address (@sky.com or @sky.uk).")
            
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered in the Sky Registry.")
        return email
