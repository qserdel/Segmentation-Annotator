# Segmentation Annotator

This repository is a fork from https://github.com/unmannedlab/Segmentation-Annotator. It contains a segmentation annotator tool that allows you to annotate images for segmentation tasks. The tool was used to annotate [The Great Outdoors Dataset](http://www.unmannedlab.org/the-great-outdoors-dataset/).

## Features

- Super Pixelation
- Auto "SAM" Masks
- Interactive SAM masks
- Rectangle SAM mask
- Coarse OFFseg segmentation
- Manual Polygon
- Hand Painting

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
    - Refine the annotation using the interactive SAM feature.
    (Note: you can click in multiple place after clicking on the _Interact with SAM_ button to refine its segmentation)
    - When SAM struggles to capture elements, you can use the hand painting tool 
        - first select a label, then click on _Hand Paint_
        - you can zoom in the image by scrolling and pan by pressing the wheel button (feature to be improved)


4. Click "Save" to export the original image, labeled image and colored label image in the "outputs" folder.

When opeining a folder, only images with names not already present in the outputs/images folder will be loaded to the segmentation tool.

## Custom Dataset
To annotate your custom dataset with your own custom labels, please refer to [custom_annotations_readme.md](./custom_annotations_readme.md)

## Changelog from original repository

- Added transparency between color labels and original image for better visualisation during annotation
- Updated the layout to support window resizing without overlapping elements
- Changed the saving procedure (don't delete the images from original folder but check presence in the outputs instead)
- Unlabeled pixels are now automatically given the 0 label_id, removed the 100\% pixel annotation condition to save the results
- Added _Previous Image_ and _Next Image_ buttons
- Updated the README (obviously)
- A zoom feature
- A free painting tool
- TODO: debug and improve pan and zoomed painting

## License

This project is licensed under the [MIT License](LICENSE).
