import openai, os, time, logging
from dotenv import load_dotenv


# ────────────────────  CONFIG  ────────────────────
AUDIO_PATH = r""
CLIENT_ID  = "sample_client_id"
DUMMY_CLIENT_INFO = {"note": "fake client data only for test"}

# ────────────────────  ENV  ────────────────────
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

# ────────────────────  1. TRANSCRIBE  ────────────────────
with open(AUDIO_PATH, "rb") as audio_file:
    t0 = time.time()
    whisper_result = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"        # plain text response
    )
    latency_ms = round((time.time() - t0) * 1000, 2)

transcript_text = whisper_result
print("\n🎙️  TRANSCRIPT --------------------------------")
print(transcript_text)
print(f"⏱️  Whisper latency: {latency_ms} ms")

# ────────────────────  2. GPT‑4o‑mini REPLY  ─────────────
gpt = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an AI assistant. Reply to the user."},
        {
            "role": "user",
            "content": f"Live conversation: {transcript_text}\nPrevious data: {DUMMY_CLIENT_INFO}",
        },
    ],
)

ai_reply = gpt.choices[0].message.content

print("\n🤖  GPT‑4o‑mini REPLY --------------------------")
print(ai_reply)
print("------------------------------------------------")
