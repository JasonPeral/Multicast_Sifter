# Multicast Sifter

A simple Python script that plays a list of multicast streams one at a time using VLC and allows you to verify their playback. After verifying each stream, you can press Enter to move to the next stream in the list. The script will loop through the list of multicast streams indefinitely.

## Features
- Plays multicast streams using VLC.
- Allows switching between streams by pressing Enter.
- Loops through the streams once all have been verified.
- Gracefully handles keyboard interrupts to exit.

## Requirements
- Python 3.x
- VLC installed on your system
- `subprocess` module (standard in Python)
- List of multicast streams (modify the `multicast_streams` list with your own URLs)
