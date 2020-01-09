from . import other_hello

def test_other_hello():
    assert other_hello.apply("Jane") == "hello Jane"
