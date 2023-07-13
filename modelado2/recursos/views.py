from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url_login = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/GetEmisor")
    emisores = url_login.json()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        emisor = request.POST['emisor']

        #Verificar ingreso de usuario que no ingrese letras
        if username.isalpha() == True:
            return render(request, 'index.html', {
                'error': "Usuario o contraseña incorrectos",
                'emisores': emisores,
            })

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Usuarios?usuario="+
                               username+"&password="+password)
            data = url.json()
        except:
            return render(request, 'index.html', {
                'error': "Usuario o contraseña incorrectos",
                'emisores': emisor,
            })

        if data[0]['OBSERVACION'] == "INGRESO EXITOSO":
            if emisor == data[0]['NOMBREEMISOR'].strip():
                url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
                data = url.json()

                return render(request, 'recursos/centrocostos.html',{
                    'data': data,
                })   
            else:
                return render(request, 'index.html', {
                    'error': "Emisor mal registrado",
                    'emisores': emisor,
                })
    else:
        return render(request, 'recursos/index.html',{
            'emisores': emisores,
        })

def centrocostos(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSearch?descripcioncentrocostos="+descripcion)
        data = url.json()

        codigo = data[0]['Codigo']
        descripcionmostrar = data[0]['NombreCentroCostos']
        
        return render(request, 'recursos/busqueda.html',{
            'codigo': codigo,
            'descripcion': descripcionmostrar,
        })

    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    data = url.json()

    return render(request, 'recursos/centrocostos.html',{
        'data': data,
    })

def pagTipoTrabajador(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoTrabajador")
    data = url.json()

    return render(request, 'recursos/tipoTrabajador.html',{
        'data': data,
    })

def pagNivelSalarial(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/NivelSalarial")
    data = url.json()

    return render(request, 'recursos/nivelSalarial.html',{
        'data': data,
    })

def pagCategoriaOcupacional(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CategoriaOcupacional")
    data = url.json()

    return render(request, 'recursos/categoriaOcupacional.html',{
        'data': data,
    })

def pagTipoCese(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoCese")
    data = url.json()

    return render(request, 'recursos/tipoCese.html',{
        'data': data,
    })

def pagTipoContrato(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoContrato")
    data = url.json()

    return render(request, 'recursos/tipoContrato.html',{
        'data': data,
    })

def pagEstadoTrabajador(request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/EstadoTrabajador")
    data = url.json()

    return render(request, 'recursos/estadotrabajador.html',{
        'data': data,
    })
