#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for a, b in zip(my_list_1, my_list_2):
        try:
            c = a / b
        except (ValueError, TypeError):
            print("wrong type")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except IndexError:
            print("out of range")
            c = 0
        finally:
            new_list.append(c)

    return new_list[:list_length]
