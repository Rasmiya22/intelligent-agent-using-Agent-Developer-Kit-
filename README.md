
# 🧠 HSN Code Validation Agent using Google's Agent Developer Kit (ADK)

This repository contains a conversational agent built using the **Google Agent Developer Kit (ADK)** to validate **HSN (Harmonized System of Nomenclature) codes** from an Excel dataset. It checks whether the provided code is valid and returns the corresponding description.

## 🚀 Features

- ✅ Validates HSN codes against a dataset (Excel file)
- 📄 Provides relevant description for valid codes
- ❌ Returns error message for invalid codes
- 🧠 Built using ADK 


## 🗂️ Project Structure

```
intelligent-agent-using-Agent-Developer-Kit-/
│
├── hsn_code_agent/
│   ├── __init__.py                # Required for Python module
│   ├── agent.py                   # Main agent code (intent logic and validation)
│   ├── .env                       # Environment variables (API key, etc.)
│   └── data/
│       └── hsn_codes.xlsx         # Excel dataset of HSN codes and descriptions
│
├── .gitignore                     # Ignores env/cache/pyc

└── README.md                      # You're here!
```

## 🧪 How It Works

1. **Excel File** (`hsn_codes.xlsx`) contains HSN codes and their descriptions.
2. **ADK Agent** loads this Excel and validates codes through a tool function.
3. If code is valid, it responds with the description; else an error.

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rasmiya22/intelligent-agent-using-Agent-Developer-Kit-.git
   cd intelligent-agent-using-Agent-Developer-Kit-
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (create a `.env` file)
   ```env
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   ```

5. **Run the agent locally**
   ```bash
   adk web
   ```

6. **Test in Browser**
   Open `http://localhost:8000` and try:
   > Validate HSN code 1234



## 📄 Sample Excel

```
| HSNCode | Description                     |
|---------|----------------------------------|
| 1234    | Sample Description 1             |
| 5678    | Sample Description 2             |
```

> Make sure the Excel has clean headers with no extra spaces or newline characters.

## 🔐 .env Sample

```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## 🧾 requirements.txt Sample

```txt
pandas
google-generativeai
adk
python-dotenv
openpyxl
```

## 🙏 Acknowledgement

This project is part of the assignment submission for Google's ADK agent framework using Gemini. Built by Rasmiya.

---


