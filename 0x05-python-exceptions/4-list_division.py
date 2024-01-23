#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_len):
    ans = []
    for i in range(list_len):
        try:
            d = my_list_1[i] / my_list_2[i]
        except TypeError:
            d = 0
            print("wrong type")
        except ZeroDivisionError:
            d = 0
            print("division by zero")
        except IndexError:
            d = 0
            print("out of range")
        finally:
            ans.append(d)
    return (ans)
