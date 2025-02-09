import streamlit as st
import pandas as pd
import requests
from io import BytesIO
from fpdf import FPDF
import plotly.express as px
import json

# Set Page Configuration (default layout)
st.set_page_config(page_title="Crane Comparison & Decision Support Tool")

# Azure OpenAI LLM Credentials
azure_endpoint = st.secrets["AZURE_ENDPOINT"]
api_key = st.secrets["API_KEY"]
api_version = st.secrets["API_VERSION"]
model = st.secrets["MODEL"]

# LLM Query Function
def query_llm(prompt):
    """Sends a query to the Azure OpenAI GPT-4 API and retrieves a response."""
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
    }
    try:
        response = requests.post(
            f"{azure_endpoint}/openai/deployments/{model}/chat/completions?api-version={api_version}",
            headers=headers,
            data=json.dumps(payload),
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# Generate PDF Report
def generate_pdf(data, recommendation):
    """Generates a PDF report containing crane comparison data and recommendations."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Crane Comparison Report", ln=True, align="C")
    pdf.ln(10)

    # Add Crane Data
    pdf.set_font("Arial", size=10)
    for index, row in data.iterrows():
        pdf.cell(200, 10, txt=str(row.to_dict()), ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Recommendation:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, recommendation)

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S').encode('latin1'))  # Write PDF content to BytesIO object
    pdf_output.seek(0)  # Reset file pointer to the beginning
    return pdf_output

# Streamlit App
def main():
    st.title("Crane Comparison & Decision Support Tool")

    # Information Button
    if st.sidebar.button("ℹ️ How to Use This App"):
        st.sidebar.info("""
        **Step-by-Step Guide:**
        1. **Upload Crane Dataset**: Upload your crane dataset in CSV format.
        2. **Input Requirements**: Enter the load weight, wind speed, and radius.
        3. **Get Recommendations**: Click the button to get crane recommendations.
        4. **View Results**: See the filtered crane data and recommendations.
        5. **Download Report**: Download the PDF report with detailed information.
        """)

    # Sample Data Download Button
    sample_data_url = "https://drive.google.com/uc?export=download&id=1pCXYaS6pM-DJzsjLi5Gqm6cKLjZbPJYv"
    if st.sidebar.button("📥 Download Sample Data"):
        st.sidebar.markdown(f'<a href="{sample_data_url}" download="sample_crane_data.csv">Click here to download the sample data</a>', unsafe_allow_html=True)

    # File Upload
    st.sidebar.header("Upload Crane Dataset")
    uploaded_file = st.sidebar.file_uploader(
        "Upload your crane dataset (CSV format)", type=["csv"]
    )

    if uploaded_file is not None:
        # Load the uploaded dataset
        try:
            cranes = pd.read_csv(uploaded_file)
            st.sidebar.success("File uploaded successfully!")
        except Exception as e:
            st.sidebar.error(f"Error loading file: {e}")
            return
    else:
        st.info("Please upload a crane dataset to proceed.")
        return

    # Sidebar Input
    st.sidebar.header("Input Crane Requirements")
    load_weight = st.sidebar.number_input("Load Weight (tons)", min_value=0, step=1)
    wind_speed = st.sidebar.number_input("Wind Speed (m/s)", min_value=0, step=1)
    radius = st.sidebar.number_input("Radius (meters)", min_value=0, step=1)

    # Input Validation
    if st.sidebar.button("Get Recommendations"):
        if load_weight == 0 or wind_speed == 0 or radius == 0:
            st.sidebar.error("Please provide valid inputs.")
        else:
            # Query LLM for Recommendations
            prompt = f"""
            You are an expert in crane operations and safety. Based on the following crane specifications:
            {cranes.to_dict(orient='records')},
            recommend the best crane(s) for lifting {load_weight} tons under {wind_speed} m/s wind speed at a radius of {radius} meters.

            Please consider the following factors in your recommendation:
            1. **Safety**: Ensure the crane can operate safely under the specified conditions.
            2. **Efficiency**: Choose cranes that can perform the task efficiently.
            3. **Cost-effectiveness**: Consider the cost of operation and maintenance.
            4. **Durability**: Evaluate the durability and reliability of the cranes.
            5. **Compliance**: Ensure the cranes comply with relevant regulations and standards.

            Provide a detailed reasoning for your recommendation, including:
            - The specific features of the recommended cranes that make them suitable for the task.
            - Any potential risks or limitations associated with the recommended cranes.
            - Suggestions for optimizing crane usage and ensuring safe operations.

            Your response should be clear, concise, and professional.
            """
            with st.spinner("Analyzing crane data..."):
                recommendation = query_llm(prompt)
            st.success("Recommendation generated!")

            # Display Recommendation
            st.subheader("Recommendation")
            st.write(recommendation)

            # Filter Data for Visualization
            filtered_cranes = cranes[
                (cranes["Max_Lift_Capacity"] >= load_weight)
                & (cranes["Tolerable_Wind_Speed"] >= wind_speed)
                & (cranes["Radius"] >= radius)
            ]

            if filtered_cranes.empty:
                st.warning("No cranes match the specified requirements.")
                return

            # Display Data Table
            st.subheader("Filtered Crane Data")
            st.dataframe(filtered_cranes)

            # Data Visualization
            st.subheader("Crane Comparison")
            numeric_columns = ["Max_Lift_Capacity", "Tolerable_Wind_Speed", "Radius", "Speed"]
            columns_to_plot = [col for col in numeric_columns if col in filtered_cranes.columns]

            fig = px.bar(
                filtered_cranes,
                x="Crane",
                y=columns_to_plot,
                barmode="group",
                title="Crane Specifications Comparison",
            )
            st.plotly_chart(fig)

            # Downloadable Report
            pdf = generate_pdf(filtered_cranes, recommendation)
            st.download_button(
                label="Download PDF Report",
                data=pdf.getvalue(),
                file_name="crane_comparison_report.pdf",
                mime="application/pdf",
            )

if __name__ == "__main__":
    main()
