from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME="microsoft/phi-2"

tokenizer=AutoTokenizer.from_pretrained(MODEL_NAME)
model=AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

def generate_post(theme,tone,platform,image_caption=None):

    prompt=f"Write a {tone.lower()}social media post for {platform} about {theme}."
    if image_caption:
        prompt+=f" The post should be based on this image caption: '{image_caption}'."
    prompt+=" Include appropriate emojis and hashtags."

    inputs=tokenizer(prompt,return_tensors="pt",truncation=True)
    with torch.no_grad():
        outputs=model.generate(**inputs,max_new_tokens=100,do_sample=True,temperature=0.7)
    generated_text=tokenizer.decode(outputs[0],skip_special_tokens=True)

    return generated_text.replace(prompt, "").strip()
