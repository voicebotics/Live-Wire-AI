from fastapi import FastAPI, WebSocket
import openai
import database
import ghl_api
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept() # Tells the server to accept the connection from the frontend
    while True:
        data = await websocket.receive_text() # data = Audio text
        

        client_info = ghl_api.fetch_client_data("client_id") # Will have to update with actual info
        
        ai_response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": f"Live conversation: {data}, Previous data: {client_info}"}
            ]
        )

        # ^^^ Will need to do some prompt engineering once the application is setup

        await websocket.send_text(ai_response["choices"][0]["message"]["content"]) # Sends the AI's response back to the frontend in real time.



### This code works for testing ###

# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Initialize the OpenAI client
# client = openai.OpenAI()

# # Open and transcribe the audio file
# with open(r"", "rb") as audio_file:
#     transcript = client.audio.transcriptions.create(
#         model="whisper-1",
#         file=audio_file,
#         response_format="text"
#     )

# # Print the transcript text
# print(transcript)