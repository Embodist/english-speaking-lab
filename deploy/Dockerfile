FROM python:3.13-slim

ARG OPENPRONOUNCE_REF=main

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/models/huggingface \
    HOME=/models/home \
    REPO=/opt/OpenPronounce \
    ENVDIR=/usr/local \
    OPENPRONOUNCE_TTS=piper \
    OPENPRONOUNCE_TTS_VOICE=en_US-lessac-medium

RUN apt-get update && apt-get install -y --no-install-recommends \
      ffmpeg espeak-ng git curl ca-certificates rclone tini \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir "openpronounce[app]" "openpronounce[tts-piper]" openai-whisper vosk

RUN git clone https://github.com/Halleck45/OpenPronounce.git /opt/OpenPronounce \
 && git -C /opt/OpenPronounce checkout "$OPENPRONOUNCE_REF"

WORKDIR /app
COPY scripts /app/scripts
RUN mkdir -p /app/07_review-log/reports /app/11_attachments /models/home/.cache

COPY deploy/entrypoint.sh /usr/local/bin/lab-entrypoint.sh
RUN chmod +x /usr/local/bin/lab-entrypoint.sh

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=120s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/health || exit 1

ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/lab-entrypoint.sh"]
