import os
import gradio as gr

from embedchain import App

def process_input(openai_key, uploaded_file):
    os.environ["OPENAI_API_KEY"] = openai_key
    app = App.from_config(config_path="config.yaml")
    # Your processing logic using the OpenAI key and the uploaded file
    return "Processed result"

openai_key_input = gr.Textbox(label="OpenAI Key", type="password")
upload_button = gr.UploadButton(label="Upload File")

interface = gr.Interface(
    fn=process_input,
    inputs=[openai_key_input, upload_button],
    outputs="text",
    title="OpenAI Key and File Upload",
    description="Enter your OpenAI key and upload a file to process.",
)

interface.launch()
