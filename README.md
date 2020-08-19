# carbonsh

Python module for carbon.now.sh

## Install

```shell script
pip install carbonsh
```
** *[pyppeteer](https://pyppeteer.github.io/pyppeteer/) requires to download Chromium the first time you use it, go to its documentation for more information*
## Usage

```python
import carbonsh
import asyncio
code = ("const test = 'test';"
        "let x = 0.1 + 0.2;"
        "console.log(test, x)")

config = carbonsh.Config(language=carbonsh.languages.JAVASCRIPT)

# returns >>> 'https://carbon.now.sh/?bg=rgba(...'
carbon_url = carbonsh.code_to_url(code, config)

loop = asyncio.get_event_loop()

# saves the image as carbon.png where expected
loop.run_until_complete(carbonsh.url_to_file(carbon_url, '/path/to/save/screenshot/'))

loop.run_until_complete(carbonsh.code_to_file(code,config,'/path/to/save/screenshot/'))
```