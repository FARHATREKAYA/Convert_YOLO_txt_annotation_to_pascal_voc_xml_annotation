import os
import xml.etree.ElementTree as ET


# Define class labels
classes = ["Arabic_Box", "Latin_Box", "Number", "Mixed_Box"]

# Define input and output directories
input_dir = "test5"
output_dir = "test5\\testxml"

def convert_txt_to_xml(txt_file):
    file_id = os.path.basename(txt_file)[:-4]
    xml_file = os.path.join(output_dir, file_id + ".xml")

    with open(txt_file, "r") as f:
        lines = f.readlines()

    root = ET.Element("annotation")
    folder = ET.SubElement(root, "folder")
    folder.text = "Annotations"
    filename = ET.SubElement(root, "filename")
    filename.text = file_id + ".jpg"
    size = ET.SubElement(root, "size")
    width_elem = ET.SubElement(size, "width")
    height_elem = ET.SubElement(size, "height")

    # Set width and height values according to your image dimensions
    width_elem.text = "0"
    height_elem.text = "0"

    for line in lines:
        data = line.split()
        class_id = int(data[0])
        x = float(data[1])
        y = float(data[2])
        w = float(data[3])
        h = float(data[4])

        object_elem = ET.SubElement(root, "object")
        name = ET.SubElement(object_elem, "name")
        name.text = classes[class_id]
        bndbox = ET.SubElement(object_elem, "bndbox")
        xmin = ET.SubElement(bndbox, "xmin")
        ymin = ET.SubElement(bndbox, "ymin")
        xmax = ET.SubElement(bndbox, "xmax")
        ymax = ET.SubElement(bndbox, "ymax")

        # Calculate bounding box coordinates based on image dimensions
        width = int(width_elem.text)
        height = int(height_elem.text)

        xmin.text = str(int(x * width))
        ymin.text = str(int(y * height))
        xmax.text = str(int((x + w) * width))
        ymax.text = str(int((y + h) * height))

    tree = ET.ElementTree(root)
    tree.write(xml_file)


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

txt_files = os.listdir(input_dir)
for txt_file in txt_files:
    if not txt_file.endswith(".txt"):
        continue
    txt_path = os.path.join(input_dir, txt_file)
    convert_txt_to_xml(txt_path)
