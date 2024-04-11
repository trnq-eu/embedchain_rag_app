import os
import gradio as gr
from dotenv import load_dotenv
from embedchain import App
import openai

load_dotenv()

prompt = gr.Textbox()
openai_key = os.getenv("OPEN_AI_KEY")
os.environ["OPENAI_API_KEY"] = openai_key



def process_input(prompt):
    app = App.from_config(config_path="config.yaml")
    app.add('data/Archivio-Storico-CSP.pdf', data_type='pdf_file')
    # Your processing logic using the OpenAI key and the uploaded file
    response = app.query(prompt)
    return response

interface = gr.Interface(
    fn=process_input,
    inputs=[prompt],
    outputs="text",
    title="Gradio Embedchain RAG App",
    description="Fammi una domanda sui documenti caricati",
)

interface.launch()