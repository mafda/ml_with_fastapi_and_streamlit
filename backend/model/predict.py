#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Digits pretrained classifier using ViT.
Source: https://huggingface.co/farleyknight-org-username/vit-base-mnist
"""

import torch
from transformers import AutoModelForImageClassification, ViTImageProcessor

pretrained_model = "farleyknight-org-username/vit-base-mnist"
processor = ViTImageProcessor.from_pretrained(pretrained_model)
model = AutoModelForImageClassification.from_pretrained(pretrained_model)


def classify_digit(img):
    inputs = processor(images=img, return_tensors="pt")
    prob = model(**inputs)
    prob = torch.nn.functional.softmax(prob.logits, dim=1)[0]
    prob = prob.detach().numpy()
    return prob
