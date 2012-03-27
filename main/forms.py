from django.forms import ModelForm

from wdys.main.models import CityImage
    
class CityImageForm(ModelForm):
    city = forms.ModelChoiceField()
        
class SceneImageForm(ModelForm):
    class Meta:
        model = SceneImage        
    
class SceneImage(CityImage):
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tag)
    date = models.DateField()