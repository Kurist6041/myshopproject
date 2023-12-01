from django.forms import ModelForm
from .models import ItemPost

class ItemPostForm(ModelForm):
    
    
    class Meta:
        
        
        model = ItemPost
        fields = ['image','name','description','price']