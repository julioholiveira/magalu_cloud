# magalu_cloud

Projeto simples para gerenciar instâncias/VMs na API Magalu Cloud.

Este repositório contém um utilitário Python (`manage_vms.py`) e exemplos de como
consumir a API (ex.: listagem de instâncias) usando `httpx`. O objetivo deste README
é explicar como instalar dependências, configurar variáveis de ambiente e executar o script.

## Pré-requisitos

- Python 3.13+
- pip
- Acesso à API Magalu Cloud e uma chave de API (x-api-key)

## Instalação

1. Clone o repositório (se ainda não o fez):

```bash
git clone <repo-url> # ou já estar no diretório local
cd magalu_cloud
```

2. (Opcional) Crie um ambiente virtual e ative-o:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale dependências:

```bash
pip install -r requirements.txt
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
python manage_vms.py list --region br-se1
```

- Iniciar Instância (exemplo):

```bash
python manage_vms.py start --region br-se1 -i <ID_DA_INSTANCIA>
```

- Desligar Instância:

```bash
python manage_vms.py stop --region br-se1 -i <ID_DA_INSTANCIA>
```

## Contribuição

Pull requests são bem-vindos. Para mudanças maiores (reorganização, integração com SDKs),
abra uma issue primeiro descrevendo a proposta.

## Licença

Este projeto é licenciado sob a Licença MIT — consulte o arquivo `LICENSE` para o texto completo.
