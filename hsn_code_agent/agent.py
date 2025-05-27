import os
import pandas as pd
from google.adk.agents import Agent

# Get the directory where this agent.py file lives
BASE_DIR = os.path.dirname(__file__)
# Construct full path to the Excel file inside data folder
DATA_FILE_PATH = os.path.join(BASE_DIR, "data", "hsn_codes.xlsx")

# Load HSN codes Excel file into a DataFrame
hsn_data = pd.read_excel(DATA_FILE_PATH)
print("Columns in Excel:", hsn_data.columns)

def validate_hsn_code(code: str) -> dict:
    """Validate the given HSN code against the dataset."""
    if code in hsn_data['\nHSNCode'].astype(str).values:

        description = hsn_data.loc[hsn_data['\nHSNCode'].astype(str) == code, 'Description'].values[0]
        return {
            "status": "success",
            "message": f"HSN code {code} is valid. Description: {description}"
        }
    else:
        return {
            "status": "error",
            "message": f"HSN code {code} is not valid."
        }

root_agent = Agent(
    name="hsn_code_validation_agent",
    model="gemini-2.0-flash",  # Replace with your actual model ID
    description="Agent to validate HSN codes and provide descriptions",
    instruction="You validate if the given HSN code is valid and return its description or an error message.",
    tools=[validate_hsn_code]
)
