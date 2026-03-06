import gradio as gr
import os

def file_copy_gradio(input_file):
    try:
        # Read uploaded file
        with open(input_file.name, "r", encoding="utf-8") as f:
            content = f.read()

        # Modify content
        modified_content = content.title()

        # Write to output file
        output_path = "output.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(modified_content)

        return output_path

    except Exception as e:
        return f"Error: {e}"


iface = gr.Interface(
    fn=file_copy_gradio,
    inputs=gr.File(label="Upload a text file"),
    outputs=gr.File(label="Download processed file"),
    title="Dynamic File Processing App",
    description="Upload a text file and download the title-cased version."
)

if __name__ == "__main__":
    iface.launch()
