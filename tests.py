def test_smile():
    from awesome import smile
    assert smile() == ':)'


def test_frown():
    from awesome import frown
    assert frown() == ':('


def test_laugh():
    from awesome import laugh
    assert laugh() == ':-D'


def test_cry():
    from awesome import cry
    assert cry() == '(:_;)'
