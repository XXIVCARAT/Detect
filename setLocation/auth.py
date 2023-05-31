
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from pathlib import Path


current_dir = Path.cwd()
relative_path = current_dir / 'setLocation\\test-700f4-firebase-adminsdk-rsmds-391dbc762c.json'

cred = credentials.Certificate(relative_path)

firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-700f4-default-rtdb.firebaseio.com/'})