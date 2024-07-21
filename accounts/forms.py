from django import forms
from .models import Profile
from datetime import datetime

class EditProfileForm(forms.ModelForm):

    bio = forms.CharField(label="自己紹介", widget=forms.Textarea, required=False)

    class Meta:
        model = Profile
        fields = ["username", "bio"]
    
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(EditProfileForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj