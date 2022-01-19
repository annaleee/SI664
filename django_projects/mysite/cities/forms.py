from django.forms import ModelForm
from cities.models import State


# Create the form class.
class StateForm(ModelForm):
    class Meta:
        model = State
        fields = '__all__'