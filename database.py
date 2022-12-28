import os 

import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta
from dotenv import load_dotenv # pip install python-dotenv


# Load the environment variables
load_dotenv(".env")
DETA_KEY = "c0a4eg0u_SYhbHGcJhhPgtwfnBYbZyuo5HE4pTbxD"
# DETA_KEY = os.getenv(DETA_KEY)
# DETA_KEY = st.secrets["DETA_KEY"]
# https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management


# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

