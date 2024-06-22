from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','description','demo_link','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)  

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})


        #need to update every field
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Enter Here'})
        # self.fields['description'].widget.attrs.update({'class':'input' })