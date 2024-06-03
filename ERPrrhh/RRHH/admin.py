from django.contrib import admin
from django import forms
from .models import Area, Cargo, Empleado, Departamento, Municipio, Pago, Asistencia, Permiso

# Register your models here.
class EmpleadoAdminForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre_municipio')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['municipio'].queryset = self.instance.departamento.municipios.order_by('nombre_municipio')
            
        if 'area' in self.data:
            try:
                area_id = int(self.data.get('area'))
                self.fields['cargo'].queryset = Cargo.objects.filter(area_id=area_id).order_by('nombre_cargo')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cargo'].queryset = self.instance.area.cargos.order_by('nombre_cargo')
            
class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoAdminForm
    list_display = ('carnet', 'nombres', 'apellidos', 'departamento', 'municipio', 'area', 'cargo')
    list_filter = ('departamento', 'municipio', 'area', 'cargo')	
    

admin.site.register(Empleado, EmpleadoAdmin)

class MunicipioInline(admin.TabularInline):
    model = Municipio
    extra = 1

class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [MunicipioInline]
    
class CargoInline(admin.TabularInline):
    model = Cargo
    extra = 1

class AreaAdmin(admin.ModelAdmin):
    inlines = [CargoInline]

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio)
admin.site.register(Cargo)
admin.site.register(Area)
admin.site.register(Pago)
admin.site.register(Asistencia)
admin.site.register(Permiso)