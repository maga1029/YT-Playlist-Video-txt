# YT-Playlist-Video-txt

A Python script to extract video titles and URLs from a YouTube playlist and save them into a text file.

## Features

- Extracts video titles and URLs from any public YouTube playlist.
- Saves the playlist data in a `.txt` file for easy access and sharing.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries (see [Installation](#installation))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maga1029/YT-Playlist-Video-txt.git
   cd YT-Playlist-Video-txt
   ```

2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pytube
   ```

## Usage

1. Run the script:
   ```bash
   python yt_playlist_video_txt.py
   ```

2. Enter the URL of the YouTube playlist when prompted.

3. The script will generate a `playlist.txt` file in the same directory, containing the video titles and URLs.

## Example Output

Sample `playlist.txt` file:
```
1. Video Title 1 - https://www.youtube.com/watch?v=example1
2. Video Title 2 - https://www.youtube.com/watch?v=example2
3. Video Title 3 - https://www.youtube.com/watch?v=example3
...
```

## Notes

- The script works only for public YouTube playlists.
- Ensure you have a stable internet connection when running the script.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by the need for easily sharing YouTube playlist information.

---

Feel free to customize this file further based on additional details about your project!
