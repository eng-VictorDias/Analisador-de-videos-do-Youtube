import os
import yt_dlp
import whisper
from openai import OpenAI

# 1. Configuração da API do ChatGPT via Variável de Ambiente (Boas Práticas de Segurança)

cliente_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def baixar_audio(url, nome_arquivo="audio_temp"):
    """Faz o download do áudio do vídeo do YouTube na melhor qualidade."""
    print("1/3 - Baixando áudio do YouTube...")
    opcoes = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        'outtmpl': nome_arquivo,
        'quiet': True # Mantém o terminal limpo
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])
    return f"{nome_arquivo}.mp3"

def transcrever_audio(caminho_audio):
    """Utiliza o modelo Whisper da OpenAI para converter o áudio em texto."""
    print("2/3 - Transcrevendo o áudio...")
    modelo = whisper.load_model("base") 
    resultado = modelo.transcribe(caminho_audio)
    return resultado["text"]

def gerar_resumo(texto):
    """Envia a transcrição para o GPT-4o-mini gerar um resumo estruturado."""
    print("3/3 - Gerando resumo com Inteligência Artificial...")
    resposta = cliente_openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente especialista em resumir vídeos do YouTube. Extraia os pontos principais em tópicos (bullet points)."},
            {"role": "user", "content": f"Resuma o seguinte conteúdo:\n\n{texto}"}
        ]
    )
    return resposta.choices[0].message.content

# --- Execução Principal do Script (Pipeline) ---
if __name__ == "__main__":
    url_video = input("Cole a URL do vídeo do YouTube: ")
    arquivo_mp3 = ""

    try:
        arquivo_mp3 = baixar_audio(url_video)
        texto_completo = transcrever_audio(arquivo_mp3)
        resumo_final = gerar_resumo(texto_completo)
        
        print("\n" + "="*40)
        print("RESUMO DO VÍDEO")
        print("="*40 + "\n")
        print(resumo_final)
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a execução: {e}")
        
    finally:
        # Limpeza do arquivo temporário para não ocupar espaço no disco
        if arquivo_mp3 and os.path.exists(arquivo_mp3):
            os.remove(arquivo_mp3)