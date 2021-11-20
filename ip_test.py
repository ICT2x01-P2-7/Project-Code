from ip import validate_ip_address, start_connect

def test1():
    result = validate_ip_address('192.168.0.1')

    print("Test 1: Passed in '192.168.0.1', expect True")
    print("Result returned: ", result)

def test2():
    result = validate_ip_address('192.168.0.300')

    print("Test 2: Passed in '192.168.0.300', expect False")
    print("Result returned: ", result)

def test3():
    result = validate_ip_address('19216801')

    print("Test 3: Passed in integer 19216801, expect False")
    print("Result returned: ", result)

def test4():
    result = validate_ip_address('192')

    print("Test 4: Passed in '192', expect False")
    print("Result returned: ", result)

def test5():
    result = validate_ip_address('This is an IP address')

    print("Test 5: Passed in 'This is an IP address', expect False")
    print("Result returned: ", result)

# Test cases for start_connect
def test6():
    result = start_connect('192.168.0.1')

    print("Test 6: Passed in '192.168.0.1', expect True")
    print("Result returned: ", result)

def test7():
    result = start_connect('192.168.0.300')

    print("Test 7: Passed in '192.168.0.300', expect False")
    print("Result returned: ", result)

def test8():
    result = start_connect('19216801')

    print("Test 8: Passed in '19216801', expect False")
    print("Result returned: ", result)

def test9():
    result = start_connect('192')

    print("Test 9: Passed in '192', expect False")
    print("Result returned: ", result)

def test10():
    result = start_connect('This is an IP address')

    print("Test 10: Passed in 'This is an IP address', expect False")
    print("Result returned: ", result)

if __name__ =='__main__':
    test1()
    print('\n')
    test2()
    print('\n')
    test3()
    print('\n')
    test4()
    print('\n')
    test5()
    print('\n')
    test6()
    print('\n')
    test7()
    print('\n')
    test8()
    print('\n')
    test9()
    print('\n')
    test10()