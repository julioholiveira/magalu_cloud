import os

import httpx
from dotenv import load_dotenv

load_dotenv()


class MagaluVMSnapshot:
    def __init__(self, region: str):
        self.region = region
        self.url = f"https://api.magalu.cloud/{region}/compute/v1"
        self.api_key = os.getenv("API_KEY")

    def set_headers(self):
        if not self.api_key:
            raise ValueError("API_KEY environment variable is not set")
        self.headers = {
            "x-api-key": self.api_key,
            "Accept": "application/json",
        }
        return self.headers

    def get_snapshot(self, id: str):
        response = httpx.get(f"{self.url}/snapshots/{id}", headers=self.set_headers())
        if response.status_code != 200:
            return {"status": response.status_code, "message": response.text}
        return response.json()

    def get_snapshot_by_name(self, name: str):
            snapshots = self.list_snapshots()
            for snapshot in snapshots.get("snapshots", []):
                if snapshot.get("name") == name:
                    return snapshot
            return None

    def list_snapshots(self):
        response = httpx.get(f"{self.url}/snapshots", headers=self.set_headers())
        if response.status_code != 200:
            return {"status": response.status_code, "message": response.text}
        return response.json()

    def create_snapshot(self, snapshot_data: dict):
        response = httpx.post(
            f"{self.url}/snapshots", headers=self.set_headers(), json=snapshot_data
        )
        result = {"status": response.status_code, "message": response.json()}
        return result

    def delete_snapshot(self, id):
        response = httpx.delete(
            f"{self.url}/snapshots/{id}", headers=self.set_headers()
        )
        result = {"status": response.status_code}
        return result
