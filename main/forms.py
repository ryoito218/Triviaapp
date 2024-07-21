from django import forms
from .models import Post
from datetime import datetime

class PostCreateForm(forms.ModelForm):

    content = forms.CharField(label="説明", widget=forms.Textarea, required=False)

    class Meta:
        model = Post
        fields = ['title', 'category', 'prefecture', 'content']

    # 必要ない可能性あり
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        obj = super(PostCreateForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj