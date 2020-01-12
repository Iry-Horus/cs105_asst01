## This is a test program for COMPSCI 105, Summer 2017, Assignment One.
## You can use this program to run a small number of basic tests on the
## three classes you have defined (in the "Asst1.py" source file).

## You should define additional tests to test these classes.  You are
## welcome to modify this "TestProgram.py" source file directly, because
## you will not submit it for marking.  You will only submit the file
## "Asst1.py" for marking.

## Good luck!

from Asst1 import Polynomial
from Asst1 import Car
from Asst1 import Traffic

test_counts = [0, 0]

def print_welcome():
        print('CS105 - Summer School 2017')
        print('Assignment One')
        print('--------------')
        print('This is a basic program that is designed to be run alongside the "Asst1.py"')
        print('source file that you have prepared.  The "Asst1.py" source file should contain')
        print('your definitions of the Polynomial, Car and Traffic classes.\n')

def print_results():
        print('\nCurrently, your implementation of "Asst1.py" performs as follows:')
        print('\n  Tests passed:', test_counts[0])
        print('  Tests failed:', test_counts[1])
        print('\nPlease note, this only gives an approximate indication of the correctness of')
        print('your "Asst1.py" source file.  You should design additional tests to test your')
        print('class definitions more thoroughly\n')
        print('Good luck!\n')

def compare_expected_and_actual_output(test_number, expected, actual):
    print('Test #' + str(test_number), end = '')
    if expected == actual:
        print('  PASS :-)  ', actual)
        test_counts[0] = test_counts[0] + 1
    else:
        print('  FAIL :-(')
        print('    - the expected output = ', expected)
        print('    - the actual output =   ', actual)
        test_counts[1] = test_counts[1] + 1

def test_Q1():
    p1 = Polynomial()
    compare_expected_and_actual_output(1, '0', str(p1))

    p1 = Polynomial()
    p1.add_term(1, 2)
    compare_expected_and_actual_output(2, 'x^2', str(p1))

    p1 = Polynomial()
    p1.add_term(2, 4)
    p1.add_term(13, 0)
    p1.add_term(1, 2)
    p1.add_term(-7, 1)
    compare_expected_and_actual_output(3, '2x^4 + x^2 - 7x + 13', str(p1))

    p1 = Polynomial()
    p1.add_term(123, 987654321)
    p1.add_term(-9, -987654321)
    compare_expected_and_actual_output(4, '123x^987654321 - 9x^-987654321', str(p1))

    p1 = Polynomial()
    p1.add_term(1, 3)
    p1.add_term(-4, 2)
    p1.add_term(-100, 25)
    p1.add_term(-66, 0)
    p1.add_term(6, -7)
    compare_expected_and_actual_output(5, '-100x^25 + x^3 - 4x^2 - 66 + 6x^-7', str(p1))

    p1 = Polynomial()
    p2 = Polynomial()
    p1.add_term(3, 5)
    p1.add_term(-2, 2)
    p1.add_term(1, -1)
    result1 = p1.evaluate(2)
    p2.add_term(-7, 10)
    result2 = p2.evaluate(2)
    compare_expected_and_actual_output(6, '88.5', str(result1))
    compare_expected_and_actual_output(7, '-7168', str(result2))

    p1 = Polynomial()
    p1.add_term(5, 2)
    p1.add_term(1, 11)
    p1.add_term(8, -7)
    degree = p1.get_degree()
    compare_expected_and_actual_output(7, '11', str(degree))

    p1 = Polynomial()
    p1.add_term(-4, 3)
    p1.add_term(2, 2)
    p1.add_term(-1, 1)
    p1.add_term(7, 0)
    p1.add_term(6, -2)
    p1.scale(-2)
    compare_expected_and_actual_output(8, '8x^3 - 4x^2 + 2x - 14 - 12x^-2', str(p1))

    p1 = Polynomial()
    p1.add_term(10, 2)
    p1.add_term(-5, 0)
    p2 = Polynomial()
    p2.add_term(5, -1)
    p3 = p1 + p2
    compare_expected_and_actual_output(9, '10x^2 - 5', str(p1))
    compare_expected_and_actual_output(10, '5x^-1', str(p2))
    compare_expected_and_actual_output(11, '10x^2 - 5 + 5x^-1', str(p3))

    p2.add(p1)
    compare_expected_and_actual_output(12, '10x^2 - 5', str(p1))
    compare_expected_and_actual_output(13, '10x^2 - 5 + 5x^-1', str(p2))

    p1 = Polynomial()
    p1.add_term(10, 2)
    p1.add_term(-5, 1)
    p2 = Polynomial()
    p2.add_term(-10, 2)
    p1.add(p2)
    compare_expected_and_actual_output(14, '-5x', str(p1))
    result = p1.get_degree()
    compare_expected_and_actual_output(15, '1', str(result))

    p1 = Polynomial()
    p1.add_term(1, 10)
    p1.add_term(2, 0)
    p1.add_term(3, -1)
    p1.add_term(4, -2)
    p1.add_term(5, -3)
    p1.collapse()
    compare_expected_and_actual_output(16, '15x^4', str(p1))

    p1 = Polynomial()
    p1.add_term(1, 1000)
    p1.add_term(-1, -10)
    p1.collapse()
    compare_expected_and_actual_output(17, '0', str(p1))

    p1 = Polynomial()
    p1.add_term(1, 10)
    compare_expected_and_actual_output(18, 'x^10', str(p1))
    p1.add_term(1, 10)
    compare_expected_and_actual_output(19, '2x^10', str(p1))
    p1.add_term(1, 10)
    compare_expected_and_actual_output(20, '3x^10', str(p1))


def test_Q2():
    t = Traffic(5, 5)
    c1 = Car("UP123", 3, 0, -1, 0)
    c2 = Car("LEFT123", 1, 4, 0, -2)

    t.add_car(c1)
    t.add_car(c2)

    compare_expected_and_actual_output(21, 'UP123_3_0 LEFT123_1_4', str(t))
    t.execute(1)
    compare_expected_and_actual_output(22, 'UP123_2_0 LEFT123_1_2', str(t))
    t.execute(1)
    compare_expected_and_actual_output(23, 'UP123_1_0 LEFT123_1_0', str(t))
    t.execute(1)
    compare_expected_and_actual_output(24, 'UP123_1_0 LEFT123_1_0', str(t))

    result = t.get_collisions()
    compare_expected_and_actual_output(25, '[(1, 0)]', str(result))

    plates = t.get_plates(1, 0)
    compare_expected_and_actual_output(26, "['LEFT123', 'UP123']", str(plates))


    c1 = Car('ABC123', 2, 2, 1, -1)
    c2 = Car('DEF456', 5, 8, 0, 2)

    compare_expected_and_actual_output(27, 'ABC123_2_2', str(c1))
    compare_expected_and_actual_output(28, 'DEF456_5_8', str(c2))

    c1_plate = c1.get_plate()
    c1_pos = c1.get_position()

    compare_expected_and_actual_output(29, 'ABC123', str(c1_plate))
    compare_expected_and_actual_output(30, '(2, 2)', str(c1_pos))

    c1.move(10, 10)
    c2.move(10, 10)
    compare_expected_and_actual_output(31, 'ABC123_3_1', str(c1))
    compare_expected_and_actual_output(32, 'DEF456_5_0', str(c2))

    c3 = Car('GHI789', 3, 1, -1, 2)
    compare_expected_and_actual_output(33, 'True', str(c1.collides(c3)))
    compare_expected_and_actual_output(34, 'False', str(c2.collides(c3)))

    t = Traffic(10, 10)
    c1 = Car('DEF456', 5, 5, -1, -1)
    c2 = Car('ABC123', 1, 1, 1, 1)
    c3 = Car('XYZ999', 9, 9, 0, 0)
    c4 = Car('SLOW12', 8, 8, 0, 0)
    c5 = Car('FAST99', 0, 4, 8, 4)
    t.add_car(c1)
    compare_expected_and_actual_output(35, 'DEF456_5_5', str(t))
    t.add_car(c2)
    compare_expected_and_actual_output(36, 'DEF456_5_5 ABC123_1_1', str(t))
    t.add_car(c3)
    compare_expected_and_actual_output(37, 'DEF456_5_5 ABC123_1_1 XYZ999_9_9', str(t))
    t.add_car(c4)
    compare_expected_and_actual_output(38, 'DEF456_5_5 ABC123_1_1 XYZ999_9_9 SLOW12_8_8', str(t))
    t.add_car(c5)
    compare_expected_and_actual_output(39, 'DEF456_5_5 ABC123_1_1 XYZ999_9_9 SLOW12_8_8 FAST99_0_4', str(t))

    compare_expected_and_actual_output(40, '(5, 5)', str(t.get_location('DEF456')))
    compare_expected_and_actual_output(41, '(9, 9)', str(t.get_location('XYZ999')))
 
    t.execute(1)
    compare_expected_and_actual_output(42, 'DEF456_4_4 ABC123_2_2 XYZ999_9_9 SLOW12_8_8 FAST99_8_8', str(t))

    t.execute(1)
    compare_expected_and_actual_output(43, 'DEF456_3_3 ABC123_3_3 XYZ999_9_9 SLOW12_8_8 FAST99_8_8', str(t))
    
    t.execute(1)
    compare_expected_and_actual_output(44, 'DEF456_3_3 ABC123_3_3 XYZ999_9_9 SLOW12_8_8 FAST99_8_8', str(t))

    compare_expected_and_actual_output(45, '[(3, 3), (8, 8)]', str(t.get_collisions()))

    compare_expected_and_actual_output(46, "['ABC123', 'DEF456']", str(t.get_plates(3, 3)))
    compare_expected_and_actual_output(47, "['XYZ999']", str(t.get_plates(9, 9)))

    t = Traffic(10, 10)
    c1 = Car('DEF456', 5, 5, -1, -1)
    c2 = Car('ABC123', 1, 1, 1, 1)
    c3 = Car('XYZ999', 5, 5, 0, 0)
    c4 = Car('DEF456', 8, 2, 0, 0)

    t.add_car(c1)
    t.add_car(c2)
    except_caught = False
    try:
        t.add_car(c3)
    except ValueError:
        except_caught = True        
    compare_expected_and_actual_output(48, 'True DEF456_5_5 ABC123_1_1', str(except_caught) + ' ' + str(t))

    t.add_car(c4)
    compare_expected_and_actual_output(49, 'DEF456_8_2 ABC123_1_1', str(t))


## Display a welcome message
print_welcome()

## Run the tests
test_Q1()
test_Q2()

## Print results
print_results()

