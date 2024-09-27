"""
==========================
!! Educational use only !!
==========================
"""

import json
import pathlib
import urllib.request
from urllib.parse import urlparse
from multiprocessing import Pool
import os

BUCKET_FILE_PATH = "bucket.json"
WALLPAPERS_DIR_PATH = "wallpapers/"


def extract_image_name(url: str) -> str:
    url_path: str = urlparse(url).path
    last_slash_index = url_path.rfind("/")
    image_name = url_path[last_slash_index + 1 :]
    image_name = image_name.replace("~", "-")
    return image_name


def get_nested_values(d: dict):
    values = []
    for value in d.values():
        if isinstance(value, dict):
            values.extend(get_nested_values(value))
        else:
            values.append(value)
    return values


def extract_image_urls(filepath: str) -> list[str]:
    raw_bucket = pathlib.Path(filepath).read_text()
    bucket = json.loads(raw_bucket)
    data: dict = bucket["data"]
    urls = get_nested_values(data)
    return urls


def filter_image_urls(image_urls: list[str]) -> list[str]:
    blacklist = ["artists", "feature-banner", "crop"]
    return [
        url for url in image_urls if all(keyword not in url for keyword in blacklist)
    ]


def ensure_wallpapers_dir():
    wallpapers_dir = pathlib.Path(WALLPAPERS_DIR_PATH)
    if not wallpapers_dir.exists():
        wallpapers_dir.mkdir()


def download_wallpaper(url: str):
    """Downloads wallpaper from given URL. If download fails, will automatically reattempt until successful download."""
    wallpaper_name = extract_image_name(url)
    print(f"Downloading {wallpaper_name}..")

    max_retries = 5
    for _ in range(max_retries):
        try:
            urllib.request.urlretrieve(url, f"{WALLPAPERS_DIR_PATH}{wallpaper_name}")
            print(f"Downloaded {wallpaper_name}!")
            break
        except Exception:
            print(f"An error occurred downloading {wallpaper_name}. Trying again.")
    else:
        print(f"{wallpaper_name} failed to download after {max_retries} attempts.")


if __name__ == "__main__":
    ensure_wallpapers_dir()

    wallpaper_urls = extract_image_urls(BUCKET_FILE_PATH)
    wallpaper_urls = filter_image_urls(wallpaper_urls)

    pool = Pool(os.cpu_count())
    pool.map(download_wallpaper, wallpaper_urls)
