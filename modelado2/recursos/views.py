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
            return render(request, 'recursos/index.html', {
                'error': "Usuario o contraseña incorrectos",
                'emisores': emisores,
            })

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Usuarios?usuario="+
                               username+"&password="+password)
            data = url.json()
        except:
            return render(request, 'recursos/index.html', {
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
                return render(request, 'recursos/index.html', {
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
    
def pagCentroCostos(request):
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

#recursos/
def agregarCentroCostos(request):
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        codigo = request.POST['codigo']
        
        requests.post("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosInsert?descripcioncentrocostos="+descripcion+"&codigocentrocostos="+codigo)
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()

        return render(request, 'recursos/centrocostos.html',{
            'data': data,
        })
    else:
        return render(request, 'recursos/agregarCentroCostos.html')

def eliminarCentroCostos(request, id, descripcion):
    if request.method == 'POST':
        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosDelete?codigocentrocostos="+id+"&descripcioncentrocostos="+descripcion)
        except:
            return render(request, 'recursos/centrocostos.html', {
                'message': "Error al eliminar el centro de costos"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'recursos/centrocostos.html',{
                'data': data,
            })
    else:
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'recursos/centrocostos.html',{
                'data': data,
            })
            
def editCentroCostos(request, id):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
    data = url.json()

    for datos in data:
        if datos['Codigo'] == int(id):
            data = datos
    
    return render(request, 'recursos/editCentroCostos.html',{
        'data': data,
    })

def edit(request, id):
    if request.method == "POST":
        descripcion = request.POST['descripcion']

        try:
            url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosUpdate?codigocentrocostos="+id+"&descripcioncentrocostos="+descripcion)

        except:
            return render(request, 'exceptiondentro.html', {
                'message': "Error al editar el centro de costos"
            })
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'recursos/centrocostos.html',{
                'data': data,
            })
    else:
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/CentroCostosSelect")
        data = url.json()
        return render(request, 'recursos/centrocostos.html',{
                'data': data,
            })
    

##Movimiento de plantilla
def PagMovimientoPlanilla (request):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
    data = url.json()

    ##Filtrar por prioridad
    data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)
    
    return render(request, 'movimientoplanilla.html',{
        'data': data,
    })

def PagMovimientoPlanillaSearch (request):
    if request.method == "POST":
        ## buscar por Concepto
        concepto = request.POST['Concepto']
        ##Quitar los espacios entre palabras
        concepto = concepto.replace(" ", "&")

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSearch?Concepto="+concepto)
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)
        
        return render(request, 'busquedaMovimientoPlantilla.html',{
            'data': data,
        })
    
def eliminarMovimientoPlanilla (request, id):
    if request.method == 'POST':

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        # buscar por Concepto
        for datos in data:
            if datos['CodigoConcepto'] == int(id):
                concepto = datos['Concepto']

        url = requests.delete("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimeintoPlanillaDelete?codigomovimiento="+id+
                            "&descripcionomovimiento="+concepto)
        
        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
                'data': data,
            })

    
def PagMovimientoPlanillaEdit (request, id):
    url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
    data = url.json()

    for datos in data:
        if datos['CodigoConcepto'] == int(id):
            data = datos

    ##Sacar tipos de operaciones
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoOperacion")
    data2 = url2.json()

    ##Sacar movimiento excepcion
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion1y2")
    data3 = url3.json()

    #Sacar movimiento de excepcion 3
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion3")
    data4 = url4.json()

    ##Sacar traba aplica a iess
    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabaAfectaIESS")
    data5 = url5.json()

    ##Sacar afecta impuesto a la renta
    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabAfecImpuestoRenta")
    data6 = url6.json()
    
    return render(request, 'editMovimientoPlanilla.html',{
        'datos': data,
        'operacion': data2,
        'excepcion': data3,
        'excepcion3': data4,
        'traba': data5,
        'afecta': data6,
    })

