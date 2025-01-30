from TTS.api import TTS 

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

tts.tts_to_file(
    text="What are we going to do tonight? Can there be a way for the fortnite team to get this together",
    file_path="output/output.wav",  # Fixed the filename typo
    speaker_wav=["ref1.wav"],
    language="en",
    split_sentences=True
)