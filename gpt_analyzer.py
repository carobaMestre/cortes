import openai
from core.transcript_extractor import TranscriptExtractor
from core.logger import log_info, log_error

# Certifique-se de definir a sua chave de API corretamente
openai.api_key = 'SUA-KEY'

class GPTAnalyzer:
    @staticmethod
    def analyze_transcript(transcript, max_segments=5):
        """Envia a transcrição para análise do GPT e retorna sugestões de cortes."""
        try:
            log_info("Enviando transcrição para análise do GPT...")
            response = openai.ChatCompletion.create(
                model="gpt-3.5",  
                messages=[
                    {"role": "system", "content": "Você é um assistente que sugere cortes em vídeos com base em transcrições."},
                    {"role": "user", "content": f"Analise a seguinte transcrição e sugira até {max_segments} cortes: {transcript}"}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            log_error(f"Erro durante a análise com GPT: {str(e)}")
            return None

def run_video_analysis(video_id, language='pt', max_segments=5):
    """Executa a análise completa de um vídeo do YouTube."""
    log_info(f"Iniciando análise para o vídeo {video_id}")
    
    # Extração de Transcrição
    transcript = TranscriptExtractor.fetch_transcript(video_id, language)
    if transcript:
        log_info(f"Transcrição obtida com sucesso para o vídeo {video_id}.")
        
        # Análise com GPT
        analysis = GPTAnalyzer.analyze_transcript(transcript, max_segments)
        if analysis:
            log_info("Análise e sugestões de cortes:")
            print(analysis)
        else:
            log_error("Erro ao realizar análise com GPT.")
    else:
        log_error("Erro ao extrair transcrição.")

if __name__ == '__main__':
    video_id = 'IktGbSbzHqY'  # Exemplo de ID de vídeo
    run_video_analysis(video_id)
