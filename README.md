# Panels Scraper

> [!CAUTION]
> This project is purely for educational use. All art/wallpapers are protected by US Copyright law, and property of Panels Wallpaper Mobile App LLC. Do NOT use this to gain access to wallpapers illicitly.

[Panels](https://panels.art) was meant to be a premium wallpaper site by MKBHD. X users quickly discovered flaws in the app's design, exposing premium wallpapers to the public. Images are hosted on a publicly available google bucket.

**I will not be providing the link directly**, though the related X thread is linked at the bottom.

## Educational use steps
1. Clone repo, cd into it
2. Download a file in the same format of the Panels bucket[^1]
3. Rename it `bucket.json` & move it into the same directory of this script
4. Run this script with `python scrapers.py`

## Multiprocessing
This script downloads the wallpapers in parallel via multiprocessing

| Processes | Seconds |
|-----------|---------|
| Single    | 105     |
| Multi     | 21      |

**~80%** speed increase!

## Credit
The following "Xeet" details more about the publicly available bucket

https://x.com/uwukko/status/1838640935770440031

[^1]: To reiterate: download a file *in the same format* as the Panels bucket. Not the actual response from the Panels bucket
