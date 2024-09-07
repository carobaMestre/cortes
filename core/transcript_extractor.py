from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from core.logger import log_error, log_info

class TranscriptExtractor:
    
    @staticmethod
    def fetch_transcript(video_id, language='pt'):
        """Extrai a transcrição de um vídeo do YouTube."""
        try:
            log_info(f"Buscando transcrição para o vídeo {video_id} no idioma {language}...")
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
            formatter = JSONFormatter()
            formatted_transcript = formatter.format_transcript(transcript)
            log_info(f"Transcrição obtida com sucesso para o vídeo {video_id}.")
            return formatted_transcript
        except Exception as e:
            log_error(f"Erro ao obter a transcrição: {e}")
            return None
