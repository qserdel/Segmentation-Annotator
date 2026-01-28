# Segmentation Annotator

This repository is a fork from https://github.com/unmannedlab/Segmentation-Annotator. It contains a segmentation annotator tool that allows you to annotate images for segmentation tasks. The tool was used to annotate [The Great Outdoors Dataset](http://www.unmannedlab.org/the-great-outdoors-dataset/).

## Features

- Super Pixelation
- Auto "SAM" Masks
- Interactive SAM masks
- Rectangle SAM mask
- Coarse OFFseg segmentation
- Manual Polygon

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/qserdel/Segmentation-annotator.git
    ```

2. Install the required dependencies: 

    ```bash
    pip install -r requirements.txt
    ```

3. Install SAM package

    ```bash
    cd segment-anything; pip install -e .
    ```
Download the [SAM checkpoint](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth) and update the path in [gui.py](./gui.py) Line:50.

#### If you are facing issues with generating SAM prompts/rectangles due to computation constraints. Please use the SAM base model [SAM-base](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth) for faster SAM inference.

## Usage

1. Run the annotator tool:

    ```bash
    python gui.py
    ```

2. Load an image folder and start annotating.

3. Suggested image segmentation pipeline: 
    - Start by clicking on the _Generate Superpixels_ button
    - Allocate the most represented label in each superpixel for a coarse segmentation
    - Refine the annotation using the interactive SAM feature
    Note: you can click in multiple place after clicking on the _Interact with SAM_ button to refine its segmentation

4. Click "Save" to export the original image, labeled image and colored label image in the "outputs" folder.

When opeining a folder, only images with names not already present in the outputs/images folder will be loaded to the segmentation tool.

## Custom Dataset
To annotate your custom dataset with your own custom labels, please refer to [custom_annotations_readme.md](./custom_annotations_readme.md)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 
##### Contact: kasiv@tamu.edu
### We will release a new update with the integration of SAM 2 for faster video annotations. Stay tuned!

### Upcoming

- A zoom feature
- A free painting tool

## License

This project is licensed under the [MIT License](LICENSE).
