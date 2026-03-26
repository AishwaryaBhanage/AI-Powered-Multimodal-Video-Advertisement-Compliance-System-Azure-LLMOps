# 🚀 AI-Powered Multimodal Compliance System (Azure Data Foundry)

## 📌 Overview
An end-to-end AI-powered system that analyzes multimodal content (video, audio, text) and generates structured compliance reports using Azure-native services.

Designed with a production-first mindset, this system leverages LLMs, Retrieval-Augmented Generation (RAG), and workflow orchestration to automate policy validation at scale.

---

## 🎯 Key Features
- 🎥 Multimodal Processing (Video, Audio, Text)
- 🧠 LLM-based Compliance Reasoning (Azure OpenAI - GPT-4o)
- 🔍 RAG Pipeline using Azure AI Search
- 🧾 Structured JSON Compliance Reports
- ⚙️ Agentic Workflows using LangGraph
- 📊 Observability with Azure Application Insights
- ⚡ Scalable ETL using Azure Data Foundry

---

## 🏗️ Architecture


User Input (Video/Audio/Text)
↓
Azure Video Indexer / OCR / Speech-to-Text
↓
Azure Data Foundry (ETL Pipelines)
↓
Embedding + Indexing (Azure AI Search)
↓
LLM Reasoning (Azure OpenAI - GPT-4o)
↓
LangGraph (Agent Orchestration)
↓
Structured Output (JSON)
↓
Monitoring (Azure Application Insights)


---

## 🧰 Tech Stack

### AI / ML
- Azure OpenAI (GPT-4o)
- Embeddings + RAG
- LangGraph (multi-agent workflows)

### Azure Services
- Azure Data Foundry (data pipelines)
- Azure AI Search (vector database)
- Azure Video Indexer (multimodal extraction)
- Azure Blob Storage / ADLS
- Azure Application Insights (monitoring)

### Backend
- Python
- FastAPI
- REST APIs

---

## ⚙️ How It Works

### 1. Input Processing
- Upload video/audio/text
- Extract transcripts, OCR, and metadata

### 2. Data Pipeline (Azure Data Foundry)
- Clean and transform extracted data
- Store structured data for downstream tasks

### 3. Retrieval (RAG)
- Retrieve relevant policy documents using vector search
- Provide contextual grounding for LLM

### 4. LLM Analysis
- Combine input data + retrieved policies
- Generate compliance decisions with reasoning

### 5. Output
- Structured JSON report including:
  - Violations
  - Risk scores
  - Explanations

---

## 📊 Example Output

```json
{
  "ad_id": "12345",
  "compliance_status": "Non-Compliant",
  "violations": [
    {
      "rule": "Misleading Claims",
      "confidence": 0.92,
      "explanation": "The ad exaggerates product performance..."
    }
  ],
  "risk_score": 0.87
}
📈 Impact
⏱️ Reduced manual compliance review effort by ~22%
⚡ Automated large-scale policy validation workflows
📉 Improved consistency, traceability, and auditability
🚀 Future Improvements
Real-time streaming compliance checks
Fine-tuned domain-specific LLMs
Human-in-the-loop feedback system
Multi-agent evaluation and guardrails
Compliance analytics dashboard
🤝 Use Cases
Ad compliance (Meta Ads, Google Ads)
Regulatory monitoring (finance, healthcare)
Content moderation systems
Brand safety and policy enforcement
💡 Why This Matters

This project demonstrates how AI-native systems + cloud data pipelines can transform compliance workflows from manual processes into scalable, automated decision systems.

📬 Contact

Aishwarya Bhanage
📧 aish.bhanage0412@gmail.com

🔗 https://linkedin.com/in/aishwaryabhanage

💻 https://github.com/AishwaryaBhanage
