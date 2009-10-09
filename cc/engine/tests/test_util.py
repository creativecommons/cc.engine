from cc.engine import util

class FakeAcceptLanguage(object):
    def __init__(self, best_matches):
        self._best_matches = best_matches

    def best_matches(self):
        return self._best_matches


class FakeRequest(object):
    def __init__(self, best_matches):
        self.accept_language = FakeAcceptLanguage(best_matches)


def test_get_locale_text_orientation():
    # Make sure rtl languates are accepted as rtl
    assert util.get_locale_text_orientation(
        FakeRequest(['he-il'])) == u'rtl'

    # Make sure ltr languates are accepted as ltr
    assert util.get_locale_text_orientation(
        FakeRequest(['en'])) == u'ltr'

    # Make sure rtl language first is rtl
    assert util.get_locale_text_orientation(
        FakeRequest(['he-il', 'en'])) == u'rtl'

    # Make sure ltr language first is ltr
    assert util.get_locale_text_orientation(
        FakeRequest(['en', 'he-il'])) == u'ltr'

    # Make sure unknown/imaginary languages are ignored
    assert util.get_locale_text_orientation(
        FakeRequest(['foo-bar', 'he-il'])) == u'rtl'
    assert util.get_locale_text_orientation(
        FakeRequest(['foo-bar', 'en'])) == u'ltr'

    # If only an unknown/imaginary language is given, default to ltr
    assert util.get_locale_text_orientation(
        FakeRequest(['foo-bar'])) == u'ltr'

    # If only an no language is given, default to ltr
    assert util.get_locale_text_orientation(
        FakeRequest([])) == u'ltr'
