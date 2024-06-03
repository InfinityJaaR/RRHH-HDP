import csv
from io import TextIOWrapper
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Area, Cargo, Empleado, Departamento, Municipio, Pago, Asistencia, Permiso
from .froms import CargoForm, AreaForm, CustomUserCreationForm, CSVUploadForm
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

# def index(request):
#     return render(request, "login.html")

def GestionarEmpleadosView(request, id):
    empleado = get_object_or_404(Empleado, carnet=id)
    return render(request, 'EMgestionarEmpleado.html', {'empleado': empleado})

def AdministrarCargoView(request):
    cargos=Cargo.objects.all()
    data={
        'cargos': cargos
    }
    return render(request, "ADadministrarCargo.html", data)

def GestionarPermisosView(request, id):
    empleado = get_object_or_404(Empleado, carnet=id) 

    permisos = Permiso.objects.filter(carnet=empleado)
    
    return render(request, 'EMgestionarPermisos.html', {'permisos': permisos, 'empleado':empleado})

def SolicitarPermisoView(request, id):
    if request.method == 'POST':
        empleado = get_object_or_404(Empleado, carnet=id)
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        razon = request.POST.get('razon')

        # Crear una nueva instancia de Permiso
        permiso = Permiso(
            #carnet=request.user.empleado,  # Asocia el permiso al empleado logueado
            carnet=empleado,
            fechainicio=fecha_inicio,
            fechafinal=fecha_fin,
            justificacion=razon,
            estado = '3'# Estado inicial del permiso
            #fecha_solicitud=timezone.now()  # Fecha en la que se solicita el permiso
        )
        permiso.save()
        messages.success(request, "Se ha guardado su solicitud")

        return redirect("{% url 'gestionar_permisosEM' user.username %}")  # Redirige a la página de gestión de permisos
    return render(request, 'EMsolicitarPermiso.html')

def GestionarPagoEMView(request, id):
    empleado = get_object_or_404(Empleado, carnet=id)
    fecha_pago = request.GET.get('fechaPago')
    if fecha_pago:
        pagos = Pago.objects.filter(carnet=empleado, fechapago=fecha_pago)
    else:
        pagos = Pago.objects.filter(carnet=empleado)
    return render(request, 'EMgestionarPago.html', {'pagos': pagos, 'empleado': empleado})


def CrearPagoView(request):
    return render(request, "ADcrearPagos.html")

def HomeView(request):
    return render(request, "inicio.html")

#Pantallas de Eduardo


def AdministrarAreaView(request):
    areas=Area.objects.all()
    data={
        'areas':areas
    }
    return render(request, "ADadministrarArea.html", data)

def GestionarAreaView(request):
    data={
        'form': AreaForm()
    }
    if request.method == 'POST':
        formulaio= AreaForm(data=request.POST)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarAreaView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarArea.html", data)

def GestionarCargoView(request):
    data={
        'form': CargoForm()
    }
    if request.method == 'POST':
        formulaio= CargoForm(data=request.POST)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarCargoView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarCargo.html", data)

def GestionarPermisoADView(request):
    return render(request, "ADgestionarPermiso.html")

def GestionarOrganizacionView(request):
    busqueda = request.GET.get("buscar")
    empleados=Empleado.objects.all()
    page= request.GET.get('page', 1)

    if busqueda:
        empleados = Empleado.objects.filter(
            Q(carnet__icontains =busqueda)|
            Q(nombres__icontains = busqueda)|
            Q(apellidos__icontains = busqueda)|
            Q(area__nombre_area__icontains = busqueda)|
            Q(cargo__nombre_cargo__icontains = busqueda)
        ).distinct()

    try:
        paginator = Paginator(empleados, 10)
        empleados= paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': empleados,
        'paginator': paginator
    }
    return render(request, "ADgestionarOrganizacion.html", data)

def ModificarPagoView(request):
    return render(request, "ADmodificarPago.html")

#CREAR EMPLEADO
def GestionarEmpleadoADView(request):
    if request.method == 'POST':
        carnet = request.POST.get('carnet')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        dui = request.POST.get('dui')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        area_id = request.POST.get('area')
        cargo_id = request.POST.get('cargo')
        departamento_id = request.POST.get('departamento')
        municipio_id = request.POST.get('municipio')
        fechanacimiento = request.POST.get('fechanacimiento')
        telefono = request.POST.get('telefono')
        salariobase = request.POST.get('salariobase')

        area = Area.objects.get(pk=area_id)
        cargo = Cargo.objects.get(pk=cargo_id)
        departamento = Departamento.objects.get(pk=departamento_id)
        municipio = Municipio.objects.get(pk=municipio_id)

        Empleado.objects.create(
            carnet=carnet, nombres=nombres, apellidos=apellidos, dui=dui, genero=genero,
            direccion=direccion, area=area, cargo=cargo, departamento=departamento,
            municipio=municipio, fechanacimiento=fechanacimiento, telefono=telefono,
            salariobase=salariobase
        )

        return redirect('GestionarOrganizacionView')

    return render(request, 'ADgestionarEmpleado.html', {
        'areas': Area.objects.all(),
        'departamentos': Departamento.objects.all()
    })

