import platform
import urllib.parse

from pyppeteer import launch

from .Config import Config

_carbon_url = 'https://carbon.now.sh/'
_directory_separator = "\\" if platform.system() == 'Windows' else '/'


def code_to_url(code: str, config: Config) -> str:
    code = urllib.parse.quote(code, safe='')
    return f'{_carbon_url}?{config}&code={code}'


async def url_to_file(url: str, location: str, extension='png', headless=False, timeout=2000):
    browser = await launch({'headless': headless})
    page = await browser.newPage()

    await page.setViewport({'width': 1600, 'height': 1000, 'deviceScaleFactor': 2.0})

    await page.goto(url, {'waitUntil': 'load'})

    if headless:
        export_container = await page.waitForSelector('#export-container')
        element_bounds = await export_container.boundingBox()

        await export_container.screenshot({
            'path': f'{location}{_directory_separator}carbon.png',
            'clip': {
                **element_bounds,
                'x': round(element_bounds['x']),
                'height': round(element_bounds['height']) - 1
            }
        })
    else:
        await page._client.send('Page.setDownloadBehavior', {
            'behavior': 'allow',
            'downloadPath': f'{location}{_directory_separator}'
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


async def code_to_file(code: str, config: Config, location: str, extension='png', headless=False, timeout=2000):
    url = code_to_url(code, config)
    await url_to_file(url, location, extension, headless, timeout)
