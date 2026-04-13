from par import es_par

def test_pares():
    assert es_par(2) == True
    assert es_par(4) == True
    assert es_par(0) == True

def test_impares():
    assert es_par(1) == False
    assert es_par(3) == False
    assert es_par(7) == False
