#!/bin/bash
# Simple TTS wrapper using edge-tts
# Usage: ./tts.sh "text to speak" [voice]
# Default voice: ar-SA-ZariyahNeural (Arabic female)

TEXT="${1:-Hello, this is a test}"
VOICE="${2:-ar-SA-ZariyahNeural}"
RATE="${3:-+0%}"

# Generate audio to temp file
/tmp/pdf_venv/bin/edge-tts --voice "$VOICE" --rate "$RATE" --text "$TEXT" --write-media /tmp/tts_output.mp3 2>/dev/null

# Play with mpv
if command -v mpv &>/dev/null; then
    mpv --no-video --really-quiet /tmp/tts_output.mp3 2>/dev/null
elif command -v ffplay &>/dev/null; then
    ffplay -nodisp -autoexit -loglevel quiet /tmp/tts_output.mp3 2>/dev/null
else
    echo "No audio player found. Install mpv or ffplay."
    exit 1
fi

rm -f /tmp/tts_output.mp3
