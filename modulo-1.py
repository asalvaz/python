from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo("Andres") 


c =  CamelCase()
s = "this is a sentence that needs CamelCasing"
camelcased = c.hump(s)
print(camelcased)
