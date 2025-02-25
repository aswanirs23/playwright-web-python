"""
Configuration Settings
This module manages environment-specific configuration for the test suite.
It loads environment variables from .env file using python-dotenv.

"""

from dotenv import load_dotenv
import os

load_dotenv()

login_url = os.getenv("LOGIN_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")