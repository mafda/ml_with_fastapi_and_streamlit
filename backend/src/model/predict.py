"""
Digits pretrained classifier using ViT.
Source: https://huggingface.co/farleyknight-org-username/vit-base-mnist
"""

import torch
from transformers import AutoModelForImageClassification, ViTImageProcessor

pretrained_model = "farleyknight-org-username/vit-base-mnist"

# Create a ViT image processor for the pretrained model
processor = ViTImageProcessor.from_pretrained(pretrained_model)

# Load the pretrained ViT model for image classification
model = AutoModelForImageClassification.from_pretrained(pretrained_model)


def classify_digit(img):
    """
    Classify a given image of a digit using the pretrained ViT model.

    Args:
        img (PIL.Image.Image): The input image to be classified.

    Returns:
        A numpy array of probabilities for each digit class (0-9).
    """
    # Preprocess the input image using the image processor
    inputs = processor(images=img, return_tensors="pt")

    # Pass the preprocessed inputs through the model
    prob = model(**inputs)

    # Softmax the model output to get probabilities for each class
    prob = torch.nn.functional.softmax(prob.logits, dim=1)[0]

    # Detach from the computational graph and convert to numpy array
    prob = prob.detach().numpy()

    return prob
