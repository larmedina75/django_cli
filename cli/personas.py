import os, sys

# This is let Django knows where to find stuff.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cli.settings")
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR)

# This is allows models to get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#your script goes here --+
#                        |
#                        V

from cli.models import Persona

def start_main_function():
    # count the arguments
    arguments = len(sys.argv) - 1
    if arguments > 0:
        nombre = sys.argv[1]
        edad   = sys.argv[2]
        if isinstance(nombre, str) and edad.isnumeric():
            nueva = Persona()
            nueva.nombre = nombre
            nueva.edad   = edad
            nueva.save()

    # Look for all records on Persona Model
    personas = Persona.objects.all()

    if not personas :
        # No records, create a new
        print("No hay Personas que listar")
        nueva = Persona()
        nueva.nombre = "Anónimo"
        nueva.edad   = 99
        nueva.save()
        print("Se ha agregando a Anónimo de 99 años")
    else:
        # List all records on Model
        for persona in personas:
            print(persona.nombre, persona.edad)



if __name__ == '__main__':
    start_main_function()