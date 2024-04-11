def dobro(x):
    return 2 * x

def quadruplica(x):
    return dobro(x) * x

def test_with_number_integer():
    assert dobro(2) == 4
    
def test_with_number_float():
    assert dobro(2.0) == 5

def test_with_string():
    assert dobro("a") == "aa"