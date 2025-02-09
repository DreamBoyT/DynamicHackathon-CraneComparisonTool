# Crane Comparison & Decision Support Tool

## Dynamic Hackathon
**Innovating Safety Solutions for the Material Handling Industry.**

Empowering Innovators to Revolutionize Safety and Efficiency in Crane Operations and Material Handling Industry.

### Problem Statement: PS 8 - Web-Based Crane Comparison and Decision Support Platform
Design a web-based platform for comparing cranes based on operational parameters such as maximum lift capacity, radius, wind tolerance, and speed. The system should also analyze load distribution and provide recommendations for safe lifting operations, ensuring optimal equipment usage.

## Table of Contents
- Introduction
- Features
- Installation
- Usage
- Sample Data
- Output Result
- Contributing
- Live Demo

## Introduction
The **Crane Comparison & Decision Support Tool** is a cutting-edge web-based platform designed to help users compare cranes based on various operational parameters. It provides detailed recommendations for safe lifting operations, ensuring optimal equipment usage and enhancing safety and efficiency in crane operations.

## Features
- **Upload Crane Dataset**: Easily upload your crane dataset in CSV format.
- **Input Crane Requirements**: Enter specific requirements such as load weight, wind speed, and radius.
- **Get Detailed Recommendations**: Receive expert recommendations for the best cranes based on your input.
- **View Filtered Crane Data**: See the filtered crane data that meets your requirements.
- **Visual Comparisons**: Compare crane specifications through interactive graphs.
- **Download PDF Report**: Generate and download a comprehensive PDF report with crane data and recommendations.

## Installation
Follow these steps to set up the project locally.

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/DynamicHackathon-CraneComparisonTool.git
    cd DynamicHackathon-CraneComparisonTool
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```sh
    streamlit run app.py
    ```

## Usage
1. **Upload Crane Dataset:**
    - Upload your crane dataset in CSV format using the sidebar.

2. **Input Requirements:**
    - Enter the load weight, wind speed, and radius in the sidebar.

3. **Get Recommendations:**
    - Click the "Get Recommendations" button to receive crane recommendations.

4. **View Results:**
    - View the filtered crane data and recommendations on the main page.

5. **Download Report:**
    - Download the PDF report with detailed crane data and recommendations.

## Sample Data
A sample crane dataset is provided in the `data/` directory. You can use this dataset to test the application.

## Output Result
### Crane Comparison Report
```plaintext
{'Crane': 'Crane C', 'Max_Lift_Capacity': 100, 'Tolerable_Wind_Speed': 30, 'Radius': 30, 'Speed ': 3}
{'Crane': 'Crane E', 'Max_Lift_Capacity': 200, 'Tolerable_Wind_Speed': 25, 'Radius': 40, 'Speed ': 5}