def editMovimientoPlantilla (request, id):
    if request.method == "POST":
        Conceptos = request.POST['Conceptos']
        Prioridad = request.POST['Prioridad']
        TipoOperacion = request.POST['TipoOperacion']
        Cuenta1 = request.POST['Cuenta1']
        Cuenta2 = request.POST['Cuenta2']
        Cuenta3 = request.POST['Cuenta3']
        Cuenta4 = request.POST['Cuenta4']
        MovimientoExcepcion1 = request.POST['MovimientoExcepcion1']
        MovimientoExcepcion2 = request.POST['MovimientoExcepcion2']
        MovimientoExcepcion3 = request.POST['MovimientoExcepcion3']
        Traba_Aplica_iess = request.POST['Traba_Aplica_iess']
        Traba_Proyecto_imp_renta = request.POST['Traba_Proyecto_imp_renta']
        Aplica_Proy_Renta = request.POST['Aplica_Proy_Renta']
        Empresa_Afecta_Iess = request.POST['Empresa_Afecta_Iess']

        try:
            requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaUpdate?codigoplanilla="+id+"&conceptos="+Conceptos+"&prioridad="+Prioridad+"&tipooperacion="+TipoOperacion+"&cuenta1="+Cuenta1+"&cuenta2="+Cuenta2+"&cuenta3="+Cuenta3+"&cuenta4="+Cuenta4+"&MovimientoExcepcion1="+MovimientoExcepcion1+"&MovimientoExcepcion2="+MovimientoExcepcion2+"&MovimientoExcepcion3="+MovimientoExcepcion3+"&Traba_Aplica_iess="+Traba_Aplica_iess+"&Traba_Proyecto_imp_renta="+Traba_Proyecto_imp_renta+"&Aplica_Proy_Renta="+Aplica_Proy_Renta+"&Empresa_Afecta_Iess="+Empresa_Afecta_Iess)
        except:
            return render(request, 'exceptiondentro.html',{
                'message': 'Error al actualizar el movimiento de planilla',
            })

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
            'data': data,
        })
    
def PagMovimientoPlanillaCreate (request):
    ##Sacar tipos de operaciones
    url2 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TipoOperacion")
    data2 = url2.json()

    ##Sacar movimiento excepcion
    url3 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion1y2")
    data3 = url3.json()

    #Sacar movimiento de excepcion 3
    url4 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientosExcepcion3")
    data4 = url4.json()

    ##Sacar traba aplica a iess
    url5 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabaAfectaIESS")
    data5 = url5.json()

    ##Sacar afecta impuesto a la renta
    url6 = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/TrabAfecImpuestoRenta")
    data6 = url6.json()

    return render(request, 'agregarMovimiento.html',{
        'operacion': data2,
        'excepcion': data3,
        'excepcion3': data4,
        'traba': data5,
        'afecta': data6,
    })

def pushMovimientoPlantilla(request):
    if request.method == "POST":
        Conceptos = request.POST['Conceptos']
        Prioridad = request.POST['Prioridad']
        TipoOperacion = request.POST['TipoOperacion']
        Cuenta1 = request.POST['Cuenta1']
        Cuenta2 = request.POST['Cuenta2']
        Cuenta3 = request.POST['Cuenta3']
        Cuenta4 = request.POST['Cuenta4']
        MovimientoExcepcion1 = request.POST['MovimientoExcepcion1']
        MovimientoExcepcion2 = request.POST['MovimientoExcepcion2']
        MovimientoExcepcion3 = request.POST['MovimientoExcepcion3']
        Traba_Aplica_iess = request.POST['Traba_Aplica_iess']
        Traba_Proyecto_imp_renta = request.POST['Traba_Proyecto_imp_renta']
        Aplica_Proy_Renta = request.POST['Aplica_Proy_Renta']
        Empresa_Afecta_Iess = request.POST['Empresa_Afecta_Iess']

        Traba_Aplica_iess = Traba_Aplica_iess + " Aplica"

        if Traba_Proyecto_imp_renta == "Aplica":
            Traba_Proyecto_imp_renta = "Si Aplica"

        try:
            requests.post("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaInsert?conceptos="+Conceptos+
                         "&prioridad="+Prioridad+"&tipooperacion="+TipoOperacion+"&cuenta1="+Cuenta1+"&cuenta2="+Cuenta2+
                         "&cuenta3="+Cuenta3+"&cuenta4="+Cuenta4+"&MovimientoExcepcion1="+MovimientoExcepcion1+
                         "&MovimientoExcepcion2="+MovimientoExcepcion2+"&MovimientoExcepcion3="+MovimientoExcepcion3+
                         "&Traba_Aplica_iess="+Traba_Aplica_iess+"&Traba_Proyecto_imp_renta="+Traba_Proyecto_imp_renta+
                         "&Aplica_Proy_Renta="+Aplica_Proy_Renta+"&Empresa_Afecta_Iess="+Empresa_Afecta_Iess)
        except:
            return render(request, 'exceptiondentro.html',{
                'message': 'Error al insertar el movimiento de planilla',
            })

        url = requests.get("http://apiservicios.ecuasolmovsa.com:3009/api/Varios/MovimientoPlanillaSelect")
        data = url.json()

        ##Filtrar por prioridad
        data = sorted(data, key=lambda k: k['Prioridad'], reverse=True)

        return render(request, 'movimientoplanilla.html',{
            'data': data,
        }) 