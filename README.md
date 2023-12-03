# Streameth/m3u8 Downloader

This script downloads a bunch of m3u8 video/stream parts. It does it by making a folder for each id, grabbing each of the .ts files, then stringing them back together with ffmpeg.

Usage:
```
python3 downloader.py <video id> <optional: resolution. default: '1080p'>
```

The video ID is this value from the URL in the 'Network' tab for each part:
![How to extract the ID](image.png)

And the resolution (1080p in this case) is also part of that.
