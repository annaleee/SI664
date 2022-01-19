from django.forms import ModelForm
from solo.models import Solo


# Create the form class.
class BreedForm(ModelForm):
    class Meta:
        model = Solo
        fields = '__all__'