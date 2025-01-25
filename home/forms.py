from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={"class":"w-full p-3 focus:outline-none","placeholder":"Entrer votre nom"}))
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(attrs={"class":"w-full p-3 focus:outline-none","placeholder":"Entrer votre e-mail"}))
    message = forms.CharField(label="Message", required=True,widget=forms.Textarea(attrs={"rows":"2","class":"w-full p-3 focus:outline-none","placeholder":"Votre message"}))
