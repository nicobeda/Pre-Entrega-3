from django import forms

class ClientesForm(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()

class LocalesForm(forms.Form):
    calle= forms.CharField()
    altura= forms.IntegerField()

class ProveedoresForm(forms.Form):
    nombre= forms.CharField()
    email= forms.EmailField()

class BuscarCliente(forms.Form):
    nombre= forms.CharField()
    edad= forms.IntegerField()

class BuscarLocal(forms.Form):
    calle= forms.CharField()
    altura= forms.IntegerField()

class BuscarProveedor(forms.Form):
    nombre= forms.CharField()
    email= forms.EmailField()

        