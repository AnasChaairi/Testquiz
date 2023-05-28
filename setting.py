import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_CONFIG = os.path.join(ROOT_DIR, 'logging.yml')

OUT_DIR = os.path.join(ROOT_DIR, 'output/')
RECORDING_DIR = os.path.join(OUT_DIR, 'recording')
TEXT_DIR = os.path.join(OUT_DIR, 'transcribed')
WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
TEXT_OUTPUT_FILE = os.path.join(TEXT_DIR, "text.txt")

Auth_DIR = os.path.join(ROOT_DIR, 'client_secrets.json')
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
#Api
OPENAI_API_KEY= "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"
Google_API_KEY ="AIzaSyBkfIa12KckrxJJhor6iMi0FY9-C8UlJOQ"    
# Audio configurations
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  # Max input channels
DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
DURATION = 10   # 10 seconds
CHUNK_SIZE = 1024