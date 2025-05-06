import random

#Crear clase Building que contenga conteo de pisos y habitaciones
class Building:
#se inicia el programa con numero de pisos y de habitaciones    
    def __init__(self, floors_count, rooms_floor):
        self.floors = []
        self.floors_count = floors_count
        self.rooms_floor = rooms_floor
        for i in range(floors_count): #Crea los pisos y habitaciones
            floor = Floor(i, rooms_floor)
            self.floors.append(floor)
#Muestra el estado actual del edificio    
    def show_status(self):
        for floor in self.floors:
            print(f"Floor {floor.floor_number}:")
            floor.show_rooms()
            print("\n")

#Crear clase Floor que contenga numero de pisos y de habitaciones
class Floor:
    def __init__(self, floor_number, rooms_count):
        self.floor_number = floor_number
        self.rooms = [Room() for _ in range(rooms_count)]      

    def show_rooms(self):
        for i, room in enumerate(self.rooms):
            print(f"  Room {i}: {room.check_sensor()}")
        
#Crear clase Room que donde se revisan los sensores
class Room:
    def __init__(self):
        self.sensor = Sensor()
        self.has_zombies = False
    
    def add_zombies(self):
        self.has_zombies = True
        self.sensor.set_alert()
    
    def remove_zombies(self):
        self.has_zombies = False
        self.sensor.reset()
    
    def check_sensor(self):
        return str(self.sensor)

#Definimos clase sensor 
class Sensor:
#parametro inicial
    def __init__(self):
        self.state = "normal"
#en estado de alerta 
    def set_alert(self):
        self.state = "alert"
#se vuelve a la normalidad    
    def reset(self):
        self.state = "normal"
#imprimir respuesta del estado del sensor    
    def __str__(self):
        return f"Sensor state: {self.state}"

#Definimos la simulacion
class Simulation:
    def __init__(self, floors, rooms, zombies):
        self.building = Building(floors, rooms)
        self.zombie_positions = []
        self.place_zombies(zombies)

#Definir cantidad de zombies    
    def place_zombies(self, num_zombies):
        placed = 0
        while placed < num_zombies:
            floor = random.randint(0, self.building.floors_count - 1)
            room = random.randint(0, self.building.rooms_floor - 1)
            if not self.building.floors[floor].rooms[room].has_zombies:
                self.building.floors[floor].rooms[room].add_zombies()
                self.zombie_positions.append((floor, room))
                placed += 1

#Definimos movimientos y lo guardamos en una lista    
    def advance_turn(self):
        new_positions = set(self.zombie_positions)
        for floor_num, room_num in self.zombie_positions:
            possible_moves = []
            if room_num > 0:
                possible_moves.append((floor_num, room_num - 1))
            if room_num < self.building.rooms_floor - 1:
                possible_moves.append((floor_num, room_num + 1))
            if floor_num > 0:
                possible_moves.append((floor_num - 1, room_num))
            if floor_num < self.building.floors_count - 1:
                possible_moves.append((floor_num + 1, room_num))
            
            for move in possible_moves:
                if move not in new_positions:
                    self.building.floors[move[0]].rooms[move[1]].add_zombies()
                    new_positions.add(move)
        
        self.zombie_positions = list(new_positions)
    
    def play(self):
        while True:
            print("\n--- ESTADO DEL EDIFICIO ---")
            self.building.show_status()
            print("1. Avanzar turno !!NOS INVADEN LOS ZOMBIES!!")
            print("2. Mostrar estado del edificio")
            print("3. Salir")
            choice = input("Selecciona una opción: ")
            
            if choice == '1':
                self.advance_turn()
            elif choice == '2':
                continue
            
            elif choice == '3':
                print("Simulación terminada.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    floors = int(input("¿Cuántos pisos tiene el edificio? "))
    rooms = int(input("¿Cuántas habitaciones por piso? "))
    zombies = int(input("¿Cuántos zombis iniciales? "))
    
    simulation = Simulation(floors, rooms, zombies)
    simulation.play()
    
