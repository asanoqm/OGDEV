
from OCR_REQUEST import text_detection
from amazon_polly import voice_synthesize

if __name__ == '__main__':
    imagepath = "画像までのパス"
    reconized_text = text_detection(imagepath)
    voice_synthesize(reconized_text)
