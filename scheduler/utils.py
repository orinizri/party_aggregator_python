from typing import Tuple
from datetime import datetime
import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load environment variables fro    m the .env file
load_dotenv()

# Get environment variables
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
SCOPES = os.getenv("API_SCOPES").split(",")
DRIVER_PARTY_ROOT_FOLDER_ID = os.getenv("DRIVER_PARTY_ROOT_FOLDER_ID")

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)


def get_latest_party_folder(cache: dict) -> Tuple[str, str, dict]:
    """
    Returns the ID and metadata of the most recently created party folder.

    Parameters:
        cache (dict): Loaded JSON cache with 'createdTime' per folder.

    Returns:
        Tuple[str, str, dict]: (root_folder_id, latest_party_folder_id, folder_data)
    """
    latest_time = None
    latest_folder_id = None

    for _, files in cache.items():
        
        for folder_id, properties in files.items():
            createdTime = properties['createdTime']
            folder_name = properties['folder_name']
            if createdTime:
                created_dt = datetime.fromisoformat(createdTime.replace("Z", "+00:00"))
                if latest_time is None or created_dt > latest_time:
                    latest_time = created_dt
                    latest_party_name = folder_name
                    latest_folder_id = folder_id

    if latest_time:
        return latest_folder_id, latest_party_name
    else:
        raise ValueError("No folder with created_time found in cache.")


def generate_cache_from_drive(root_folder_id: str, credentials) -> dict:
    drive = build("drive", "v3", credentials=credentials)

    cache = {root_folder_id: {}}
    folders = drive.files().list(q=f"'{root_folder_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
                                 fields="files(id, name, createdTime)").execute().get("files", [])
    for folder in folders:
        folder_id = folder["id"]
        files = drive.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                   fields="files(id, name)").execute().get("files", [])

        cache[root_folder_id][folder_id] = {
            "folder_name": folder["name"],
            "createdTime": folder["createdTime"],
            "files": files
        }

    return cache

print(get_latest_party_folder(generate_cache_from_drive(DRIVER_PARTY_ROOT_FOLDER_ID, credentials)))