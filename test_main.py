from main import thing

def test_thing_works():
    expected = 3
    result = thing(1, 2)
    assert expected == result
