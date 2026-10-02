import argparse

from services.snapshots import MagaluVMSnapshot


def list_all_snapshots(region: str):
    snapshot_manager = MagaluVMSnapshot(region)
    return snapshot_manager.list_snapshots()


def retrieve_snapshot(region: str, snapshot_id: str):
    snapshot_manager = MagaluVMSnapshot(region)
    return snapshot_manager.get_snapshot(snapshot_id)


def parse_args():
    parser = argparse.ArgumentParser(description="Gerencia VMs (exemplo)")
    # Ação posicional (list, start, stop)
    parser.add_argument(
        "action",
        choices=["list", "get", "start", "stop"],
        help="Ação a executar sobre as VMs",
    )
    # ID da VM (opcional para algumas ações)
    parser.add_argument("-s", "--snapshot_id", help="ID do snapshot (quando aplicável)")
    # Região
    parser.add_argument("-r", "--region", default="br-se1", help="Região/zone")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    match args.action:
        case "list":
            snapshots = list_all_snapshots(args.region)
            print("Snapshots disponíveis:")
            for snapshot in snapshots.get("snapshots", []):
                print(
                    f"snapshot_name: {snapshot.get('name')}, snapshot_id: {snapshot.get('id')}"
                )
        case "get":
            if not args.snapshot_id:
                print("Erro: --snapshot_id é obrigatório para recuperar um snapshot.")
            else:
                snapshot = retrieve_snapshot(args.region, args.snapshot_id)
                print(snapshot)
        # case "start":
        #     if not args.vm_id:
        #         print("Erro: --vm_id é obrigatório para iniciar uma VM.")
        #     else:
        #         vms = asyncio.run(start_vm(args.region, args.vm_id))
        # case "stop":
        #     if not args.vm_id:
        #         print("Erro: --vm_id é obrigatório para desligar uma VM.")
        #     else:
        #         vms = asyncio.run(stop_vm(args.region, args.vm_id))
        case _:
            print(f"Ação '{args.action}' não implementada ainda.")
