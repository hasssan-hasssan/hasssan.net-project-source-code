from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""
        self.fields['email'].label = ""
        self.fields['name'].label = ""

    class Meta:
        model = Comment
        fields = ['body', 'email', 'name']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'دیدگاه شما....',
                'class': 'border-secondary',
                'class': 'bg-light',

            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'border-secondary',
                'class': 'bg-light',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'border-secondary',
                'class': 'bg-light',

            })
        }


class ShareForm(forms.Form):
    name = forms.CharField(label=False, max_length=25, widget=forms.TextInput(
        attrs={
            'placeholder': 'نام و نام خانوادگی...',
            'class': 'border-secondary',
            'class': 'bg-light',
        }))
    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'placeholder': 'ایمیل خودم...',
        'class': 'border-secondary',
        'class': 'bg-light',
    }))
    to = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'placeholder': 'ایمیل دوستم...',
        'class': 'border-secondary',
        'class': 'bg-light',
    }))
    comments = forms.CharField(label=False, required=False, widget=forms.Textarea(attrs={
        'placeholder': 'یادداشت من درباره این پست برای دوستم...',
        'class': 'border-secondary',
        'class': 'bg-light',
    }))


class SearchForm(forms.Form):
    data = forms.CharField(label=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'کلمه مورد نظر رو وارد کنید....',
            'class': 'mt-2',
        }
    ))