from car import Car # del archivo car importar el método Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car() # creo una variable igual a la clase Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Marta"
    print(vars(car2))