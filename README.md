# magalu_cloud

Projeto simples para gerenciar instâncias/VMs na API Magalu Cloud.

Este repositório contém um utilitário Python (`manage_vms.py`) e exemplos de como
consumir a API (ex.: listagem de instâncias) usando `httpx`. O objetivo deste README
é explicar como instalar dependências, configurar variáveis de ambiente e executar o script.

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

O script principal é `manage_vms.py`. Os exemplos abaixo mostram como listar instâncias, ligar e desligar uma instância.

- Listar instâncias:

```bash
uv run manage_vms.py list --region br-se1
```

- Iniciar Instância (exemplo):

```bash
uv run manage_vms.py start --region br-se1 -i <ID_DA_INSTANCIA>
```

- Desligar Instância:

```bash
uv run manage_vms.py stop --region br-se1 -i <ID_DA_INSTANCIA>
```

## Contribuição

Pull requests são bem-vindos. Para mudanças maiores (reorganização, integração com SDKs),
abra uma issue primeiro descrevendo a proposta.

## Licença

Este projeto é licenciado sob a Licença MIT — consulte o arquivo `LICENSE` para o texto completo.
