
from validate import validate_number, validate_lenght


def get_int (mensaje: str, mensaje_error: str, maximo: int, minimo: int, reintentos: int) -> int|None:
    #valido y convierto 
    numero = input(mensaje)
    if validate_number(numero, int):
      numero = int(numero)

      for i in range (reintentos - 1):
          if numero < minimo or numero > maximo:
              numero = int(input(mensaje_error))

              if i == reintentos - 1:
                return None
      return numero
    else:
          print("Error, el valor ingresado no es un numero")


# get_int ("Ingresar un numero entero: ", "Error, ingresar otro numero entero: ", 100, 0, 3)


def validar_int(ingreso, mensaje_error: str, reintentos: int, maximo: int, minimo: int) -> str|None:
    for a in range (reintentos):
        if ingreso < minimo or ingreso > maximo:
            ingreso = int(input(mensaje_error))
            if a == reintentos - 1:
                retorno = None
        
        else:
            retorno = "Numero dentro del rango especificado"
    return retorno

# ingreso = input("Ingresar un numero entero del 0 al 5")
# ingreso = int (ingreso)
# valido = validar_int(ingreso, "reingrese el numero el numero, debe ser del 0 al 5: ", 3, 5, 0,) 
# print(valido)





# def get_float

def get_float (mensaje: str, mensaje_error: str, maximo: int, minimo: int, reintentos: int) -> int|None:
    #valido y convierto 
    numero = input(mensaje)
    if validate_number(numero, float):
      numero = float(numero)

      for i in range (reintentos - 1):
          if numero < minimo or numero > maximo:
              numero = int(input(mensaje_error))

              if i == reintentos - 1:
                return None
      return numero
    else:
          print("Error, el valor ingresado no es un numero")


# get_float ("Ingresar un numero flotante: ", "Error, ingresar otro numero flotante: ", 100, 0, 3)


# def get_string

def get_string(longitud: int) -> str | None:
  cadena = input(f"Ingresar una cadena de {longitud} caracteres como maximo")
  if validate_lenght(cadena, longitud):
      retorno = cadena
  else:
      print("Longitud de cadena invalida")
      retorno = None

  return retorno