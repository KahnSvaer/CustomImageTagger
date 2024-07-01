# Custom Image Tagger

A simple custom image annotator tool built with Python using the Tkinter and PIL libraries. This tool allows users to annotate images by providing input values, which are saved to a CSV file.

## Features

- Load and display images from a specified directory.
- Annotate images by entering custom values.
- Save the annotations to a CSV file.
- Skip images without providing annotations.

## Prerequisites

- Python 3.x
- Tkinter
- Pillow (PIL)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/custom-image-annotator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd custom-image-annotator
    ```

3. Install the required dependencies:

    ```bash
    pip install Pillow
    ```

## Usage

1. Update the file paths in the script as needed:

    - `FILE_PATH`: Path to the CSV file where annotations will be saved.
    - `IMAGE_PATH`: Path to the directory containing the images to be annotated.

2. Run the script:

    ```bash
    python annotator.py
    ```

3. Use the GUI to annotate images:
    - The image will be displayed in the main window.
    - Enter the annotation value in the provided entry field.
    - Click "Save" to save the annotation and move to the next image.
    - Click "Skip" to move to the next image without saving an annotation.

## Example

Here's a simple example of how to set up the file paths and run the annotator:

```python
FILE_PATH = "../ImageFiles/num_lanes_test.csv"
IMAGE_PATH = "../ImageFiles/direct_site_images"
```
Then run the Python script

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
