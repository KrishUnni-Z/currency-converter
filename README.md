
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
    git clone https://github.com/KrishUnni-Z/currency-converter.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
   cd currency-converter
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
├── api.py                # Contains functions to interact with the API.
├── requirements.txt      # List of required Python packages
└── README.txt            # Documentation for the project
```

### Description of Files

- `app.py`: Main file for running the Streamlit app. It includes user interface, API interaction, and output formatting.
- `frankfurter.py`: Contains functions to fetch the list of currencies and conversion rates from the Frankfurter API.
- `api.py`: Contains functions to interact with the API.
- `currency.py`: Helper functions to format output and handle currency conversion logic.
- `requirements.txt`: Lists all Python dependencies needed to run the app.
- `README.txt`: The file you are currently reading, which documents how to use the app.

### Functions Explained
- `round_rate(rate)`: Rounds the given conversion rate to four decimal places for clarity and consistency in display.
- `reverse_rate(rate)`: Calculates the inverse of a given conversion rate, rounded to four decimal places. This is useful for displaying how much of the base currency one unit of the target currency is worth.
- `format_output(date, from_currency, to_currency, rate, amount)`: Formats the conversion output into plain text and markdown. It returns a comprehensive string that includes the conversion date, amount, converted value, conversion rate, and inverse rate.


## Output Format
The output of the currency conversion is presented in two formats: plain text and markdown.

### Plain Text Output:
This format provides a summary of the conversion details in a straightforward manner. An example output would be:
```
The conversion rate on 2024-10-07 from AUD to BGN was 1.2132. So 0.00 in AUD equals 0.00 in BGN. The inverse rate is 0.8243.
```

### Markdown Output:
The markdown format presents the conversion results structured with bullet points for clarity. An example output would look like this:
```
 Conversion Result
- Conversion Date: 2024-10-07
- Amount Converted: 0.00 AUD corresponds to **0.00 BGN**
- From Currency: AUD
- To Currency: BGN
- Conversion Rate: 1.2132
- Inverse Rate: 0.8243
```

### Swap Feature

The swap feature allows users to quickly exchange the 'from' and 'to' currencies by clicking a button with an arrow symbol (↔️). This enhances user experience by making the conversion process more efficient, especially for users who frequently switch currencies.

### Date and Time Limitations

When fetching historical rates, users are required to select a valid past date. The application does not support future dates for historical rate queries, as the API only provides historical data. Make sure to select a date that is not in the future to ensure successful retrieval of the conversion rate.

## Citations

- **Frankfurter API**: [Frankfurter API Documentation](https://www.frankfurter.app/)
- **Streamlit Documentation**: [Streamlit](https://docs.streamlit.io/)
