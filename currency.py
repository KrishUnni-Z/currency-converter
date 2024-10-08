def round_rate(rate):
    """
    Function to round a rate to 4 decimal places.
    
    Parameters
    ----------
    rate : float
        The rate to round.
    
    Returns
    -------
    float
        The rounded rate.
    """
    return round(rate, 4)

def reverse_rate(rate):
    """
    Function that calculates the inverse of a conversion rate, rounded to 4 decimal places.

    Parameters
    ----------
    rate : float
        The conversion rate to invert.

    Returns
    -------
    float
        The inverse of the conversion rate, or 0 if the rate is 0.
    """
    return round(1 / rate, 4) if rate != 0 else 0

def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function to format the output for display in the app.

    Parameters
    ----------
    date : str
        The date of the conversion.
    from_currency : str
        The base currency.
    to_currency : str
        The target currency.
    rate : float
        The conversion rate.
    amount : float
        The amount in the base currency.

    Returns
    -------
    str
        The formatted output string with both plain text and markdown.
    """
    converted_amount = round_rate(rate * amount)
    inverse_rate = reverse_rate(rate)

    # Plain text version of the output
    plain_text_output = (
        f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate:.4f}. "
        f"So {amount:.2f} in {from_currency} equals {converted_amount:.2f} in {to_currency}. "
        f"The inverse rate is {inverse_rate:.4f}."
    )

    # Markdown version of the output
    markdown_output = f"""
    ### Conversion Result
    - **Conversion Date:** {date}
    - **Amount Converted:** {amount:.2f} {from_currency} corresponds to **{converted_amount:.2f} {to_currency}**
    - **From Currency:** {from_currency}
    - **To Currency:** {to_currency}
    - **Conversion Rate:** {rate:.4f}
    - **Inverse Rate:** {inverse_rate:.4f}
    """

    # Combine both plain text and markdown
    return plain_text_output, markdown_output