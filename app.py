import gradio as gr
from generator import generate_post
from caption import generate_caption

def image_captioning_tab(image,theme,tone,platform):
    if image is None:
        return "Please upload an image.", None

    caption=generate_caption(image)
    post=generate_post(theme,tone,platform,image_caption=caption)
    return post,caption

def enhancer_tab(theme,tone,platform):
    post=generate_post(theme,tone,platform)
    return post

def web_image_tab(image_url,theme,tone,platform):
    from PIL import Image
    import requests
    from io import BytesIO

    try:
        response=requests.get(image_url)
        img=Image.open(BytesIO(response.content))
    except Exception as e:
        return f"Error loading image: {e}", None

    caption=generate_caption(img)
    post=generate_post(theme,tone,platform,image_caption=caption)
    return post, caption

with gr.Blocks(title="Social Media Post & Caption Generator") as demo:
    gr.Markdown("## 📸 Social Media Post & Caption Generator")

    with gr.Tab("Image Upload"):
        with gr.Row():
            image_input=gr.Image(type="pil",label="Upload Image")
            with gr.Column():
                theme=gr.Textbox(label="Theme(e.g.,travel,fashion)")
                tone=gr.Dropdown(["Friendly","Professional","Funny","Poetic"],label="Tone")
                platform=gr.Dropdown(["Instagram","Twitter","LinkedIn"],label="Platform")
                generate_btn=gr.Button("Generate Post")
        caption_output=gr.Textbox(label="Image Caption")
        result_output=gr.Textbox(label="Generated Post")
        generate_btn.click(fn=image_captioning_tab,inputs=[image_input,theme,tone,platform],outputs=[result_output,caption_output])

    with gr.Tab("Post Enhancer (Text Only)"):
        with gr.Row():
            theme2=gr.Textbox(label="Theme")
            tone2=gr.Dropdown(["Friendly","Professional","Funny","Poetic"],label="Tone")
            platform2=gr.Dropdown(["Instagram","Twitter","LinkedIn"],label="Platform")
            enhance_btn=gr.Button("Generate Post")
        post_output=gr.Textbox(label="Generated Post")
        enhance_btn.click(fn=enhancer_tab, inputs=[theme2,tone2,platform2],outputs=[post_output])

    with gr.Tab("Image via Web URL"):
        with gr.Row():
            image_url=gr.Textbox(label="Image URL")
            theme3=gr.Textbox(label="Theme")
            tone3=gr.Dropdown(["Friendly","Professional","Funny","Poetic"],label="Tone")
            platform3=gr.Dropdown(["Instagram","Twitter","LinkedIn"],label="Platform")
            web_btn=gr.Button("Generate Post")
        web_caption=gr.Textbox(label="Image Caption")
        web_output=gr.Textbox(label="Generated Post")
        web_btn.click(fn=web_image_tab, inputs=[image_url,theme3,tone3,platform3],outputs=[web_output, web_caption])

demo.launch()
