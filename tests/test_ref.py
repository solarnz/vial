import vial.utils
from vial import ref, refs


def test_ref():
    refs.clear()

    def boo(foo):
        return foo
    r = ref(boo)

    assert r(1) == 1
    assert str(r) == 'vial.refs[\'tests.test_ref.boo:8\']'


def test_ref_with_same_name():
    refs.clear()

    def boo():
        return 1
    r1 = ref(boo)

    def boo():
        return 2
    r2 = ref(boo)

    assert r1() == 1
    assert r2() == 2


def test_lambda():
    refs.clear()
    r = ref(lambda: 'boo')
    assert r() == 'boo'
    assert str(r) == 'vial.refs[\'tests.test_ref.<lambda>:33\']'


def bar(foo):
    return foo


def test_lazy_func():
    refs.clear()
    r = ref('.test_ref.bar')
    assert r(10) == 10
    assert str(r) == 'vial.refs[\'tests.test_ref.bar:lazy\']'
