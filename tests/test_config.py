from unittest import TestCase, main

from carbonsh.Config import *


class TestConfig(TestCase):
    def test_parse_bg(self):
        expect = 'rgba(171, 184, 195, 1)'
        self.assertEqual(parse_bg(''), expect, msg='Default does not match')
        self.assertEqual(parse_bg('#ABB8C3'), expect, msg='Hex to RGBA conversion failed')

    def test_int_to_px(self):
        self.assertEqual(int_to_px(10), '10px')

    def test_int_to_percent(self):
        self.assertEqual(int_to_percent(10), '10%')

    def test_Config_default(self):
        expect = "bg=rgba(171%2C%20184%2C%20195%2C%201)&t=seti&wt=none&l=auto&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false"

        config = Config()
        self.assertEqual(str(config), expect, msg='Default does not match')

    def test_Config(self):
        expect = "bg=rgba(171%2C%20184%2C%20195%2C%201)&t=seti&wt=none&l=javascript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false"

        config = Config(language=languages.JAVASCRIPT)
        self.assertEqual(str(config), expect, msg='Default does not match')
if __name__ == '__main__':
    main()
