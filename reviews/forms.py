from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=20, error_messages={
        "required": "Your name must not be empty",
        "max_length": "please enter a shorter name!"
    })

