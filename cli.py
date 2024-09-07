import click
from core.transcript_extractor import TranscriptExtractor
from core.gpt_analyzer import GPTAnalyzer
from core.logger import log_info, log_error

@click.command()
@click.option('--video-id', prompt='ID do vídeo do YouTube', help='O ID do vídeo do YouTube para extração de transcrição.')
@click.option('--language', default='pt', help='O idioma da transcrição (padrão: pt).')
@click.option('--max-segments', default=5, help='Número máximo de segmentos/cortes sugeridos.')
def main(video_id, language, max_segments):
    """CLI para extração de transcrição e sugestão de cortes usando GPT."""
    
    log_info(f"Iniciando processo para o vídeo {video_id}...")
    
    # Passo 1: Extração de Transcrição
    transcript = TranscriptExtractor.fetch_transcript(video_id, language)
    if transcript:
        # Passo 2: Análise com GPT
        analysis = GPTAnalyzer.analyze_transcript(transcript, max_segments)
        
        if analysis:
            log_info("\nAnálise e sugestões de cortes:\n")
            print(analysis)
        else:
            log_error("Erro durante a análise.")
    else:
        log_error("Não foi possível obter a transcrição.")
        
if __name__ == '__main__':
    main()
