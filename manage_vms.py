import argparse
import asyncio
import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser(description="Gerencia VMs (exemplo)")
    # Ação posiciona l (list, start, stop)
    parser.add_argument(
        "action",
        choices=["list", "start", "stop"],
        help="Ação a executar sobre as VMs",
    )
    # ID da VM (opcional para algumas ações)
    parser.add_argument("-i", "--vm_id", help="ID da VM (quando aplicável)")
    # Região
    parser.add_argument("-r", "--region", default="br-se1", help="Região/zone")
    return parser.parse_args()


async def list_instances_async(region: str):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError("CLOUD API key not found in API_KEY")

    url = f"https://api.magalu.cloud/{region}/compute/v1/instances"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json",
    }

    timeout = httpx.Timeout(10.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()


async def start_vm(region: str, vm_id: str):
    api_key = os.getenv("API_KEY")
    url = f"https://api.magalu.cloud/{region}/compute/v1/instances/{vm_id}/start"
    headers = {"x-api-key": api_key, "Accept": "application/json"}
    timeout = httpx.Timeout(10.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.post(url, headers=headers)
        return resp


async def stop_vm(region: str, vm_id: str):
    api_key = os.getenv("API_KEY")
    url = f"https://api.magalu.cloud/{region}/compute/v1/instances/{vm_id}/stop"
    headers = {"x-api-key": api_key, "Accept": "application/json"}
    timeout = httpx.Timeout(10.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.post(url, headers=headers)
        return resp


if __name__ == "__main__":
    args = parse_args()

    match args.action:
        case "list":
            vms = asyncio.run(list_instances_async(args.region))
            print("VMs ativas:")
            for vm in vms.get("instances", []):
                print(f" - {vm['name']} (ID: {vm['id']})")
        case "start":
            if not args.vm_id:
                print("Erro: --vm_id é obrigatório para iniciar uma VM.")
            else:
                vms = asyncio.run(start_vm(args.region, args.vm_id))
        case "stop":
            if not args.vm_id:
                print("Erro: --vm_id é obrigatório para desligar uma VM.")
            else:
                vms = asyncio.run(stop_vm(args.region, args.vm_id))
        case _:
            print(f"Ação '{args.action}' não implementada ainda.")
