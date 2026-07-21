# WriteNoise

Turn a `.wav` file into an image, and back again — a HackGT hack that encodes sound as pixels.

![Python](https://img.shields.io/badge/python-3-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-1.1.2-black?logo=flask&logoColor=white)
![License: CC BY 3.0](https://img.shields.io/badge/license-CC--BY--3.0-lightgrey)

## Demo / Screenshot

<!-- add screenshot here -->

Sample input/output pair from the encoder is included in the repo: [`input.wav`](input.wav) → [`output.png`](output.png).

## Features

- **One-to-one `.wav` → `.png` conversion** — every 16-bit audio sample is packed bit-by-bit into the RGBA channels of a pixel, so the image can (in principle) be decoded back into sound
- **Reverse decoder** (`pngToWav.py`) that reconstructs a waveform from a previously-generated image
- **Web front end** (Flask) where you upload a `.wav` file in the browser and get the generated image back
- **Signal analysis utilities** — average amplitude of local maxima (`averageAmplitude.py`), dominant frequency via pitch detection (`frequency.py`), and musical key detection via `music21`/`aubio` (`keyFinder.py`)
- **Exploratory Jupyter notebook** (`HackGT Soundwave test.ipynb`) used to prototype the waveform-plotting and encoding logic
- Ships with a `Procfile` for one-command deployment to Heroku (`gunicorn app:app`)

## Tech Stack

- **Backend:** Python 3, [Flask](https://flask.palletsprojects.com/), [Gunicorn](https://gunicorn.org/)
- **Audio/DSP:** `scipy.io.wavfile`, `numpy`, `aubio`, `music21`
- **Imaging:** `Pillow`, `matplotlib`
- **Front end:** HTML/CSS/jQuery (based on the [Stellar](https://html5up.net/stellar) template by HTML5 UP)

## Getting Started

### Prerequisites

- Python 3.7+
- `pip`

### Install

```bash
git clone <this-repo-url>
cd WriteNoise
pip install -r requirements.txt
```

> Note: `keyFinder.py` additionally depends on `music21`, `aubio`, and `wav2midi2wav`, which are not in `requirements.txt`. Install them separately if you want to use key/frequency detection.

### Run the web app

```bash
python app.py
```

This starts the Flask dev server (defaults to `http://127.0.0.1:5000`). To run it the way Heroku does:

```bash
gunicorn app:app
```

## Usage

1. Open the app in your browser and navigate to the upload page (`/generic`).
2. Upload a `.wav` file.
3. The server encodes the audio samples into a 300×300 RGBA image and saves it as `output.png`.

To decode a generated image back into audio, edit `pngToWav.py` to point at your image and run:

```bash
python pngToWav.py
```

This writes the reconstructed audio to `reverse2.wav`.

Standalone analysis scripts can be run directly, e.g.:

```bash
python averageAmplitude.py   # average amplitude of local maxima in a waveform
python keyFinder.py          # detect the musical key of a .wav file
```

## Architecture

```
 .wav file --[app.py: wavtoPNG]--> bit-packed RGBA image (output.png)
                                          |
                                          v
 reverse2.wav <--[pngToWav.py: dumberBinary]-- image pixels
```

`app.py` is a small Flask server with two routes: `/` renders the landing page, and `/generic` accepts a file upload, saves it as `input.wav`, and calls `wavtoPNG`. That function reads the waveform with `scipy.io.wavfile`, converts each 16-bit sample to binary, and scatters specific bits across the R, G, and B channels of a 300×300 image (`stupidBinary`), with the sign of the sample encoded in the alpha channel. `pngToWav.py` (`dumberBinary`) performs the inverse mapping, reading pixel channels back out and reassembling them into sample values.

The `averageAmplitude.py`, `frequency.py`, and `keyFinder.py` scripts are independent DSP utilities exploring other properties of an audio signal (amplitude envelope, dominant pitch, and musical key) and aren't wired into the Flask app.

## Configuration

- No environment variables are required to run the app locally.
- `Procfile` defines the Heroku process: `web: gunicorn app:app`.
- The encoder currently hardcodes the output image size to `300x300` and reads/writes fixed filenames (`input.wav`, `output.png`) — swap these in `app.py` if you need different behavior.

## Contributing

Contributions are welcome — feel free to open an issue or submit a pull request with a clear description of the change and, where applicable, before/after examples of the audio-to-image conversion.

## License

The front-end template (Stellar by HTML5 UP) is licensed under [Creative Commons Attribution 3.0](LICENSE.txt). See `LICENSE.txt` for the full text.
