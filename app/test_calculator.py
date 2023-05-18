from .calculator import Calculator


def test_add():
    assert Calculator().add(1, 2) == 3.0
    assert Calculator().add(1.0, 2.0) == 3.0
    assert Calculator().add(0, 2.0) == 2.0
    assert Calculator().add(2.0, 0) == 2.0
    assert Calculator().add(-4, 2.0) == -2.0


def test_add_two_positive_integeres():
    assert Calculator().add(1, 2) == 3.0


def test_add_is_a_conmutative_operation():
    assert Calculator().add(1, 2) == Calculator().add(2, 1)


def test_add_two_negative_integeres():
    assert Calculator().add(-1, -2) == -3.0


def test_add_positive_integere_and_zero():
    assert Calculator().add(1, 0) == 1.0


def test_subtract():
    assert Calculator().subtract(1, 2) == -1.0
    assert Calculator().subtract(2, 1) == 1.0
    assert Calculator().subtract(1.0, 2.0) == -1.0
    assert Calculator().subtract(0, 2.0) == -2.0
    assert Calculator().subtract(2.0, 0.0) == 2.0
    assert Calculator().subtract(-4, 2.0) == -6.0


def test_multiply():
    assert Calculator().multiply(1, 2) == 2.0
    assert Calculator().multiply(1.0, 2.0) == 2.0
    assert Calculator().multiply(0, 2.0) == 0.0
    assert Calculator().multiply(2.0, 0.0) == 0.0
    assert Calculator().multiply(-4, 2.0) == -8.0


# def test_pow():
#    assert Calculator().pow(1, 0) == 1.0
#    assert Calculator().pow(2, 3) == 8.0
#    assert Calculator().pow(4, -1) == 2


def test_pow_power_zero():
    assert Calculator().pow(1, 0) == 1.0


def test_pow_positive_base_and_power():
    assert Calculator().pow(2, 3) == 8.0


# def test_pow_positive_base_and_negative_power():
# assert Calculator().pow(4, -1) == 2


def test_divide():
    assert Calculator().divide(1, 2) == 0.5
    assert Calculator().divide(1.0, 2.0) == 0.5
    assert Calculator().divide(0, 2.0) == 0
    assert Calculator().divide(-4, 2.0) == -2.0
    # assert Calculator().divide(2.0, 0.0) == 'Cannot divide by 0'
