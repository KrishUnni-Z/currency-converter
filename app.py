import streamlit as st
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import format_output
from datetime import datetime

# Set the title of the Streamlit app
st.title("Currency Converter")

# Fetch the list of available currencies
currencies = get_currencies_list()
if currencies is None:
    st.error("Unable to fetch currency list. Please try again later.")
else:
    # Initialize session state for currencies if not done
    if 'from_currency' not in st.session_state:
        st.session_state.from_currency = currencies[0]
    if 'to_currency' not in st.session_state:
        st.session_state.to_currency = currencies[1]

    # Latest Conversion Section
    st.header("Latest Currency Conversion")
    with st.expander("Convert Currency", expanded=True):
        amount = st.number_input("Enter the amount to convert:", min_value=0.0, format="%.2f")

        # Swap currencies button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("↔️ Swap Currencies"):
                # Swap logic
                original_from_currency = st.session_state.from_currency
                st.session_state.from_currency = st.session_state.to_currency
                st.session_state.to_currency = original_from_currency

        # Currency selection boxes
        from_currency = st.selectbox("From Currency:", currencies, key="from_currency")
        to_currency = st.selectbox("To Currency:", currencies, key="to_currency")
        # Button to convert currency
    if st.button("Convert Currency"):
        # Get latest conversion rate
        date, rate = get_latest_rates(st.session_state.from_currency, st.session_state.to_currency, amount)

        if date is None or rate is None:
            st.error("Unable to fetch conversion rate. Please try again later.")
        else:
            plain_text_output, markdown_output = format_output(date, st.session_state.from_currency, st.session_state.to_currency, rate, amount)
            st.text_area("Conversion Summary", value=plain_text_output, height=50) 
            st.markdown(markdown_output)

    # Historical Conversion Section
    st.header("Historical Conversion Rate")
    with st.expander("Get Historical Rate", expanded=False):
        from_date = st.date_input("Select a past date:", max_value=datetime.today().date())
        if st.button("Get Historical Conversion Rate"):
            historical_rate = get_historical_rate(st.session_state.from_currency, st.session_state.to_currency, from_date, amount)
            if historical_rate is None:
                st.error("Unable to fetch historical rate. Please try again later.")
            else:
                plain_text_output, markdown_output = format_output(from_date, st.session_state.from_currency, st.session_state.to_currency, historical_rate, amount)
                st.text_area("Conversion Summary", value=plain_text_output, height=50) 
                st.markdown(markdown_output)  

# Footer section
st.markdown("---")
st.markdown("### About this app")
st.markdown("This app utilizes the Frankfurter API to fetch currency conversion rates. "
            "You can convert amounts and view historical rates.")
