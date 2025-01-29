from TTS.api import TTS 
tts = TTS("tts_model/multilingual/multi-dataset/xtts_v2", gpu=False)

tts.tts_to_file(text="",
                file_path="output,wav"
                speaker_wav=["ref1.wav"]
                language="en"
                split_sentences=True
                )