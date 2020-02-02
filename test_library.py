from CTF.library import cipher


def test_cipher():
    assert "cccc" == cipher("bbbb", 1)
    assert "cccc" == cipher("dddd", -1)

    assert "zzz" == cipher("aaa", -1)
    assert "aaa" == cipher("zzz", 1)

    assert "cccc" == cipher("bbbb", 27)
    assert "cccc" == cipher("dddd", -27)

    assert "zzz" == cipher("aaa", -27)
    assert "aaa" == cipher("zzz", 27)

    assert "b-z" == cipher("a-y", 1)
