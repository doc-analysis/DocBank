# DocBank

**\*\*\*\*\* This work is still in progress and the data will be released soon \*\*\*\*\***

DocBank is a new large-scale dataset that is constructed using a weak supervision approach. It enables models to integrate both the textual and layout information for downstream tasks. The current DocBank dataset totally includes 5,253 documents. **As this work is still in progress, DocBank will be further enlarged in the next version very soon**

## Introduction

For document layout analysis tasks, there have been some image-based document layout datasets, while most of them are built for computer vision approaches and they are difficult to apply to NLP methods. In addition, image-based datasets mainly include the page images and the bounding boxes of large semantic structures, which are not fine-grained token-level annotations. Moreover, it is also time-consuming and labor-intensive to produce human-labeled and fine-grained token-level text block arrangement. Therefore, it is vital to leverage weak supervision to obtain fine-grained labeled documents with minimum efforts, meanwhile making the data be easily applied to any NLP and computer vision approaches. 

To this end, we build the DocBank dataset, a  document-level  benchmark with fine-grained token-level annotations for layout  analysis. Distinct from the conventional human-labeled datasets, our approach obtains high quality annotations in a simple yet effective way with weak supervision.

## License
DocBank is released under the [Attribution-NonCommercial-NoDerivs License](https://creativecommons.org/licenses/by-nc-nd/4.0/). You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may not use the material for commercial purposes. If you remix, transform, or build upon the material, you may not distribute the modified material.

## Paper and Citation
https://arxiv.org/abs/2006.01038
```
@misc{li2020docbank,
    title={DocBank: A Benchmark Dataset for Document Layout Analysis},
    author={Minghao Li and Yiheng Xu and Lei Cui and Shaohan Huang and Furu Wei and Zhoujun Li and Ming Zhou},
    year={2020},
    eprint={2006.01038},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
