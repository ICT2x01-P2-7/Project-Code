from authenticate import check

def test1():
    result = check('password')

    print("Test 1: Passed in string 'password', expect False")
    print("Result returned: ", result)

def test2():
    result = check(123)

    print("Test 2: Passed in integer 123, expect False")
    print("Result returned: ", result)

def test3():
    result = check('1a2b3c')

    print("Test 3: Passed in string '1a2b3c', expect False")
    print("Result returned: ", result)

def test4():
    result = check('admin')

    print("Test 4: Passed in string 'admin', expect True")
    print("Result returned: ", result)

def test5():
    result = check(123.123)

    print("Test 5: Passed in float 123.123, expect False")
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