# Model Zoo

## Introduction

The models trained in our baseline are listed below. All models were trained 1 epoch under their respective backbones using the pretrained models provided by [Transformers](https://github.com/huggingface/transformers#model-architectures), [LayoutLM](https://github.com/microsoft/unilm/tree/master/layoutlm#pre-trained-model) and [detectron2](https://github.com/facebookresearch/detectron2).


## Models

The models trained on DocBank are available in the format used by Pytorch. 

|   |   name   |    backbone    |    url   |  size |
|---|:--------:|:--------------:|:--------:|:-----:|
| 0 |   BERT   | BERT-base      | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/bert_base_500k_epoch_1.zip) | 387MB |
| 1 |   BERT   | BERT-large     | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/bert_large_500k_epoch_1.zip) | 1.2GB |
| 2 |  RoBERTa | RoBERTa-base   | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/roberta_base_500k_epoch_1.zip) | 441MB |
| 3 |  RoBERTa | RoBERTa-large  | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/roberta_large_500k_epoch_1.zip) | 1.2GB |
| 4 | LayoutLM | LayoutLM-base  | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/layoutlm_base_500k_epoch_1.zip) | 398MB |
| 5 | LayoutLM | LayoutLM-large | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/layoutlm_large_500k_epoch_1.zip) | 1.2GB |
| 6 | X101 | ResNeXt-101 | [Azure](https://layoutlm.blob.core.windows.net/docbank/model_zoo/X101.zip) | 747MB |


