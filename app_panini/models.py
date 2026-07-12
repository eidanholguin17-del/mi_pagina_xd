from django.db import models

# Create your models here.


class Personaje:

    def __init__(self ,Nombre ,Fuerza ,Intelligencia ,agilidad ,Vida ,Defensa):
        self.Nombre=Nombre
        self.Fuerza=Fuerza
        self.Intelligencia=Intelligencia
        self.agilidad=agilidad
        self.Vida=Vida
        self.Defensa=Defensa
    
    def atributos(self):
        print(self.Nombre,":",sep="")
        print("·Fuerza",self.Fuerza)
        print("·Intelligencia",self.Intelligencia)
        print("·Agilidad",self.agilidad)
        print("·Vida",self.Vida)
        print("·Defensa",self.Defensa)

    def subir_nivel(self,Fuerza ,Intelligencia ,agilidad ,Vida ,Defensa):
        self.Fuerza = self.Fuerza + Fuerza
        self.Intelligencia = self.Intelligencia + Intelligencia
        self.agilidad = self.agilidad + agilidad
        self.Vida = self.Vida + Vida
        self.Defensa = self.Defensa + Defensa

    def estar_vivo(self):
        return self.Vida > 0

    def morir(self):
        self.Vida = 0
        print("El personaje",self.Nombre,"ha muerto")

    def daño(self,Enemigo):
        if self.Fuerza > Enemigo.Defensa:
            return self.Fuerza - Enemigo.Defensa
        else:
            return 0
    
    def atacar(self,Enemigo):
        daño = self.daño(Enemigo)
        Enemigo.Vida = Enemigo.Vida - daño
        print("El personaje",self.Nombre,"ataco a",Enemigo.Nombre,"y realizo un daño de",daño)
        print("La vida de",Enemigo.Nombre,"es de",Enemigo.Vida)
        if Enemigo.Vida <= 0:
            Enemigo.morir()

    def seleccionar_arma(self):
       opcion = int(input("Selecciona un arma para tu personaje:(1) Espada,daño 8 .(2) Arco, daño 5 .(3) Lanza, daño 6 "))
       if opcion == 1:
           self.espada = 8
       elif opcion == 2:
           self.arco = 5
       else:
          print("Opcion no valida")


class guerrero(Personaje):
    def __init__(self, Nombre, Fuerza, Intelligencia, agilidad, Vida, Defensa, espada):
        super().__init__(Nombre, Fuerza, Intelligencia, agilidad, Vida, Defensa)
        self.espada = espada



