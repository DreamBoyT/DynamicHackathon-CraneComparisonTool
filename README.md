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
- Contributing
- License
- Live Demo

## Introduction
The **Crane Comparison & Decision Support Tool** is a web-based platform designed to help users compare cranes based on various operational parameters. It provides recommendations for safe lifting operations, ensuring optimal equipment usage.

## Features
- Upload crane dataset in CSV format.
- Input crane requirements (load weight, wind speed, radius).
- Get detailed recommendations for the best cranes.
- View filtered crane data and visual comparisons.
- Download a PDF report with crane data and recommendations.

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

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Live Demo
You can test the application live at the following link:
Crane Comparison & Decision Support Tool
