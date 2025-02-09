# Crane Comparison & Decision Support Tool

🚀 Dynamic Hackathon

Innovating Safety Solutions for the Material Handling Industry.

Empowering innovators to revolutionize safety and efficiency in crane operations and material handling.

📌 Problem Statement: PS 8 - Web-Based Crane Comparison and Decision Support Platform

Develop a web-based platform for comparing cranes based on operational parameters such as:

- Maximum lift capacity
- Radius
- Wind tolerance
- Speed

The system should analyze load distribution and provide recommendations for safe lifting operations, ensuring optimal equipment usage.

🔗 Live Demo

Try out the application here: Crane Comparison & Decision Support Tool

📖 Introduction

The Crane Comparison & Decision Support Tool is a cutting-edge web-based platform designed to help users compare cranes based on various operational parameters. It provides detailed recommendations for safe lifting operations, ensuring optimal equipment usage and enhancing safety and efficiency.

✨ Features

✅ Upload Crane Dataset: Easily upload your crane dataset in CSV format.  
✅ Input Crane Requirements: Enter specific requirements such as load weight, wind speed, and radius.  
✅ Get Detailed Recommendations: Receive expert recommendations for the best cranes based on your input.  
✅ View Filtered Crane Data: See the filtered crane data that meets your requirements.  
✅ Visual Comparisons: Compare crane specifications through interactive graphs.  
✅ Download PDF Report: Generate and download a comprehensive PDF report with crane data and recommendations.

⚙️ Installation

Follow these steps to set up the project locally:

```sh
# Clone the repository
git clone https://github.com/yourusername/DynamicHackathon-CraneComparisonTool.git
cd DynamicHackathon-CraneComparisonTool

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
🎯 Usage

Upload Crane Dataset: Upload your crane dataset in CSV format using the sidebar.
Input Requirements: Enter load weight, wind speed, and radius in the sidebar.
Get Recommendations: Click "Get Recommendations" to receive crane suggestions.
View Results: See the filtered crane data and recommendations on the main page.
Download Report: Download the PDF report with detailed crane data and recommendations.
📂 Sample Data

A sample crane dataset is provided in the data/ directory. You can use this dataset to test the application.

📊 Output Result

Crane Comparison Report
{'Crane': 'Crane C', 'Max_Lift_Capacity': 100, 'Tolerable_Wind_Speed': 30, 'Radius': 30, 'Speed ': 3}
{'Crane': 'Crane E', 'Max_Lift_Capacity': 200, 'Tolerable_Wind_Speed': 25, 'Radius': 40, 'Speed ': 5}
🤝 Contributing

Contributions are welcome! Feel free to open issues and submit pull requests to improve this project.

📩 For inquiries, reach out via GitHub issues.


This format should be clear and engaging for anyone visiting your GitHub repository. Let me know if you need any further adjustments!
