import os
import time
import subprocess
import signal
import threading
from pyngrok import ngrok, conf
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Configuration
# -------------------------
FASTAPI_PORT = 8000
STREAMLIT_PORT = 8501

NGROK_TOKEN = os.getenv("NGROK_AUTHTOKEN")
if not NGROK_TOKEN:
    raise ValueError("NGROK_AUTHTOKEN not found in .env file")

# Set ngrok auth token
conf.get_default().auth_token = NGROK_TOKEN

# Kill previous ngrok tunnels
ngrok.kill()
print("✅ Previous ngrok tunnels terminated.")

# -------------------------
# Function to start FastAPI
# -------------------------
def start_fastapi():
    print("🚀 Starting FastAPI...")
    fastapi_proc = subprocess.Popen(
        ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", str(FASTAPI_PORT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )

    # Wait a few seconds for uvicorn to boot
    time.sleep(3)

    # Retry loop to expose ngrok
    max_retries = 10
    for i in range(max_retries):
        try:
            fastapi_url = ngrok.connect(FASTAPI_PORT, bind_tls=True)
            print(f"🌐 FastAPI public URL: {fastapi_url}")
            break
        except Exception as e:
            print(f"⚠️ Ngrok not ready for FastAPI, retrying ({i+1}/{max_retries})...")
            time.sleep(1)
    else:
        print("❌ Could not create ngrok tunnel for FastAPI.")

    return fastapi_proc

# -------------------------
# Function to start Streamlit
# -------------------------
def start_streamlit():
    print("🚀 Starting Streamlit...")
    streamlit_proc = subprocess.Popen(
        ["streamlit", "run", "app_streamlit.py", "--server.port", str(STREAMLIT_PORT)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )

    # Wait a few seconds for Streamlit to boot
    time.sleep(5)

    # Retry loop to expose ngrok
    max_retries = 10
    for i in range(max_retries):
        try:
            streamlit_url = ngrok.connect(STREAMLIT_PORT, bind_tls=True)
            print(f"🌐 Streamlit public URL: {streamlit_url}")
            break
        except Exception as e:
            print(f"⚠️ Ngrok not ready for Streamlit, retrying ({i+1}/{max_retries})...")
            time.sleep(1)
    else:
        print("❌ Could not create ngrok tunnel for Streamlit.")

    return streamlit_proc

# -------------------------
# Main
# -------------------------
if __name__ == "__main__":
    try:
        # Start both servers in parallel threads
        fastapi_thread = threading.Thread(target=start_fastapi)
        streamlit_thread = threading.Thread(target=start_streamlit)

        fastapi_thread.start()
        streamlit_thread.start()

        fastapi_thread.join()
        streamlit_thread.join()

        print("Press Ctrl+C to stop all servers and ngrok...")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping all servers and ngrok...")
        # Kill all processes
        ngrok.kill()
        os.system(f"fuser -k {FASTAPI_PORT}/tcp")
        os.system(f"fuser -k {STREAMLIT_PORT}/tcp")
        print("✅ Done.")
