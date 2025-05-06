import random

class Room:
    def __init__(self, name):
        self.name = name
        self.zombie = False

    def detect_zombie(self):
        return "ALERTA ZOMBI" if self.zombie else "Seguro"

class Building:
    def __init__(self, floors, rooms_per_floor):
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.grid = [[Room(f"P{floor+1} - H{room+1}") for room in range(rooms_per_floor)] for floor in range(floors)]

    def display(self):
        for floor in self.grid:
            for room in floor:
                print(f"{room.name}: {room.detect_zombie()}")
            print("-")

    def place_zombies(self, num_zombies):
        for _ in range(num_zombies):
            floor = random.randint(0, self.floors - 1)
            room = random.randint(0, self.rooms_per_floor - 1)
            self.grid[floor][room].zombie = True

    def advance_turn(self):
        new_positions = []
        for floor in range(self.floors):
            for room in range(self.rooms_per_floor):
                if self.grid[floor][room].zombie:
                    self.grid[floor][room].zombie = False
                    possible_moves = [(floor, max(room - 1, 0)), (floor, min(room + 1, self.rooms_per_floor - 1))]
                    if floor > 0:
                        possible_moves.append((floor - 1, room))
                    if floor < self.floors - 1:
                        possible_moves.append((floor + 1, room))
                    move = random.choice(possible_moves)
                    new_positions.append(move)

        for floor, room in new_positions:
            self.grid[floor][room].zombie = True


def main():
    floors = int(input("¿Cuántos pisos tiene el edificio? "))
    rooms = int(input("¿Cuántas habitaciones por piso? "))
    zombies = int(input("¿Cuántos zombis iniciales? "))

    building = Building(floors, rooms)
    building.place_zombies(zombies)
    
    while True:
        print("\nEstado actual del edificio:")
        building.display()
        action = input("¿Avanzar turno? (y/n): ")
        if action.lower() == 'y':
            building.advance_turn()
        else:
            print("Simulación terminada.")
            break

if __name__ == "__main__":
    main()
