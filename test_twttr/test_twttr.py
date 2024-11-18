from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("") == ""
    assert shorten("MALiK") == "MLK"
    assert shorten("(*$#E") == "(*$#"
    assert shorten("!.") == "!."
    assert shorten("1") == "1"
    assert shorten("AEIOUaeiou") == ""
