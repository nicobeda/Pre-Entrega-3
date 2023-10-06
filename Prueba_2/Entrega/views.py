from django.shortcuts import render
from django.http import HttpResponse
from Entrega.forms import ClientesForm, ProveedoresForm, LocalesForm, BuscarCliente, BuscarLocal, BuscarProveedor
from .models import Clientes, Proveedores, Locales



# Create your views here.
def inicio(request):
    return render(request, "Entrega/index.html")

def proveedores(request):  
    if request.method == "POST":
        miformulario = ProveedoresForm(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            proveedor = Proveedores(nombre=informacion["nombre"], email=informacion["email"])
            proveedor.save()
            return render(request, "Entrega/index.html")
    else:   
        miformulario = ProveedoresForm()

    return render(request, "Entrega/proveedores.html", {"miFormulario": miformulario})

def clientes(request):  
    if request.method == "POST":
        miformulario = ClientesForm(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            cliente = Clientes(nombre=informacion["nombre"], edad=informacion["edad"])
            cliente.save()
            return render(request, "Entrega/index.html")
    else:
        miformulario = ClientesForm()

    return render(request, "Entrega/clientes.html", {"miFormulario": miformulario})

def     buscar_clie(request):
    if request.method == "POST":
        miformulario = BuscarCliente(request.POST)

        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            
            clientes = Clientes.objects.filter(nombre__icontains=informacion["nombre"])

            return render(request, "Entrega/resultado_cliente.html", {"clientes": clientes})
    else:
        miformulario = BuscarCliente()

    return render(request, "Entrega/buscar_cliente.html", {"miFormulario": miformulario})

def locales(request):  
    if request.method == "POST":
        miformulario = LocalesForm(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            local = Locales (calle=informacion["calle"], altura=informacion["altura"])
            local.save()
            return render(request, "Entrega/index.html")
    else:
        miformulario = LocalesForm()

    return render(request, "Entrega/locales.html", {"miFormulario": miformulario})

