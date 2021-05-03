from math_series.math_series import lucas , fibonacci , sum_series 
# testing lucas

def test_lucas_0():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas_1():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas_2():
    expected = 3
    actual = lucas(2)
    assert actual == expected
    
def test_lucas_3():
    expected = 4
    actual = lucas(3)
    assert actual == expected


# testing fibonacci
def test_fibonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fibonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci_2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fibonacci_3():
    expected = 2
    actual = fibonacci(3)
    assert actual == expected


# testing sum_series
def test_sum_0_with_default():
    # This should generate the same as fibonacci
    expected = 0
    actual = sum_series(0)
    assert actual == expected

def test_sum_2_with_default():
     # This should generate the same as fibonacci
    expected = 1
    actual = sum_series(2)
    assert actual == expected
    
def test_sum_3_without_default_lucas():
     # This should generate the same as lucas
    expected = 4
    actual = sum_series(3,2,1)
    assert actual == expected

def test_sum_2_without_default_otherseries():
     # This should generate new series at n =2 starting with 2,3
    expected = 5
    actual = sum_series(2,2,3)
    assert actual == expected
    
def test_sum_3_without_default_otherseries():
    # This should generate new series at n =3 starting with 1,5
    expected = 11
    actual = sum_series(3,1,5)
    assert actual == expected
    


