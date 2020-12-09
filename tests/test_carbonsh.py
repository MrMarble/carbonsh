import asyncio
import tempfile
from os.path import isfile
from pathlib import Path
from unittest import TestCase, main

import pytest

from carbonsh.Config import Config
from carbonsh.carbonsh import code_to_url, url_to_file
from carbonsh.utils import encode_url


class Test(TestCase):
    def test_url_encode(self):
        url = r'{"text":"\u003cb\uf003eyou\u003c", "test":";/.^%*@({})ñ"}'
        expected = '%257B%2522text%2522%253A%2522%255Cu003cb%255Cuf003eyou%255Cu003c%2522%252C%2520%2522test%2522%253A%2522%253B%252F.%255E%2525*%2540%28%257B%257D%29%25C3%25B1%2522%257D'
        self.assertEqual(expected, encode_url(url))

    def test_code_to_url(self):
        code = 'const test = "testing"'
        expected = 'https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&t=seti&wt=none&l=auto&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=const%2520test%2520%253D%2520%2522testing%2522'

        self.assertEqual(expected, code_to_url(code, Config()))


class TestPng(TestCase):

    @pytest.mark.skip(reason="Cant't test this on CI")
    def test_url_to_file(self):
        url = code_to_url('const test = "testing"', Config())

        temp = tempfile.TemporaryDirectory()
        temp_path = Path(temp.name).joinpath('')

        loop = asyncio.get_event_loop()

        loop.run_until_complete(url_to_file(url, temp_path, headless=False))

        self.assertTrue(isfile(temp_path.joinpath('carbon.png')))
        temp.cleanup()

    def test_url_to_file_headless(self):
        url = code_to_url('const test = "testing headless"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = Path(temp.name).joinpath('')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, headless=True))
        self.assertTrue(isfile(temp_path.joinpath('carbon.png')))
        temp.cleanup()


class TestSvg(TestCase):
    @pytest.mark.skip(reason="Cant't test this on CI")
    def test_url_to_file(self):
        url = code_to_url('const test = "testing"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = Path(temp.name).joinpath('')

        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, extension='svg', headless=False))
        self.assertTrue(isfile(temp_path.joinpath('carbon.svg')))
        temp.cleanup()

    @pytest.mark.skip(reason="Headless can't make svg")
    def test_url_to_file_headless(self):
        url = code_to_url('const test = "testing headless"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = Path(temp.name).joinpath('')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, extension='svg', headless=True))
        self.assertTrue(isfile(temp_path.joinpath('carbon.svg')))
        temp.cleanup()

        if __name__ == '__main__':
            main()
