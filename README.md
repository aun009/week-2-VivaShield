# 🛡️ VivaShield AI
### *Open-Source Capstone Viva Defense & Examiner Trap Predictor*

> Built for the **Hacktoberfest Open-Source AI Challenge: Week 2 (Side Hustle)**.  
> Powered by **Google Gemma 2** running locally via Ollama with $0.00 marginal inference costs.

---

## 💡 The Problem & The Side Hustle

Over **1.5 million engineering and computer science students** graduate every year across universities (SPPU, VTU, Anna Univ, IITs, etc.). Every single one must face an **external viva defense** of their final-year capstone project.

The terror is universal:
1. External examiners deliberately probe for **copied code**, **unjustified tech choices** (*"Why did you use MongoDB instead of Postgres for relational data?"*), and **concurrency bottlenecks**.
2. Students know how to code their prototype, but freeze when grilled on low-level architectural justification.
3. Students and tuition/Xerox shops already spend ₹500 to ₹2,000 for bound project reports and slide decks.

### 💰 The Business Model: ₹49 ($0.59) Impulse Micro-SaaS
* **Direct Student Pricing:** ₹49 per capstone defense dossier (5 Examiner Traps, 10 Deep-Dive Q&As, 5 What-If Scenarios, and a 1-Page Printable Hallway Cheatsheet).
* **The Pune Xerox Shop Model (B2B2C):** Cyber cafes and photocopy centers near engineering campuses print thousands of project binders every March/April. By integrating VivaShield, they bundle a laminated *"Official Viva Defense Sheet"* for a ₹99 add-on, generating an instant high-margin offline sales channel.

---

## ⚡ Why Open Innovation Matters

| Dimension | Closed Cloud APIs (e.g. GPT-4o) | Open-Weights (Google Gemma 2 via Ollama) |
| :--- | :--- | :--- |
| **Marginal Cost / Run** | **~₹18.50 ($0.22)** (30k context for student code/README) | **₹0.00** (Local inference or fixed $5 VPS) |
| **Gross Margin @ ₹49** | ~62% (Eaten up by API price shifts & rate limits) | **98.4% Net Margin** |
| **Student IP & Anti-Plagiarism** | ❌ Code sent to 3rd-party servers; risk of indexing by Turnitin/MOSS | **🔒 100% Private; code never leaves localhost** |
| **Offline Campus Use** | ❌ Fails without reliable high-speed campus WiFi | **✓ Runs completely offline on student laptops** |
| **Domain Fine-Tuning** | ❌ Black-box prompt engineering | **✓ Can fine-tune with LoRA for university-specific rubrics** |

---

## 🏗️ System Architecture

```
+-------------------------------------------------------------------------+
|                              STUDENT CLIENT                             |
|  [GitHub Repo URL]   OR   [Pasted Code/README]   OR   [1-Click Sample]  |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                           VIVASHIELD FASTAPI                            |
|                                                                         |
|  • /api/fetch-repo    -->  Pulls public README + File Tree (GitHub API) |
|  • /api/models        -->  Queries local Ollama tags (/api/tags)        |
|  • /api/analyze       -->  Builds Examiner Persona & Prompts Gemma      |
|  • /api/pricing-calc  -->  Live Micro-SaaS Margin Calculator            |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                  LOCAL OPEN-WEIGHT INFERENCE ENGINE                     |
|                                                                         |
|            Google Gemma 2 (2B / 9B) running on Ollama                   |
|            (Fallback: Qwen 2.5 / Hybrid Viva Defense Engine)            |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                       EXAMINER DEFENSE DOSSIER                          |
|  1. 🎯 5 Ruthless Examiner Trap Questions & Defenses                    |
|  2. ⚙️ 10 Deep-Dive Architecture Questions & Model Answers              |
|  3. 🧪 5 "What-If" Chaos & Edge-Case Stress Tests                       |
|  4. 📄 1-Page Printable Hallway Cheatsheet (Memorize in 5 Mins)         |
+-------------------------------------------------------------------------+
```

---

## 🚀 Quickstart

### Prerequisites
1. Python 3.10+
2. [Ollama](https://ollama.ai/) installed and running:
   ```bash
   ollama pull gemma2:2b
   ```

### 1-Click Launch
```bash
git clone https://github.com/your-username/vivashield-ai.git
cd vivashield-ai
chmod +x run.sh
./run.sh
```
Visit **`http://localhost:8000`** in your browser.

---

## 🐳 Docker & Cloud Deployment

### Run with Docker:
```bash
docker build -t vivashield-ai .
docker run -p 8000:8000 -e OLLAMA_HOST=http://host.docker.internal:11434 vivashield-ai
```

### Deploy to Render (Best Use of Render Category):
1. Connect this repo to [Render](https://render.com/).
2. Render will automatically detect `render.yaml` and configure the web service.

---

## 🏆 Hacktoberfest '26 Prize Categories Targeted

- **Overall Winner ($250):** Built for the "Side Hustle" prompt.
- **Featured Category — Best Use of Gemma ($200):** Built from the ground up around Google's open-weight Gemma 2 model.
- **Featured Category — Best Use of Render ($200):** Production-ready `Dockerfile` and `render.yaml` blueprint included.

---

## 📄 License
MIT License. Free and open source for students and developers worldwide.
