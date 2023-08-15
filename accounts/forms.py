from djagno.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChargerForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        field = ("email", 'username')

class CustomUserChargerForm(UserChargerForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')