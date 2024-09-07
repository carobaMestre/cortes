import google.generativeai as genai
import os
from core.transcript_extractor import TranscriptExtractor
from core.logger import log_info, log_error

# Certifique-se de que a variável de ambiente "API_KEY" esteja configurada com a chave da API Gemini
genai.configure(api_key="SUA-KEY")

class GeminiAnalyzer:
    @staticmethod
    def analyze_transcript(transcript, max_segments=5):
        """Envia a transcrição para análise do Google Gemini e retorna sugestões de cortes."""
        try:
            log_info("Enviando transcrição para análise com Google Gemini...")

            # Utilize o modelo adequado para análise de texto (gemini-1.5-flash neste caso)
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Crie a solicitação com base na transcrição fornecida
            prompt = f"Analise a seguinte transcrição e sugira até {max_segments} cortes: {transcript}"
            response = model.generate_content(prompt)

            # Retorne o texto gerado pelo modelo
            return response.text

        except Exception as e:
            log_error(f"Erro durante a análise com Google Gemini: {str(e)}")
            return None

def run_video_analysis(video_id, language='pt', max_segments=5):
    """Executa a análise completa de um vídeo do YouTube usando Google Gemini."""
    log_info(f"Iniciando análise para o vídeo {video_id}")
    
    # Extração de Transcrição
    transcript = TranscriptExtractor.fetch_transcript(video_id, language)
    if transcript:
        log_info(f"Transcrição obtida com sucesso para o vídeo {video_id}.")
        
        # Análise com Google Gemini
        analysis = GeminiAnalyzer.analyze_transcript(transcript, max_segments)
        if analysis:
            log_info("Análise e sugestões de cortes:")
            print(analysis)
        else:
            log_error("Erro ao realizar análise com Google Gemini.")
    else:
        log_error("Erro ao extrair transcrição.")

if __name__ == '__main__':
    video_id = 'IktGbSbzHqY'  # Exemplo de ID de vídeo
    run_video_analysis(video_id)
