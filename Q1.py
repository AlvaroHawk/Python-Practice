
# These are the values need to be converted:
x_int=7649
x_float=31.0
x_str_only_number='497'
x_str_only_letter='AbCdEfJ'
x_str_only_complex='7+2j'
x_str_NumberAndAlpha='237abc'
x_str_mess='sof2+j(vse)'
x_bool=True
x_complex=1+2j
import random
import re
# IMPLEMENT YOUR FUNCTION HERE
def random_converter(x):
    import random
    import re
    item_type=type(x)
    a=random.randint(0,4)
    # using RE to test the concent.
    # first set RE testing rules.
    test1=r'^\d+$'
    test2=r'^\d*\.?\d*$'
    test3=r'^[(]?\d+\.?\d*\+\d+\.?\d*j[)]?$'
    test4=r'^[(]?\d*\.?\d*[)]?$'

    if a == 0:                     #converter into int
        if item_type == str:
            if re.findall(test1,x) != []:
                print('Converted into integer:')
                print(int(x))
            else:
                print('this string cannot be converted into integer')
        elif item_type == complex:
            print('Complex cannot be converted into integer')
        else:
            print('Converted into integer:')
            print(int(x))

    if a == 1:                        #converter into float
        if item_type == str:
            if x == '':
                print('this string cannot be converted into float')
            else:
                if re.findall(test2,x) != []:
                    print('Converted into float: ')
                    print(float(x))
                else:
                    print('this string cannot be converted into float')
        elif item_type == complex:
            print('Complex cannot be converted into float')
        else:
            print('Converted into float: ')
            print(float(x))

    if a == 2:                     #converter into string
        print('Converted into string: ')
        print(str(x))

    if a == 3:                        #converter into bool
        print('Converted into bool: ')
        print(bool(x))

    if a == 4:                        #converter into complex
        if item_type == str:
            if re.findall(test3,x) != []:
                print('Converted into complex: ')
                print(complex(x))
            elif re.findall(test4,x) != []:
                print('Converted into complex: ' + str(complex(x)))
                print(complex(x))
            else:
                print('this string cannot be converted into complex')
        else:
            print('Converted into complex: ')
            print(complex(x))




# Call Function:


random_converter(x_int)
random_converter(x_float)
random_converter(x_str_only_number)
random_converter(x_str_only_letter)
random_converter(x_str_NumberAndAlpha)
random_converter(x_str_only_complex)
random_converter(x_str_mess)
random_converter(x_bool)
random_converter(x_complex)
