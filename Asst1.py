## COMPSCI 105 - Summer, 2017
## Author: <<Zachary Bennett>>

class Polynomial:

    def __init__(self):
        self.values_list = []
        

    def __str__(self):   
        if not self.values_list:
            return str(0)
        
        self.values_list.sort(key=lambda tup: tup[1], reverse=True)
        
        poly_string = ""
        count = 0
        while count < len(self.values_list):
            if count == 0:
                if self.values_list[0][0] == -1:
                    poly_string += "-"
                elif not (self.values_list[0][0] == 0 or self.values_list[0][0] == 1):
                    poly_string += str(self.values_list[0][0])

                if self.values_list[0][1] == 1:
                    poly_string += "x"
                elif not (self.values_list[0][1] == 0 or self.values_list[0][0] == 0):
                    poly_string += "x" + "^" + str(self.values_list[0][1])
                elif self.values_list[0][0] == 0 and len(self.values_list) == 1:
                    return str(0)
                    
            if count > 0:         
                if not self.values_list[count][0] == 0 and not(self.values_list[count][0] == 1 or self.values_list[count][0] == -1):
                    poly_string += str(abs(self.values_list[count][0]))
                    
                if self.values_list[count][1] == 1:
                    poly_string += "x"
                elif self.values_list[count][1] != 0 and not self.values_list[count][0] == 0:
                    poly_string += "x" + "^" + str(self.values_list[count][1])

            if count + 1 == len(self.values_list):
                break
            elif count == 0 and self.values_list[0][0] == 0:
                if self.values_list[count + 1][0] < 0:
                    poly_string += "-"            
            elif self.values_list[count + 1][0] > 0:
                poly_string += " + "
            elif self.values_list[count + 1][0] < 0:
                poly_string += " - "

            count += 1
            
        return poly_string


    def add_term(self, coefficient, exponent):
        added = 0
        for values in self.values_list:
            if exponent == values[1]:
                coeff = values[0]
                self.values_list.pop(self.values_list.index(values))
                self.values_list.append((coeff + coefficient, exponent))
                added = 1

        if added == 0:
            self.values_list.append((coefficient, exponent))


    def __add__(self, other):
        new_values_list = self.values_list + other.values_list
        new_values_list.sort(key=lambda tup: tup[1], reverse=True)

        count = 0
        while count < len(new_values_list) -1:
            if new_values_list[count][1] == new_values_list[count + 1][1]:
                new_values_list[count] = (new_values_list[count][0] + new_values_list[count +1][0], new_values_list[count][1])
                new_values_list.pop(count + 1)
            else:
                count += 1
                
        new_values_list_object = Polynomial()
        for i in range(len(new_values_list)):
            new_values_list_object.add_term(new_values_list[i][0], new_values_list[i][1])
                       
        return new_values_list_object

              
    def add(self, other):
        new_list = self.__add__(other)
        self.values_list = new_list.values_list
        
        
    def scale(self, x):
        count = 0
        while count < len(self.values_list):
            self.values_list[count] = list(self.values_list[count])
            self.values_list[count][0] *= x
            self.values_list[count] = tuple(self.values_list[count])
            count += 1


    def evaluate(self, x):
        result = 0
        count = 0
        while count < len(self.values_list):
            result += self.values_list[count][0] * x ** self.values_list[count][1]
            count += 1
        return result


    def get_degree(self):
        if not self.values_list:
            return str(0)
        
        self.values_list.sort(key=lambda tup: tup[1], reverse=True)
        count = 0
        while self.values_list[count][0] == 0:
            count += 1
        return self.values_list[count][1]


    def collapse(self):
        self.values_list.sort(key=lambda tup: tup[1], reverse=True)
        coeff = 0
        exp = 0
        count = 0
        while count < len(self.values_list):
            if count < len(self.values_list) -1:
                if self.values_list[count][1] == self.values_list[count + 1][1]:
                    coeff += self.values_list[count + 1][0]
                    self.values_list.pop(count + 1)
                else:
                    coeff += self.values_list[count][0]
                    exp += self.values_list[count][1]
                    count += 1 

            else:
                coeff += self.values_list[count][0]
                exp += self.values_list[count][1]
                count += 1 

        if coeff == 0:
            self.values_list = [(0, 0)]
        else:
            self.values_list = [(coeff, exp)]     


class Car:


    def __init__(self, plate, row, col, d_row, d_col):
        self.plate = plate
        self.row = row
        self.col = col
        self.d_row = d_row
        self.d_col = d_col
        self.exploded = 0

    
    def __str__(self):
        return str(self.plate) + '_' + str(self.row) + '_' + str(self.col)
    

    def get_plate(self):
        return str(self.plate)


    def get_position(self):
        return self.row, self.col


    def move(self, max_x, max_y):
        if self.exploded == 0:
            
            self.row += self.d_row           
            while self.row >= max_x:
                self.row -= max_x
            while self.row < 0:
                self.row += max_x
    
            self.col += self.d_col
            while self.col >= max_y:
                self.col -= max_y
            while self.col < 0:
                self.col += max_y
                    
        
    def collides(self, other):
        pos1 = self.get_position()
        pos2 = other.get_position()
        if (pos1[0] == pos2[0] and pos1[1] == pos2[1]):
            return True
        return False


class Traffic:


    def __init__(self, grid_size_rows, grid_size_cols):
        self.grid_size_rows = grid_size_rows
        self.grid_size_cols = grid_size_cols
        self.cars_list = []


    def __str__(self):
        result = ""
        for index in range(len(self.cars_list)):
            plate = self.cars_list[index].get_plate()
            pos = self.cars_list[index].get_position()
            result += plate + '_' + str(pos[0]) + '_' + str(pos[1])
            if index != len(self.cars_list) - 1:
                result += " "   
        return result
        

    def add_car(self, car):
        plate = car.get_plate()
        updated = 0
        pos1 = car.get_position()
        for car2 in self.cars_list:
            plate2 = car2.get_plate()
            pos2 = car2.get_position()
            if pos1 == pos2:
                raise ValueError()

            elif plate == plate2:
                car2.row = car.row
                car2.col = car.col
                updated = 1
                
        if updated == 0:
            self.cars_list.append(car)
        

    def execute(self, steps):
        count = 0
        while count < steps:
            for car in self.cars_list:
                car.move(self.grid_size_rows, self.grid_size_cols)
            for car in self.cars_list:
                plate = car.get_plate()
                for car2 in self.cars_list:
                    plate2 = car2.get_plate()
                    if car.collides(car2) == True and plate != plate2:
                        car.exploded = 1
                        car2.exploded = 1
            count += 1
            

    def get_location(self, plate):
        for car in self.cars_list:
            plate2 = car.get_plate()
            if plate == plate2:
                pos = car.get_position()
                return pos
        return None
        

    
    def get_plates(self, x, y):
        plates_list = []
        for car in self.cars_list:
            pos = car.get_position()
            if pos[0] == x and pos[1] == y:
                plate = car.get_plate()
                plates_list.append(plate)
        return sorted(plates_list)
        
        

    def get_collisions(self):
        collision_positions_list = []
        for car in self.cars_list:
            if car.exploded != 0:
                pos = car.get_position()
                if pos not in collision_positions_list:
                    collision_positions_list.append(pos)
        return sorted(collision_positions_list)






