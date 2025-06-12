import asyncio
import os
from pathlib import Path
from datetime import datetime
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
openai = AsyncOpenAI()  

async def main() -> None:
    try:
        async with openai.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="alloy",
                input="Bonjour! Ceci est un exemple de synthèse vocale avec l'API OpenAI TTS.",
                response_format="mp3",
        ) as response:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            audio = Path(__file__).parent / f"generated_{timestamp}.mp3"
            await response.stream_to_file(audio)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