def get_cargos(request):
    area_id = request.GET.get('area_id')
    cargos = list(Cargo.objects.filter(area_id=area_id).values('id_cargo', 'nombre_cargo'))
    return JsonResponse({'cargos': cargos})

def get_municipios(request):
    departamento_id = request.GET.get('departamento_id')
    municipios = list(Municipio.objects.filter(departamento_id=departamento_id).values('id_municipio', 'nombre_municipio'))
    return JsonResponse({'municipios': municipios})

def RegistrarAsistenciaView(request):
    return render(request, "ADregistrarAsistencia.html")

def GestionarPagoADView(request):
    busqueda = request.GET.get("buscar")
    pagos = Pago.objects.all()
    if busqueda:
        pagos = Pago.objects.filter(
            Q(codigo_pago__icontains =busqueda)
        ).distinct()
    data = {
        'pagos': pagos
    }
    return render(request, "ADgestionarPago.html", data)

def EliminarCargo(request, id):
    cargo = get_object_or_404(Cargo, id_cargo=id)
    cargo.delete()
    return redirect("AdministrarCargoView")

def EliminarArea(request, id):
    cargo = get_object_or_404(Area, id_area=id)
    cargo.delete()
    return redirect("AdministrarAreaView")

def EliminarEmpleado(request, id):
    cargo = get_object_or_404(Empleado, carnet=id)
    cargo.delete()
    return redirect("GestionarOrganizacionView")

def ModificarCargo(request, id):
    cargo= get_object_or_404(Cargo, id_cargo=id)
    data={
        'form':CargoForm(instance=cargo)
    }
    if request.method == 'POST':
        formulaio= CargoForm(data=request.POST, instance=cargo)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarCargoView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarCargo.html", data)

def ModificarArea(request, id):
    area= get_object_or_404(Area, id_area=id)
    data={
        'form':AreaForm(instance=area)
    }
    if request.method == 'POST':
        formulaio= AreaForm(data=request.POST, instance=area)
        if formulaio.is_valid():
            formulaio.save()
            return redirect("AdministrarAreaView")
        else:
            data["form"]= formulaio
    return render(request, "ADgestionarArea.html", data)

def Registro(request, id):
    empleados=get_object_or_404(Empleado, carnet=id)
    data={
        'form': CustomUserCreationForm(),
        'empleados':empleados
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST, )
        #formulario.fields["username"].initial= empleados.carnet
        if formulario.is_valid():
            formulario.save()
            # user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request,user)
            return redirect(to="GestionarOrganizacionView")
        data["form"]= formulario

    return render(request, 'registration/registro.html',data)

def exit(request):
    logout(request)
    return redirect("/")

# def RegistrarAsistenciaView(request):
#     return render(request, "ADregistrarAsistencia.html")

#@login_required
def RegistrarAsistenciaView(request):
    if request.method == 'POST' and 'csv_file' in request.FILES:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            next(reader)  # Omitir la cabecera del CSV

            data = []
            for row in reader:
                try:
                    carnet = Empleado.objects.get(carnet=row[0])
                    data.append({
                        'carnet': carnet.id,  # Almacenar el ID del empleado
                        'horas_trabajadas_diunas': row[1],
                        'horas_trabajadas_nocturnas': row[2],
                        'horas_extras_diurnas': row[3],
                        'horas_extras_nocturnas': row[4],
                        'mes_asistencia': row[5],
                    })
                except Empleado.DoesNotExist:
                    continue  # Omitir registros con carnet no encontrado

            request.session['csv_data'] = data
            return render(request, 'ADregistrarAsistencia.html', {'data': data})
    else:
        form = CSVUploadForm()

    return render(request, 'ADregistrarAsistencia.html', {'form': form})

#@login_required
def save_csv(request):
    if request.method == 'POST':
        csv_data = request.session.get('csv_data')

        if csv_data:
            for item in csv_data:
                Asistencia.objects.create(
                    carnet_id=item['carnet'],  # Usar el ID del empleado
                    horas_trabajadas_diunas=item['horas_trabajadas_diunas'],
                    horas_trabajadas_nocturnas=item['horas_trabajadas_nocturnas'],
                    horas_extras_diurnas=item['horas_extras_diurnas'],
                    horas_extras_nocturnas=item['horas_extras_nocturnas'],
                    mes_asistencia=item['mes_asistencia']
                )

            messages.success(request, 'Datos importados exitosamente.')
            return redirect('RegistrarAsistenciaView')
        else:
            messages.error(request, 'No hay datos para guardar.')

    return redirect('RegistrarAsistenciaView')