
---

# AI Agent Web App

This is a simple AI Agent web application that allows users to input queries and receive intelligent responses using the Llama3-8B language model via the LangChain framework and Groq API. The front end is built using Streamlit for easy interaction.

## Features

* Conversational AI powered by the Llama3-8B model.
* Streamlit-based user interface for real-time interaction.
* Simple and modular code structure for easy extension.
* Uses LangChain's zero-shot agent with Groq integration.

## Technologies Used

* Python
* LangChain
* Streamlit
* Groq API (Llama3-8B model)
* Tool integrations: Search and Calculator

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent-webapp.git
cd ai-agent-webapp
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

**If you don't have a `requirements.txt`, use:**

```bash
pip install langchain langchain-community streamlit openai
```

### 4. Set Environment Variables

Create a `.env` file or set these variables in your terminal:

```bash
export GROQ_API_KEY=your_groq_api_key
```

On Windows (CMD):

```cmd
set GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

## File Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies (optional)
└── README.md           # Project documentation
```
#Output:
<img width="1617" height="608" alt="image" src="https://github.com/user-attachments/assets/a1ae891d-f0d3-4905-a238-bbf8b21fe5bc" />


## Notes

* You may encounter rate limits when using the free Groq API. Consider upgrading to a higher tier for more usage.
* Make sure the `langchain-community` package is installed, as recent LangChain versions rely on it for community integrations.

## License

This project is for educational and experimental purposes. Feel free to modify and use it as needed.

---

