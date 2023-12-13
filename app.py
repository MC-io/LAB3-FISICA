def find_force_N3L(mass, acceleration):
    force = mass * acceleration
    return force

def find_mass_N3L(acceleration, force):
    mass = force / acceleration
    return mass

def find_acceleration_N3L(force, mass):
    acceleration = force / mass
    return acceleration 

if __name__ == "__main__":
    print("*****MENU*****")
    print("1) Fuerza")
    print("2) Masa")
    print("3) Aceleracion")

    op = input("Selecciona la opcion del parametro que deseas calcular co la tercera ley de Newton: ")
    if op == "1":
        mass = float(input("Ingrese la masa en kg: "))
        if mass == 0:
            print("LA MASA NO PUEDE SER 0, ES IMPOSIBLE")
            exit()
        acceleration = float(input("Ingrese la aceleracion en m/s^2: "))
        force = find_force_N3L(mass, acceleration)
        print("Segun la tercera ley de Newton la fuerza es igual a: {} N".format(force))   
    elif op == "2":
        acceleration = float(input("Ingrese la aceleracion en m/s^2: "))
        force = float(input("Ingrese la fuerza en N: "))
        mass = find_mass_N3L(acceleration, force)
        print("Segun la tercera ley de Newton la masa es igual a: {} kg".format(mass))   
    elif op == "3":
        mass = float(input("Ingrese la masa en kg: "))
        if mass == 0:
            print("LA MASA NO PUEDE SER 0, ES IMPOSIBLE")
            exit()
        force = float(input("Ingrese la fuerza en N: "))
        acceleration = find_acceleration_N3L(mass, force)
        print("Segun la tercera ley de Newton la masa es igual a: {} m/s^2".format(acceleration))   
