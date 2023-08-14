# Convert YOLO TXT to PASCAL VOC XML
This code converts YOLO TXT format to PASCAL VOC XML format. It can be used to convert annotations for object detection datasets from one format to another.
## Usage

To use this code, you will need to have the following Python libraries installed:
* `os`
* `xml.etree.ElementTree`

Once you have installed the required libraries, you can use the following steps to convert your annotations:
1. Create a directory to store your converted annotations.
2. Create a directory to store your converted annotations.
```rb
python convert_txt_xml.py <input_dir> <output_dir>
```
where `<input_dir>` is the directory containing your COCO TXT annotations and <output_dir> is the directory where you want to store your converted annotations.

## Example

The following example shows how to convert the COCO TXT annotations in the `data` directory to PASCAL VOC XML annotations in the `output` directory:
```rb
python convert_txt_xml.py data output
```

## Output
The output of this code will be a PASCAL VOC XML file for each image in the input directory. The XML files will contain the following information:

* The image filename
* The image width and height
* The bounding boxes for each object in the image
* The class labels for each object
## License
This repository is licensed under the MIT License.

## Author
This repository was created by Farhat Rekaya.
