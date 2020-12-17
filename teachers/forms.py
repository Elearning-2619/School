from django import forms
from .models import Teacher

class TeacherCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TeacherCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Teacher
        fields = ['name', 'image', 'email', 'grade', 'gender']