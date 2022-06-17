from curses.ascii import US
from car import Car # del archivo car importar el método Car
from account import Account
from uberX import UberX
from uberPool import UberPool
from user import User


if __name__ == "__main__":
    print("Hola Mundo")
    
    car = Car("AMS234", Account("Andres Herrera", "ABA123")) # creo una variable igual a la clase Car()
    print(vars(car))
    print(vars(car.driver))

    uberx = UberX("AMS234",Account("Andres Herrera", "ABA123"),"Chevrolet", "Corsa" )
    print(vars(uberx))
    print(vars(uberx.driver))

    user = User("Nicolas", "34290466")
    print(vars(user))

    # car2 = Car("QWE567", Account("Marta Perez", "DNI354"))
    # print(vars(car2))
