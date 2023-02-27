from transformers import AutoFeatureExtractor, ResNetForImageClassification
import torch
import gradio as gr

# load model
feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

def predict(image):
    
    inputs = feature_extractor(image, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    prediction = model.config.id2label[predicted_label]
    return prediction

# setup Gradio interface
title = "Image classifier"
description = "Image classification with pretrained resnet50 model"
examples = ['dog.jpg']
interpretation='default'
enable_queue=True

gr.Interface(
    fn=predict,
    inputs=gr.inputs.Image(),
    outputs=gr.outputs.Label(num_top_classes=1),
    title=title,
    description=description,
    examples=examples,
    interpretation=interpretation,
    enable_queue=enable_queue
).launch()
