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
        help_text='Use a valid business or personal email address.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
            
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered in the Sky Registry.")
        return email

    def clean_password1(self):
        """Implement robust password complexity validation for security compliance."""
        password = self.cleaned_data.get("password1")
        if password:
            if len(password) < 10:
                raise forms.ValidationError("Password must be at least 10 characters long.")
            if not any(char.isdigit() for char in password):
                raise forms.ValidationError("Password must contain at least one digit.")
            if not any(not char.isalnum() for char in password):
                raise forms.ValidationError("Password must contain at least one special character.")
        return password
