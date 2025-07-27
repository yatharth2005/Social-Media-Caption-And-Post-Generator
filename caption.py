from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    inputs=processor(image,return_tensors="pt")
    out=model.generate(**inputs)
    caption=processor.decode(out[0],skip_special_tokens=True)
    return caption
