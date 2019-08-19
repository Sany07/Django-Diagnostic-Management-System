from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    email.widget.attrs.update({'class' : 'contact_input'})
    subject = forms.CharField(max_length=100)
    subject.widget.attrs.update({'class' : 'contact_input'})
    message = forms.CharField(widget = forms.Textarea)
    message.widget.attrs.update({'class' : 'contact_textarea contact_input'})
    attach = forms.Field(widget = forms.FileInput)

  #name = forms.CharField(label='name ', widget=forms.TextInput(attrs={'placeholder': 'name '}))