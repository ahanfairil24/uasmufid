from django import forms

class remufform(forms.Form):
    Buku = forms.CharField(max_length=50)
    Penulis = forms.CharField(max_length=40)
    Penerbit = forms.CharField(widget=forms.Textarea)
    Jumlah = forms.BooleanField()
