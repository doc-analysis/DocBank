# Convert DocBanks annotation files to COCO format
This repo contains code files that can be used to extract the standard COCO format annotations from [DocBank](https://github.com/doc-analysis/DocBank).

The class COCODataset contains various methods which allow the user to read, display, convert the json files into coco format. Later, you can choose to store the coco json files into your disk based on the input you give. 

# Usage
1. Import and Usage
```
from DocbankToCOCO import COCOData

coco = COCOData()
```

2. Read Source Files and Parse
```
coco.read_src_folder(<source_parent_folder>, <destination_saving_folder>)
```

3. Convert to COCO Format
```
coco.convert_to_coco()
```

4. Save converted annotations to the destination directory (Directory path was given in read_src_folder function)
```
coco.save_coco_dataset()
```

View Source Dataset
```
coco.src_dictionary
```

View Converted Dataset
```
coco.coco_dictionary
```

