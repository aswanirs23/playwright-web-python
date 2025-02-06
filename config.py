from dotenv import load_dotenv
import os

load_dotenv()

login_url = os.getenv("LOGIN_URL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
