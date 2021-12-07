import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import json
from pprint import PrettyPrinter as pprint
from IPython.display import JSON
import re
from tqdm import tqdm
import traceback

class COCOData:
    """
        COCOData class allows DocBank dataset to be converted to COCO Format.

        Functions Available:

        1. read_src_folder(src_path, dest_path): Reads all the DocBank JSON label files from the provided parent path and stores the destination path for later use to save the converted labels.
        2. create_dict_layout(): Creates a basic layout for COCO format with basic static information.
        3. set_image_properties(file_name, image_id): Sets Image Properties. Used in convert_to_coco() function.
        4. set_caption_properties(object_dict, doc_object): Set Caption Properties. Used in set_object_properties() function.
        5. set_object_properties(doc_object, doc_object_id, image_id): Set the Object properties. Used in convert_to_coco() function.
        6. convert_to_coco(): Convert the source dataset to COCO format and store the converted data in coco_dictionary.
        7. save_coco_dataset(): Saves the converted dataset into the destination folder (Destination Folder was provided in read_src_folder function).
    """
    

    
    def __init__(self):
        self.src_file_path = []
        self.coco_file_path = []
        self.src_dictionary = []
        self.coco_dictionary = []
    
    def read_src_folder(self, src_path, dest_path):
       """
       Stores the full path of the JSON files into self.src_file_path
       Stores the content of the source JSON files into self.coco_dictionary
       Stores the full path to the new files (in COCO format)
       """
       i=0
       # Fetch each text file from the folders
       for path in tqdm(Path(src_path).rglob('*.txt'), desc="Loading Source Files"):
            # Open the file and read the content in JSON datatype
            file = pd.read_table(path, header=None, names=["token", "x0","y0", "x1", "y1", "R", "G","B", "name", "label"])
            
            # Prepare string for coco format json file
            coco_file_path = str(path).replace(".txt", ".json")
            coco_file_path = coco_file_path.replace(src_path, dest_path)

            self.src_file_path.append(str(path))
            self.src_dictionary.append(file)
            self.coco_file_path.append(str(coco_file_path))

    def create_dict_layout(self):
        temp_dict = {}
        temp_dict["info"] = {
            "year": "",
            "version": "1",
            "description": "",
            "contributor": "",
            "url": "",
            "date_created": "",
        }
        temp_dict["licenses"] = []
        
        ['abstract',
         'author',
         'caption',
         'equation',
         'figure',
         'footer',
         'list',
         'paragraph',
         'reference',
         'section',
         'table',
         'title']
        temp_dict["categories"] = [{"id": 0,"name": "Abstract","supercategory": ""},{"id": 1,"name": "Author","supercategory": ""},
            {"id": 2,"name": "Caption","supercategory": ""},{"id": 3,"name": "Equation","supercategory": ""},
            {"id": 4,"name": "Figure","supercategory": ""},{"id": 5,"name": "Footer","supercategory": ""},
            {"id": 6,"name": "List","supercategory": ""},{"id": 7,"name": "Paragraph","supercategory": ""},
            {"id": 8,"name": "Reference","supercategory": ""},{"id": 9,"name": "Section","supercategory": ""},
            {"id": 10,"name": "Table","supercategory": ""},{"id": 11,"name": "Title","supercategory": ""},
            {"id": 12,"name": "Date","supercategory": ""}]
        temp_dict["images"] = []
        temp_dict["annotations"] = []
        
        return temp_dict
    
    # Image denotes the image of a page where a set of objects exist
    def set_image_properties(self, file_name, image_id):
        # Get parent folder and the json file name separately.
        image_path, image_name = os.path.split(file_name)
        image_dict = {
            "id": image_id,
            "license": "",
            "file_name": image_name,
            "height": "",
            "width": "",
            "date_captured": "",
        } 
        return image_dict
     
    # Object denotes either a Table or Figure
    def set_object_properties(self, doc_object, doc_object_id, image_id):
        object_dict = {}
        object_dict["id"] = doc_object_id
        object_dict["image_id"] = image_id
        object_dict["iscrowd"] = 0
        object_dict["segmentation"] = []
        
        category_list = {
            'abstract': 0, 'author': 1, 'caption': 2, 'equation': 3, 'figure': 4, 'footer': 5, 
             'list': 6, 'paragraph': 7, 'reference': 8, 'section': 9, 'table': 10, 'title': 11, "date": 12}
            
        object_dict["category_id"] = category_list[doc_object[9]]
        object_width = doc_object[3] - doc_object[1],
        object_height = doc_object[4] - doc_object[2],
        
        object_dict["bbox"] = [
            int(doc_object[1]),
            int(doc_object[2]),
            int(object_width[0]),
            int(object_height[0])
        ]
        object_dict["area"] = int(object_width[0] * object_height[0]) 
        
        return object_dict
    
    def set_caption_properties(self, object_dict, doc_object):
        object_dict["caption"] = doc_object["caption_text"]
                               
    def convert_to_coco(self):
        try:
            # Init Image ID
            image_id = 0
            # Init Object ID
            doc_object_id = 0

            # Fetch each JSON file present in the folders
            for i in tqdm(range(len(self.src_file_path)), desc="Convering Source JSON to COCO JSON"):
                json_dict = self.create_dict_layout()
                image_dict = self.set_image_properties(os.path.split(self.coco_file_path[i])[1].replace(".json", ".jpg"), image_id)
                
                # Each Image present in the file is fetched and added to a cocoData object
                for doc_object in self.src_dictionary[i].values:
                    object_dict = self.set_object_properties(doc_object, doc_object_id, image_id)
                    # Add the object properties to the annotations key in COCO
                    json_dict["annotations"].append(object_dict)
                    # Increment the object ID for next annotated object in the file
                    doc_object_id += 1

                # Increment the Image ID for the next Image in the file
                image_id+=1
                # Extract Image width and height if annotations exist. There has to be atleast one annotation for an image to have the dimension attributes.
                json_dict["images"].append(image_dict)
                self.coco_dictionary.append(json_dict)
        except:
            traceback.print_exc()

    # Converts final dictionary in COCO format for storing into file.
    def save_coco_dataset(self):
        try:
            for i in tqdm(range(len(self.coco_file_path))):
                coco_file_dir = os.path.split(self.coco_file_path[i])[0]
                if not os.path.exists(coco_file_dir):
                    # Creates the parent folder and all the subfolders for the file.
                    #   Does not throw an error if parent or any subfolders already exists.
                    Path(coco_file_dir).mkdir(parents=True, exist_ok=True)

                output_file = open(self.coco_file_path[i], mode="w")
                output_file.writelines(json.dumps(self.coco_dictionary[i], indent=4))
        except:
            traceback.print_exc()
        # finally:
        #     # output_file.close()
