# magalu_cloud

Projeto simples para gerenciar instâncias/VMs e snapshots na API Magalu Cloud.

Este repositório contém utilitários Python (`manage_vms.py` e `manage_snapshots.py`)
e exemplos de como consumir a API (ex.: listagem de instâncias/snapshots) usando
`httpx`. O objetivo deste README é explicar como instalar dependências, configurar
variáveis de ambiente e executar os scripts.

## Pré-requisitos

- Python 3.14+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Acesso à API Magalu Cloud e uma chave de API (x-api-key)

## Instalação

1. Clone o repositório (se ainda não o fez):

```bash
git clone <repo-url> # ou já estar no diretório local
cd magalu_cloud
```

2. Sincronize o ambiente virtual e instale as dependências:

```bash
uv sync
```

## Configuração

Use o arquivo `env.example` para configurar variáveis de ambiente.

1. Copie `env.example` para `.env` e edite os valores:

```bash
cp env.example .env
# editar .env com seu editor preferido (code .env, nano .env, etc.)
```

## Uso

### Gerenciamento de Instâncias (VMs)

O script `manage_vms.py` permite gerenciar instâncias/VMs. Exemplos:

- Listar instâncias:

```bash
uv run manage_vms.py list --region br-se1
```

- Iniciar Instância:

```bash
uv run manage_vms.py start --region br-se1 -i <ID_DA_INSTANCIA>
```

- Desligar Instância:

```bash
uv run manage_vms.py stop --region br-se1 -i <ID_DA_INSTANCIA>
```

### Gerenciamento de Snapshots

O script `manage_snapshots.py` permite criar, listar e gerenciar snapshots de instâncias.

- Listar todos os snapshots:

```bash
uv run manage_snapshots.py list --region br-se1
```

- Recuperar snapshot por ID:

```bash
uv run manage_snapshots.py get --region br-se1 --snapshot_id <ID_DO_SNAPSHOT>
```

- Criar snapshot. Cria o snapshot com nome no formato "<snapshot_name>-YYYY-MM-DD":

```bash
uv run manage_snapshots.py create --region br-se1 --snapshot_name <NOME> --instance_id <ID_DA_INSTANCIA>
```

- Recuperar snapshot por nome:

```bash
uv run manage_snapshots.py get_by_name --region br-se1 --snapshot_name <NOME_DO_SNAPSHOT>
```

- Deletar snapshot:

```bash
uv run manage_snapshots.py delete --region br-se1 --snapshot_name <NOME_DO_SNAPSHOT>
```

## Contribuição

Pull requests são bem-vindos. Para mudanças maiores (reorganização, integração com SDKs),
abra uma issue primeiro descrevendo a proposta.

## Licença

Este projeto é licenciado sob a Licença MIT — consulte o arquivo `LICENSE` para o texto completo.
