#define los elementos

from .models import Empleados
from rest_framework import serializers

class EmpleadoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'identificacion','nombres','apellidos', 'correo', 'salario_base','activo')