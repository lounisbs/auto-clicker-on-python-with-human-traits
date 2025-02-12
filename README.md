# auto-clicker-on-python-with-human-traits

A simple and configurable autoclicker designed to simulate mouse movements and clicks in a human-like manner. This Python script uses the `pyautogui`, `random`, `time`, and `keyboard` libraries to move the mouse smoothly and perform random clicks within a specified zone at irregular intervals.

## Features

- **Smooth mouse movement:** Uses cosine interpolation to simulate natural mouse movements.
- **Random clicks:** Clicks are made within a defined area around the current mouse position.
- **Random pauses:** Random pauses are inserted between clicks to mimic human behavior.
- **Easy stop:** The script can be stopped at any time by pressing the Esc key.
- **Customization:** Easily adjust the click zone size, click frequency, and pause durations.

## Requirements

- Python 3.x
- The following libraries must be installed: `pyautogui`, `keyboard`

## Installation

1. Clone the repository or download the files.
2. Install the necessary dependencies.
    ```bash
    pip install pyautogui keyboard
    ```
3. Run the script.

## Usage

1. **Run the script:** Once the script is executed, it will give you a 15-second window to position the mouse where you want the clicks to start.
2. **Click zone:** The program clicks randomly within a zone around the current mouse position. This zone is defined by the `zone_size` variable, and you can adjust its size.
3. **Pauses:** The program inserts random pauses between clicks. You can adjust the probabilities and durations of these pauses by modifying the parameters in the code.
4. **Stop:** Press the `Esc` key at any time to stop the program.

## Main Parameters

The parameters of the script can be modified in the code to adjust its behavior:

- `min_delay`: The minimum delay between two clicks (in seconds).
- `max_delay`: The maximum delay between two clicks (in seconds).
- `zone_size`: The size of the zone around the mouse position where clicks can be made.
- `pause_probability1`: The probability of a 10-second pause between actions.
- `pause_probability2`: The probability of a 0.5-second pause between actions.
- `pause1`: Duration of the 10-second pause.
- `pause2`: Duration of the 0.5-second pause.
- `wait_time`: Wait time before starting, allowing you to position the mouse where you want.

## Example Usage

If you want to increase the click zone size and reduce the pauses, you can modify these values in the code:

- Increase the click zone: Set a higher value for `zone_size`.
- Reduce the minimum delay between clicks: Set a lower value for `min_delay`.
- Reduce the maximum delay between clicks: Set a lower value for `max_delay`.
- Fewer long pauses: Decrease `pause_probability1`.
- More short pauses: Increase `pause_probability2`.

## Warnings

- **Ethical usage:** This script is designed for personal automation and in environments where it is allowed. Using it in online games or platforms where it is prohibited may result in penalties. Use this script responsibly.
- **Beware of anti-bot systems:** Anti-bot systems may detect this kind of automation. Make sure to follow the rules of the sites and services you use.

## Contributing

1. Fork this repository.
2. Create a branch for your feature.
3. Commit your changes.
4. Push your changes.
5. Open a pull request.

