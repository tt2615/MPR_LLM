# MPRLLM

This repository is the implementation of the method MPR-LLM for the paper "MRP-LLM: Multitask Reflective Large Language Models for Privacy-Preserving Next POI Recommendation".

## Introduction

MRP-LLM is a LLM-based next POI recommender system with privacy protection in place.

## Environment Requirements
1. openai==1.3.3
2. numpy==1.26.4
3. pandas==2.2.2
4. tqdm==4.62.3

## Dataset

A sample of the dataset is uploaded to https://drive.google.com/drive/folders/1givcu_t0IBtNZIa4BODKYLR2INWMIl62?usp=sharing

## Running Instructions
If you want to run MPR-LLM with New York Dataset, run:
```
python main.py -d nyc
```

If you want to run MPR-LLM with Singapore Dataset, run:
```
python main.py -d sin
```

If you want to run MPR-LLM with Phoenix Dataset, run:
```
python main.py -d pho
```

