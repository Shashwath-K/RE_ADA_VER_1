import streamlit as st
import PyPDF2
import os
from datetime import datetime

log_file = "streamlit_actions.txt"

def write_log(message):
    with open(log_file,"a") as file:
        file.write(f"{datetime.now()}-{message}\n")

st.title("PDF Processing Dashboard")
option = st.selectbox("Choose Operation", ["Merge PDFs", "Rename PDF"])

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if option == "Merge PDFs":
    if st.button("Merge"):
        if len(uploaded_files) >=2:
            merger = PyPDF2.PdfMerger()
            for pdf in uploaded_files:
                merger.append(pdf)
            
            output_file = "mergerd_file.pdf"
            with open(output_file, "wb") as file:
                merger.write(f)
            
            write_log("PDFs merged successfully")
            st.success("Merged Successfully")
        else:
            st.error("Please upload at least two PDFs")

if option == "Rename PDF":
    if uploaded_files:
        new_name = st.text_input("Enter New file name excluding the PDF extension")

        if st.button("Rename"):
            if new_name:
                pdf_file = uploaded_files[0]
                output_path = f"{new_name}.pdf"

                with open(output_path, "wb") as f:
                    f.write(pdf_file.read())

                write_log("PDF renamed successfully")
                st.success("Renamed successfully")
            else:
                st.error("Please enter a valid file name")