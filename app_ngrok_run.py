import os
import time
import subprocess
import threading
from pyngrok import ngrok, conf
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Config
# -------------------------
FASTAPI_PORT = 8000
STREAMLIT_PORT = 8501
NGROK_TOKEN = os.getenv("NGROK_AUTHTOKEN")

if not NGROK_TOKEN:
    raise ValueError("NGROK_AUTHTOKEN missing in .env file")

# Set ngrok auth token
conf.get_default().auth_token = NGROK_TOKEN

# Kill any existing tunnels
ngrok.kill()
print("✅ Previous ngrok tunnels terminated.")

# -------------------------
# Helper to create ngrok tunnel with retry
# -------------------------
def create_ngrok_tunnel(port, max_retries=10, wait=2):
    for attempt in range(max_retries):
        try:
            url = ngrok.connect(port, bind_tls=True)
            print(f"🌐 ngrok tunnel for port {port}: {url}")
            return url
        except Exception as e:
            print(f"⚠️ Ngrok not ready for port {port}, retry {attempt+1}/{max_retries}...")
            time.sleep(wait)
    raise RuntimeError(f"❌ Could not create ngrok tunnel for port {port} after {max_retries} retries")

# -------------------------
# Start FastAPI
# -------------------------
def start_fastapi():
    print("🚀 Starting FastAPI...")
    subprocess.Popen(
        ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", str(FASTAPI_PORT)],
        stdout=None,
        stderr=None,
        preexec_fn=os.setsid
    )
    time.sleep(3)
    return create_ngrok_tunnel(FASTAPI_PORT)

# -------------------------
# Start Streamlit
# -------------------------
def start_streamlit():
    print("🚀 Starting Streamlit...")
    subprocess.Popen(
        ["streamlit", "run", "app_streamlit.py", "--server.port", str(STREAMLIT_PORT)],
        stdout=None,
        stderr=None,
        preexec_fn=os.setsid
    )
    time.sleep(5)
    return create_ngrok_tunnel(STREAMLIT_PORT)

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    try:
        # Start FastAPI first
        fastapi_thread = threading.Thread(target=start_fastapi)
        fastapi_thread.start()
        fastapi_thread.join()  # ensure FastAPI is up before Streamlit tunnel

        # Start Streamlit after FastAPI ngrok ready
        streamlit_thread = threading.Thread(target=start_streamlit)
        streamlit_thread.start()
        streamlit_thread.join()

        print("Press Ctrl+C to stop servers and ngrok.")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping servers and ngrok...")
        ngrok.kill()
        os.system(f"fuser -k {FASTAPI_PORT}/tcp")
        os.system(f"fuser -k {STREAMLIT_PORT}/tcp")
        print("✅ Done.")
