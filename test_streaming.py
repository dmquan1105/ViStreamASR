import sys
sys.path.insert(0, 'src')
from streaming import StreamingASR # type: ignore

# Initialize and use
asr = StreamingASR()

# Process audio file
for result in asr.stream_from_microphone(duration_seconds=10):
    if result['partial']:
        print(f"Partial: {result['text']}")
    if result['final']:
        print(f"Final: {result['text']}")