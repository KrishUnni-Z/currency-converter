import requests

def get_url(url: str):
    """
    Function that will call a provided GET API endpoint URL and return its status code and response content.
    
    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called
    
    Returns
    -------
    tuple
        A tuple of (status_code, response_text), where response_text is the content or error message as a string
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an error for 4xx/5xx status codes
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, f"Error: {str(e)}"
