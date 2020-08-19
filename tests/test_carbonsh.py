import asyncio
import platform
import pytest
import tempfile
from os.path import isfile
from unittest import TestCase, main

from carbonsh.Config import Config
from carbonsh.carbonsh import code_to_url, url_to_file


class Test(TestCase):
    def test_code_to_url(self):
        code = 'const test = "testing"'
        expected = 'https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&t=seti&wt=none&l=auto&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=const%20test%20%3D%20%22testing%22'

        self.assertEqual(expected, code_to_url(code, Config()))


class TestPng(TestCase):
    separator = "\\" if platform.system() == 'Windows' else '/'
    @pytest.mark.skip(reason="Cant't test this on CI")
    def test_url_to_file(self):
        url = code_to_url('const test = "testing"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = f'{temp.name}{self.separator}'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, headless=False))
        self.assertTrue(isfile(f'{temp_path}carbon.png'))
        temp.cleanup()

    def test_url_to_file_headless(self):
        url = code_to_url('const test = "testing headless"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = f'{temp.name}{self.separator}'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, headless=True))
        self.assertTrue(isfile(f'{temp_path}carbon.png'))
        temp.cleanup()


class TestSvg(TestCase):
    @pytest.mark.skip(reason="Cant't test this on CI")
    def test_url_to_file(self):
        url = code_to_url('const test = "testing"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = f'{temp.name}{self.separator}'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, extension='svg', headless=False))
        self.assertTrue(isfile(f'{temp_path}carbon.svg'))
        temp.cleanup()

    @pytest.mark.skip(reason="Headless can't make svg")
    def test_url_to_file_headless(self):
        url = code_to_url('const test = "testing headless"', Config())
        temp = tempfile.TemporaryDirectory()
        temp_path = f'{temp.name}{self.separator}'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(url_to_file(url, temp_path, extension='svg', headless=True))
        self.assertTrue(isfile(f'{temp_path}carbon.svg'))
        temp.cleanup()


if __name__ == '__main__':
    main()
