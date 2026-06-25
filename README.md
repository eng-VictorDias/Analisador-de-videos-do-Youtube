# 🎬 AI YouTube Summarizer (Resumo Automático de Vídeos)

Um pipeline em Python que automatiza a extração, transcrição e sumarização de vídeos do YouTube utilizando Inteligência Artificial. 

Este projeto foi desenvolvido para otimizar o consumo de conteúdo em vídeos, transformando horas de áudio em resumos estruturados e diretos ao ponto, demonstrando habilidades em integração de APIs, manipulação de arquivos e engenharia de prompts.

## 🚀 Como o Código Funciona (Passo a Passo)

A arquitetura do script foi dividida em funções modulares para facilitar a manutenção e leitura:

1. **`baixar_audio()` (Extração de Dados):**
   - Utiliza a biblioteca `yt-dlp` para acessar o link fornecido pelo usuário e fazer o download apenas da faixa de áudio (ignorando o vídeo para economizar banda e processamento).
   - O áudio é convertido automaticamente para o formato `.mp3` usando FFmpeg.

2. **`transcrever_audio()` (Transformação em Texto):**
   - Implementa o **OpenAI Whisper** (modelo `base`), uma rede neural de reconhecimento de fala robusta.
   - O modelo processa o arquivo `.mp3` localmente e extrai todo o texto falado no vídeo com alta precisão.

3. **`gerar_resumo()` (Processamento de Linguagem Natural):**
   - Comunica-se com a API da OpenAI utilizando o modelo **GPT-4o-mini**.
   - Foi aplicada uma técnica de *System Prompting* ("Você é um assistente especialista...") para garantir que a saída da IA venha sempre formatada em *bullet points*, destacando apenas os insights mais relevantes da transcrição.

4. **Pipeline Principal e Limpeza (Try/Finally):**
   - O script executa as funções sequencialmente e imprime o resultado final no terminal.
   - O bloco `finally` garante as boas práticas de manipulação de arquivos: independentemente de o código rodar com sucesso ou dar erro, o arquivo `.mp3` temporário é apagado do disco ao final do processo (`os.remove`), evitando lixo de memória.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **yt-dlp:** Extração de mídia do YouTube.
* **OpenAI Whisper:** Transcrição de áudio para texto.
* **OpenAI API (GPT-4o-mini):** Geração de resumos inteligentes.

## ⚙️ Como rodar o projeto na sua máquina

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/nome-do-repositorio.git](https://github.com/SEU-USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio# 🎬 AI YouTube Summarizer (Resumo Automático de Vídeos)

Um pipeline em Python que automatiza a extração, transcrição e sumarização de vídeos do YouTube utilizando Inteligência Artificial. 

Este projeto foi desenvolvido para otimizar o consumo de conteúdo em vídeo, transformando horas de áudio em resumos estruturados e diretos ao ponto, demonstrando habilidades em integração de APIs, manipulação de arquivos e engenharia de prompts.

