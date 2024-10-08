
# Currency Converter Application

## Author
- **Name**: Krishnan Unni Prasad
- **Student ID**: 25225362

## Description
This is a simple currency converter application that allows users to convert amounts between different currencies using live exchange rates from the Frankfurter API. Users can also retrieve historical exchange rates and swap between currencies with a click of a button.

### Challenges Faced:
- Handling currency swapping logic efficiently.
- Properly formatting the output of conversion rates.
- Managing the user interface in Streamlit for optimal user experience.

### Future Features:
- Add support for real-time rate monitoring and notifications.
- Improve UI design with additional currency graphs and trends.
- Add more detailed error messages and handling.

## How to Setup

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd <project-directory>
    ```

3. **Install Required Packages**:
    Use the `requirements.txt` file to install all necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. **Required Python Version**: 
    - Python 3.8 or higher

5. **Packages and Versions**:
    - `streamlit` >= 1.21.0
    - `requests` >= 2.28.0
    - `python` == 3.10

## How to Run the Program

1. **Start the Application**:
    Run the following command to launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. **Access the Application**:
    Open your web browser and go to:
    ```
    http://localhost:8501
    ```
    This will load the app where you can input currency values, select currencies, and view conversion results.

## Project Structure

```bash
.
├── app.py                # Main application script
├── frankfurter.py        # Handles fetching currency data from the Frankfurter API
├── currency.py           # Contains utility functions for formatting outputs
├── requirements.txt      # List of required Python packages
└── README.txt            # Documentation for the project
```

### Description of Files

- `app.py`: Main file for running the Streamlit app. It includes user interface, API interaction, and output formatting.
- `frankfurter.py`: Contains functions to fetch the list of currencies and conversion rates from the Frankfurter API.
- `currency.py`: Helper functions to format output and handle currency conversion logic.
- `requirements.txt`: Lists all Python dependencies needed to run the app.
- `README.txt`: The file you are currently reading, which documents how to use the app.

## Citations

- **Frankfurter API**: [Frankfurter API Documentation](https://www.frankfurter.app/)
- **Streamlit Documentation**: [Streamlit](https://docs.streamlit.io/)
