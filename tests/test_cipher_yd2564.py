from cipher_yd2564 import __version__
from cipher_yd2564 import cipher_yd2564


def test_version():
    assert __version__ == '0.1.1'


def test_negative_shift():
    assert cipher_yd2564.cipher('the', -1, encrypt=True) == 'sgd'
