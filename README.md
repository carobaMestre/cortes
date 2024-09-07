
```markdown
# Video Transcript Analyzer

Este projeto fornece uma ferramenta para análise automática de transcrições de vídeos do YouTube, utilizando os modelos de IA GPT (OpenAI) e Gemini (Google). O objetivo é sugerir cortes em vídeos com base no conteúdo das transcrições, facilitando a edição de vídeos com foco em trechos importantes.

## Funcionalidades

- **Extração de Transcrição**: Obtém a transcrição de vídeos do YouTube com base no ID do vídeo.
- **Análise de Transcrição**: Envia a transcrição para análise utilizando os modelos GPT ou Gemini.
- **Sugestão de Cortes**: Gera até 5 sugestões de cortes baseadas no conteúdo da transcrição.

## Pré-requisitos

- Python 3.7 ou superior
- Conta e chave de API do OpenAI e do Google Gemini

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/carobaMestre/cortes.git
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure suas chaves de API:

   - **GPT (OpenAI)**: Defina a variável `openai.api_key` no código com sua chave.
   - **Google Gemini**: Configure a variável de ambiente `API_KEY` com a chave da API Gemini.

## Uso

### Analisando transcrições com GPT

1. No arquivo `gpt_analyzer.py`, execute o seguinte código:

   ```bash
   python gpt_analyzer.py
   ```

2. Exemplo de execução:

   ```bash
   python gpt_analyzer.py --video_id "ID_DO_VIDEO_YOUTUBE"
   ```

3. O sistema extrairá a transcrição do vídeo e enviará para análise do GPT, retornando sugestões de cortes.

### Analisando transcrições com Google Gemini

1. No arquivo `gemini_analyzer.py`, execute o seguinte código:

   ```bash
   python gemini_analyzer.py
   ```

2. Exemplo de execução:

   ```bash
   python gemini_analyzer.py --video_id "ID_DO_VIDEO_YOUTUBE"
   ```

3. O sistema extrairá a transcrição do vídeo e enviará para análise do Google Gemini, retornando sugestões de cortes.

## Estrutura do Projeto

```plaintext
.
├── core/
│   ├── transcript_extractor.py  # Módulo responsável pela extração de transcrições de vídeos do YouTube
│   ├── logger.py                # Módulo de logging para registrar atividades e erros
├── gpt_analyzer.py               # Analisador utilizando GPT
├── gemini_analyzer.py            # Analisador utilizando Google Gemini
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests para melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```

Esse `README.md` detalha o uso dos dois códigos (GPT e Google Gemini) para sugerir cortes em vídeos do YouTube, além de fornecer instruções claras sobre como configurar e executar o projeto.