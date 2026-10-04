import argparse
from datetime import datetime

from services.snapshots import MagaluVMSnapshot


def list_all_snapshots(region: str):
    snapshot_manager = MagaluVMSnapshot(region)
    return snapshot_manager.list_snapshots()


def retrieve_snapshot(region: str, snapshot_id: str):
    snapshot_manager = MagaluVMSnapshot(region)
    return snapshot_manager.get_snapshot(snapshot_id)


def create_snapshot(region: str, snapshot_name: str, instance_id: str):
    current_date = datetime.now().date()
    snapshot_name = f"{snapshot_name}-{current_date}"
    snapshot_manager = MagaluVMSnapshot(region)
    if not instance_id:
        raise ValueError("instance_id is required to create a snapshot")
    return snapshot_manager.create_snapshot(
        {"name": snapshot_name, "instance": {"id": instance_id}}
    )


def delete_snapshot(region: str, name: str):
    snapshot_manager = MagaluVMSnapshot(region)
    snapshot = snapshot_manager.get_snapshot_by_name(name)
    if not snapshot:
        raise ValueError(f"Snapshot with name '{name}' not found")
    snapshot_id = snapshot.get("id")
    return snapshot_manager.delete_snapshot(snapshot_id)


def get_snapshot_by_name(region: str, snapshot_name: str):
    snapshot_manager = MagaluVMSnapshot(region)
    return snapshot_manager.get_snapshot_by_name(snapshot_name)


def parse_args():
    parser = argparse.ArgumentParser(description="Gerencia VMs (exemplo)")
    # Ação posicional (list, start, stop)
    parser.add_argument(
        "action",
        choices=["list", "get", "create", "delete", "get_by_name"],
        help="Ação a executar sobre as VMs",
    )
    # ID da instância (opcional para criação, será necessário se for criar um snapshot)
    parser.add_argument(
        "-i",
        "--instance_id",
        help="ID da instância (necessário para criar um snapshot)",
    )
    # ID da VM (opcional para algumas ações)
    parser.add_argument("-s", "--snapshot_id", help="ID do snapshot (quando aplicável)")
    # Região
    parser.add_argument("-r", "--region", default="br-se1", help="Região/zone")
    # Nome do snapshot (opcional para criação, será gerado automaticamente se não fornecido)
    parser.add_argument(
        "-n", "--snapshot_name", help="Nome do snapshot (opcional para criação)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    match args.action:
        case "list":
            snapshots = list_all_snapshots(args.region)
            print("Snapshots disponíveis:")
            for snapshot in snapshots.get("snapshots", []):
                print(
                    f"snapshot_name: {snapshot.get('name')}, "
                    f"snapshot_id: {snapshot.get('id')}, "
                    f"created_at: {snapshot.get('created_at')},"
                    f"instance_id: {snapshot.get('instance', {}).get('id')}"
                )
        case "get":
            if not args.snapshot_id:
                print("Erro: --snapshot_id é obrigatório para recuperar um snapshot.")
            else:
                snapshot = retrieve_snapshot(args.region, args.snapshot_id)
                print(snapshot)
        case "create":
            if not args.snapshot_name:
                print("Erro: --snapshot_name é obrigatório para criar um snapshot.")
            if not args.instance_id:
                print("Erro: --instance_id é obrigatório para criar um snapshot.")
            else:
                snapshot_name = args.snapshot_name
                instance_id = args.instance_id
                snapshot_result = create_snapshot(
                    args.region, snapshot_name, instance_id
                )
                print(snapshot_result)
        case "delete":
            if not args.snapshot_name:
                print("Erro: --snapshot_name é obrigatório para deletar um snapshot.")
            else:
                snapshot_result = delete_snapshot(args.region, args.snapshot_name)
                print(snapshot_result)
        case "get_by_name":
            if not args.snapshot_name:
                print(
                    "Erro: --snapshot_name é obrigatório para recuperar um snapshot pelo nome."
                )
            else:
                snapshot = get_snapshot_by_name(args.region, args.snapshot_name)
                print(snapshot)
        case _:
            print(f"Ação '{args.action}' não implementada ainda.")
