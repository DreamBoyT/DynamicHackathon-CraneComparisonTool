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
Recommendation
Based on the specified criteria for lifting 100 tons under wind speeds of 20 m/s at a radius of 30 meters, the following analysis of the available cranes leads to the recommendation of Crane C and Crane E.

Crane Analysis:
Crane A
Max Lift Capacity: 50 tons (Insufficient for 100 tons)
Tolerable Wind Speed: 25 m/s
Radius: 20 m
Speed: 5 m/s
Recommendation: Not suitable due to insufficient lift capacity.
Crane B
Max Lift Capacity: 75 tons (Insufficient for 100 tons)
Tolerable Wind Speed: 20 m/s
Radius: 25 m
Speed: 4 m/s
Recommendation: Not suitable due to insufficient lift capacity.
Crane C
Max Lift Capacity: 100 tons (Meets requirement)
Tolerable Wind Speed: 30 m/s (Safe under specified conditions)
Radius: 30 m (Meets requirement)
Speed: 3 m/s
Recommendation: Suitable for the task.
Crane D
Max Lift Capacity: 150 tons (Exceeds requirement)
Tolerable Wind Speed: 15 m/s (Not safe under specified conditions)
Radius: 35 m
Speed: 6 m/s
Recommendation: Not suitable due to low tolerable wind speed.
Crane E
Max Lift Capacity: 200 tons (Exceeds requirement)
Tolerable Wind Speed: 25 m/s (Safe under specified conditions)
Radius: 40 m (Exceeds requirement)
Speed: 5 m/s
Recommendation: Suitable for the task.
Recommendations:
Recommended Cranes: Crane C and Crane E

Features Supporting the Recommendation:
Crane C:
Capacity: Exactly meets the requirement for lifting 100 tons.
Wind Tolerance: Can safely operate in wind speeds up to 30 m/s.
Radius: Perfectly matches the required radius of 30 m.
Safety: With a balanced design and operational limits, this crane can operate efficiently under the specified conditions.
Crane E:
Capacity: Significantly exceeds the lifting requirement, providing a safety margin.
Wind Tolerance: Safe operation up to 25 m/s, ensuring stability in windy conditions.
Radius: Can easily handle the required 30 m radius with room for greater reach if needed.
Potential Risks/Limitations:
Crane C: While it meets the capacity and operational criteria, its speed of 3 m/s is lower than Crane E, which may affect efficiency in time-sensitive operations.
Crane E: Although it provides a higher capacity, the operational cost may be higher due to maintenance and fuel consumption. It also has a larger radius than necessary, which could lead to challenges in confined spaces.
Suggestions for Optimizing Crane Usage and Ensuring Safe Operations:
Pre-Operational Safety Checks: Conduct thorough inspections of the cranes before use, focusing on the lifting mechanism, stability, and wind speed monitoring systems.
Weather Monitoring: Continuously monitor weather conditions to ensure that wind speeds do not exceed tolerable limits during operations.
Load Management: Ensure that the load is evenly distributed and secured properly to maintain stability during the lift.
Training and Compliance: Ensure that all operators are trained in crane operations and familiar with safety regulations. Compliance with local regulations is crucial.
Communication Protocols: Establish clear communication protocols among the team involved in the lifting operation to ensure coordinated efforts.
In conclusion, Crane C and Crane E are the best choices for the task based on their specifications and operational capabilities. Their selection balances safety, efficiency, and compliance with operational standards.

Filtered Crane Report
!Filtered Crane Data

Graph Plot
!Crane Specifications Comparison

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

Live Demo
You can test the application live at the following link: Crane Comparison & Decision Support Tool


### Repository Structure
DynamicHackathon-CraneComparisonTool/ ├── .streamlit/ │ └── secrets.toml ├── .gitignore ├── README.md ├── app.py ├── requirements.txt ├── setup.sh └── data/ └── sample_crane_data.csv


### Instructions for GitHub Repository

1. **Create a new repository on GitHub** with the name `DynamicHackathon-CraneComparisonTool`.

2. **Clone the repository** to your local machine:
    ```sh
    git clone https://github.com/yourusername/DynamicHackathon-CraneComparisonTool.git
    cd DynamicHackathon-CraneComparisonTool
    ```

3. **Add the files** to the repository:
    ```sh
    git add .
    git commit -m "Initial commit with project structure and files"
    git push origin main
    ```

4. **Update the README.md** with your GitHub username and any additional information specific to your project.

This setup ensures that the hackathon judges can easily understand and test your application. Let me know if you need any further assistance!
