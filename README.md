# Projeto Diamond P

Este projeto é uma ferramenta para leitura e análise de arquivos CSV, com foco na detecção automática de codificação para garantir que os dados sejam carregados corretamente.

---

## Funcionalidades

- **Detecção automática de codificação**: Usa a biblioteca `chardet` para identificar a codificação do arquivo CSV.
- **Leitura de arquivos CSV**: Carrega o arquivo CSV em um DataFrame do Pandas para análise.
- **Fallback para UTF-8**: Se a codificação detectada falhar, tenta ler o arquivo com UTF-8.
- **Verificação de existência do arquivo**: Antes de tentar ler o arquivo, verifica se ele existe no caminho especificado.

---

## Como Usar

### Pré-requisitos

- Python 3.x instalado.
- Bibliotecas necessárias: `pandas` e `chardet`.

### Instalação das Dependências

Para instalar as bibliotecas necessárias, execute o seguinte comando:

```bash
pip install pandas chardet
