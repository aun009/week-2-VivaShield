#!/usr/bin/env bash
set -e

echo "=========================================================="
echo "🛡️  VivaShield AI — Launching Capstone Defense Engine"
echo "=========================================================="

# Check Python virtualenv
if [ -d ".venv" ]; then
    echo "✓ Found .venv, activating..."
    source .venv/bin/activate
else
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi

# Check Ollama status
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✓ Local Ollama service detected on port 11434"
else
    echo "⚠️ Warning: Ollama not responding on http://localhost:11434."
    echo "   VivaShield will run in Hybrid/Mock fallback mode."
fi

echo "Starting VivaShield web server at http://localhost:8000"
exec uvicorn app:app --host 0.0.0.0 --port 8000 --reload
