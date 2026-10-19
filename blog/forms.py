from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields =['title', 'content', 'category']
        fields = '__all__' # 全部表示したい時
