# Data Insight Hub

Welcome to Data Insight Hub, your personal data analyst assistant! This project allows users to effortlessly connect, analyze, visualize, and present their data. With features such as CSV file upload, insightful data analysis, graph creation, and report generation, you can unlock the full potential of your data.

## Features

1. **Connect Your CSV File**: Easily upload your CSV file to start analyzing your data.
2. **Ask Any Data-Related Question**: Use natural language to query your dataset.
3. **Create Insightful Graphs and Charts**: Generate visualizations like graphs and pie charts.
4. **Summarize Datasets**: Get detailed summaries and insights from your data.
5. **Generate PowerPoint Presentations**: Create comprehensive presentations of your data analysis.

## Setup and Run

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- PandasAI
- Matplotlib
- OpenAI API Key
- dotenv

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-insight-hub.git
   cd data-insight-hub


2. Create and activate a virtual environment:
    ````bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

    ````
    pip install -r requirements.txt

4. Create a .env file in the root directory and add your OpenAI API key:

    ````
   OPENAI_API_KEY=your_openai_api_key

## Running the Application

1. Start the Streamlit app:
    ````
   streamlit run app.py

2. Open your web browser and navigate to the URL provided by Streamlit, typically http://localhost:8501.

## Usage
Login: Use the login credentials (username: admin, password: 123) to access the main application.

Upload CSV: Click on the sidebar to upload your CSV file.

Interact with Data: Use the chat input to ask questions or request visualizations. For example:

"Show a graph of sales trends over the past year."
"Summarize the dataset."


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.