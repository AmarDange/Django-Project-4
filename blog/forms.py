from django_summernote.widgets import SummernoteWidget
from .models import Post
from django import forms
from django.forms import ModelForm
from .models import Comment
from django import forms


class AddPostForm(forms.ModelForm):
    """
    Form to add a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "destinations",
            "content",
            "featured_image",
            "best_time",
            "ideal_duration",
        )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "author": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "hidden"
            }
        ),
        "destinations": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(
            attrs={
                "class": "form-control",
                "placeholder": "Add your content here",
            }
        ),
        "best_time": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Which season or months",
            }
        ),
        "ideal_duration": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ideal trip duration(days/week)",
            }
        ),
    }


class UpdatePostForm(forms.ModelForm):
    """
    Form to edit a blog post
    """

    class Meta:
        model = Post
        fields = (
            "title",
            "destinations",
            "content",
            "featured_image",
            "best_time",
            "ideal_duration",
        )

    widgets = {
        "title": forms.TextInput(attrs={"class": "form-control"}),
        "destinations": forms.Select(attrs={"class": "form-control"}),
        "content": SummernoteWidget(attrs={"class": "form-control"}),
        "best_time": forms.TextInput(attrs={"class": "form-control"}),
        "ideal_duration": forms.TextInput(attrs={"class": "form-control"}),
    }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body',)

class CommentForm(forms.ModelForm):
    """
    Form for post comment
    """
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "md-textarea form-control",
                "placeholder": "Please enter your comment here..",
                "rows": "6",
            }
        )
    )

    class Meta:
        # Choose fields to display from the Comment model
        model = Comment
        fields = ("body",)