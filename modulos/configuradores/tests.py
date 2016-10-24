from django.test import TestCase
from autofixture import AutoFixture
from modulos.configuradores.models import  Area
from modulos.configuradores.models import  clases
# Create your tests here.

class ConfiguradoresTestCase(TestCase):


    def setUp(self):
        for clase in clases():
            fixture = AutoFixture(clase)
            entries = fixture.create(10)
    def test_creacion10(self):
        print "Prueba de configuraciones"
        for clase in clases():
            self.assertEqual(clase.objects.filter().count(), 10)
