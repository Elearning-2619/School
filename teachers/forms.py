from django import forms
from .models import Teacher

class TeacherCreationForm(forms.ModelForm):

    # grade = forms.IntegerField(widget=forms.TextInput(attrs={'value': ""}))
    def __init__(self, *args, **kwargs):
        super(TeacherCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Teacher
        fields = ['name', 'email', 'image', 'gender', 'grade']