import urllib.parse
from pathlib import Path
from typing import Any

from pyppeteer import launch

from .Config import Config

_carbon_url = 'https://carbon.now.sh/'


def code_to_url(code: str, config: Config) -> str:
    code = urllib.parse.quote(code, safe='')
    return f'{_carbon_url}?{config}&code={code}'


async def url_to_file(url: str, location: str, extension='png', headless=False, timeout=2000, **kwargs: Any):
    location = Path(location)

    browser = await launch({'headless': headless}, **kwargs)
    page = await browser.newPage()

    await page.setViewport({'width': 1600, 'height': 1000, 'deviceScaleFactor': 2.0})

    await page.goto(url, {'waitUntil': 'load'})

    if headless:
        export_container = await page.waitForSelector('#export-container')
        element_bounds = await export_container.boundingBox()

        await export_container.screenshot({
            'path': str(location.joinpath('carbon.png')),
            'clip': {
                **element_bounds,
                'x': round(element_bounds['x']),
                'height': round(element_bounds['height']) - 1
            }
        })
    else:
        await page._client.send('Page.setDownloadBehavior', {
            'behavior': 'allow',
            'downloadPath': str(location.joinpath(''))
        })

        save_image_trigger = await page.waitForSelector('#export-menu')
        await save_image_trigger.click()

        png_export_trigger = await page.querySelector('#export-png')
        svg_export_trigger = await page.querySelector('#export-svg')

        if extension == 'png':
            await png_export_trigger.click()
        elif extension == 'svg':
            await svg_export_trigger.click()

        await page.waitFor(timeout)
        await browser.close()


async def code_to_file(code: str, config: Config, location: str, extension='png', headless=False, timeout=2000,
                       **kwargs: Any):
    url = code_to_url(code, config)
    await url_to_file(url, location, extension, headless, timeout, **kwargs)
