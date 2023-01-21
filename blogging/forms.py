from django.forms import ModelForm
from .models import Blog
from django import forms
from .models import Tags,Blog
#create_form


#submit_form

class SubmitForm(ModelForm):

    class Meta:
        model =Blog
        fields =['blog_title','desc','blog_image','blog','tags']
    
    widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    