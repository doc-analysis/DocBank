**DocBank dataset samples**

We use the original pdf name as the prefix and the page index starts from 0.

Every sample is consist of six files:

- {prefix}_color.pdf: The pdf file generated after changing the structures' font colors to the structure-specific colors.
- {prefix}_black.pdf: The pdf file generated after changing the structures' font colors to black, similar to the original pdf.
- {prefix}_{page_index}.jpg: The image of the page in the "_color.pdf".
- {prefix}_{page_index}_ori.jpg: The image of the page in the "_black.pdf".
- {prefix}_{page_index}_ann.jpg: The annotation diagram of this sample page.

The previous five files are given for the visualization purpose, the following file is the only file the model need.
- {prefix}_{page_index}.txt: The annotation of this sample page.
