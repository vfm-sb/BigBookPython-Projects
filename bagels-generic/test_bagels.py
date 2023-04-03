"""bagels.py -- Simple Function Tests Using pytest"""

import bagels


def test_pico_fermi_bagels_function():
    assert bagels.pico_fermi_bagels("123", "123") == ["Pico", "Pico", "Pico"]
    assert bagels.pico_fermi_bagels("123", "423") == ["Pico", "Pico"]
    assert bagels.pico_fermi_bagels("123", "124") == ["Pico", "Pico"]
    assert bagels.pico_fermi_bagels("123", "143") == ["Pico", "Pico"]
    assert bagels.pico_fermi_bagels("123", "145") == ["Pico"]
    assert bagels.pico_fermi_bagels("123", "983") == ["Pico"]
    assert bagels.pico_fermi_bagels("123", "928") == ["Pico"]
    assert bagels.pico_fermi_bagels("123", "321") == ["Fermi", "Pico", "Fermi"]
    assert bagels.pico_fermi_bagels("123", "932") == ["Fermi", "Fermi"]
    assert bagels.pico_fermi_bagels("123", "451") == ["Fermi"]
    assert bagels.pico_fermi_bagels("123", "415") == ["Fermi"]
    assert bagels.pico_fermi_bagels("123", "345") == ["Fermi"]
    assert bagels.pico_fermi_bagels("123", "456") == ["Bagels"]
