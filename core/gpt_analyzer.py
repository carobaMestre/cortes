import openai
from core.logger import log_error, log_info
from config.settings import settings

class GPTAnalyzer:
    
    @staticmethod
    def analyze_transcript(transcript, max_segments=5):
        """Envia a transcrição para análise do GPT e retorna sugestões de cortes."""
        prompt = f"""
        Você é um assistente especializado em edição de vídeos. Aqui está a transcrição de um vídeo. 
        Sugira cortes baseados nos momentos mais importantes:

        {transcript}

        Identifique no máximo {max_segments} cortes e descreva os tópicos mais importantes discutidos.
        """
        
        try:
            log_info("Enviando transcrição para análise do GPT...")
            openai.api_key = settings.GPT_API_KEY

            # Nova forma de fazer a requisição com openai>=1.0.0
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente especializado em edição de vídeo."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )

            analysis = response['choices'][0]['message']['content']
            log_info("Análise completada com sucesso.")
            return analysis

        except Exception as e:
            log_error(f"Erro durante a análise do GPT: {e}")
            return None


def chunk_text(transcript, chunk_size=3000):
    """Divide a transcrição em blocos menores de acordo com o limite de tokens."""
    for i in range(0, len(transcript), chunk_size):
        yield transcript[i:i + chunk_size]

def analyze_in_chunks(transcript, max_segments=5):
    """Analisa a transcrição em blocos menores."""
    all_analyses = []
    for chunk in chunk_text(transcript):
        analysis = GPTAnalyzer.analyze_transcript(chunk, max_segments)
        if analysis:
            all_analyses.append(analysis)
        else:
            log_error("Erro ao realizar análise com GPT.")
    
    return "\n".join(all_analyses)


def run_video_analysis(video_id, language='pt', max_segments=5):
    """Executa a análise completa de um vídeo do YouTube."""
    log_info(f"Iniciando análise para o vídeo {video_id}")
    
    # Extração de Transcrição
    transcript = TranscriptExtractor.fetch_transcript(video_id, language)
    if transcript:
        # Análise com GPT
        analysis = analyze_in_chunks(transcript, max_segments)
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
