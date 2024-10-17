import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def extract_data(endpoint:str)-> list:
    """ used for extracting Data from the business API.

    `args:`
        endpoint: the API endpoint to extract data from.
    `returns:`
        list: a list of dictionaries containing product details.
    """

    try:
        print(f"`{endpoint}` Extraction in progress....")
        raw_data = requests.get(BASE_URL + endpoint).json()
        
    except Exception as e:
        print(f"ERROR: Occured during `{endpoint}` extraction-> ",e)
        raise e
    print(f"`{endpoint}` Extraction Successful. -> Got `{len(raw_data)}` {endpoint}")
    return raw_data




def transform_data(raw_data: list, endpoint: str) -> pd.DataFrame:
    """ used for transforming raw data into a pandas DataFrame.

    `args:`
        raw_data: list of dictionaries containing product details.
        endpoint: the API endpoint for which the data was extracted.
    `returns:`
        pd.DataFrame: a pandas DataFrame containing the transformed data.

    """

    try:
        print(f"`{endpoint}` Transformation in progress....")
        df = pd.DataFrame(raw_data)
        print(f"`{endpoint}` Transformation Successful. -> Got `{len(df)}` {endpoint}")

        # engineer needs to add a timestamp column to the dataframe
        # <demo add>

        return df
    except Exception as e:
        print(f"ERROR: Occured during `{endpoint}` transformation-> ", e)
        raise e


if __name__ == "__main__":
    print(extract_data("products"))