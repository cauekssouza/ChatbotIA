import json
import os
from datetime import datetime

DATA_DIR = "data"
PROMPT_FILE = os.path.join(DATA_DIR, "prompts.json")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedbacks.json")
PROMPT_TXT = os.path.join(DATA_DIR, "prompt.txt")  # opcional, para reset padrão
DEFAULT_PROMPT = "Você é um assistente útil e objetivo."

# Garante que a pasta data existe
os.makedirs(DATA_DIR, exist_ok=True)

def load_prompt():
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
            if prompts:
                return prompts[-1]["prompt"]
            return DEFAULT_PROMPT
    except:
        return DEFAULT_PROMPT

def save_feedback(feedback: str, suggestion: str):
    entry = {
        "feedback": feedback,
        "suggestion": suggestion,
        "date": datetime.now().isoformat()
    }

    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_prompt(suggestion: str, feedback: str):
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
    except:
        prompts = []

    base_prompt = prompts[-1]["prompt"] if prompts else DEFAULT_PROMPT

    if feedback == "Ruim":
        new_prompt = (
            base_prompt
            + " Seja mais claro, objetivo e explique passo a passo. "
            + suggestion
        )
    elif feedback == "Regular":
        new_prompt = base_prompt + " Melhore a clareza da resposta. " + suggestion
    else:
        new_prompt = base_prompt + " " + suggestion

    prompts.append({
        "prompt": new_prompt.strip(),
        "date": datetime.now().isoformat()
    })

    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)

def load_feedbacks():
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def load_all_prompts():
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# -------- novas utilitárias (sem quebrar o que já existe) --------

def clear_feedbacks():
    """Apaga todos os feedbacks registrados."""
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)

def clear_prompts():
    """Apaga o histórico de prompts registrados."""
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)

def reset_prompt():
    """
    Restaura o prompt inicial padrão (DEFAULT_PROMPT) e grava como último estado em prompts.json.
    Mantém o histórico coerente: adiciona uma entrada com o prompt padrão.
    """
    # Zera histórico
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2, ensure_ascii=False)

    # Regrava uma entrada padrão
    prompts = [{"prompt": DEFAULT_PROMPT, "date": datetime.now().isoformat()}]
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)

    # Opcionalmente mantém um arquivo .txt (se você quiser ler por fora)
    try:
        with open(PROMPT_TXT, "w", encoding="utf-8") as f:
            f.write(DEFAULT_PROMPT)
    except:
        pass
