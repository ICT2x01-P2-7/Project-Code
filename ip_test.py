from ip import IpValidator

def test1():
    ipTest = IpValidator('192.168.0.1')

    result = ipTest.validate_ip_address()

    print("Test 1: Passed in '192.168.0.1', expect True")
    print("Result returned: ", result)

def test2():
    ipTest = IpValidator('192.168.0.300')

    result = ipTest.validate_ip_address()

    print("Test 2: Passed in '192.168.0.300', expect False")
    print("Result returned: ", result)

def test3():
    ipTest = IpValidator('19216801')

    result = ipTest.validate_ip_address()

    print("Test 3: Passed in integer 19216801, expect False")
    print("Result returned: ", result)

def test4():
    ipTest = IpValidator('192')

    result = ipTest.validate_ip_address()

    print("Test 4: Passed in '192', expect False")
    print("Result returned: ", result)

def test5():
    ipTest = IpValidator('This is an IP address')

    result = ipTest.validate_ip_address()

    print("Test 5: Passed in 'This is an IP address', expect False")
    print("Result returned: ", result)

# Test cases for start_connect
def test6():
    ipTest = IpValidator('192.168.4.1')

    result = ipTest.start_connect()

    print("Test 6: Passed in '192.168.0.1', expect True")
    print("Result returned: ", result)

def test7():
    ipTest = IpValidator('192.168.0.300')

    result = ipTest.start_connect()

    print("Test 7: Passed in '192.168.0.300', expect False")
    print("Result returned: ", result)

def test8():
    ipTest = IpValidator('19216801')

    result = ipTest.start_connect()

    print("Test 8: Passed in '19216801', expect False")
    print("Result returned: ", result)

def test9():
    ipTest = IpValidator('192')

    result = ipTest.start_connect()

    print("Test 9: Passed in '192', expect False")
    print("Result returned: ", result)

def test10():
    ipTest = IpValidator('This is an IP address')

    result = ipTest.start_connect()

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