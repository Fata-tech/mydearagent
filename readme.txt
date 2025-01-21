# AI Market Research Agent

An AI-powered market research assistant built with Streamlit and OpenAI's GPT model. This tool helps analyze industry trends, generate market insights, and create SWOT analyses for companies.

## Features

- Generate market insights using AI
- Perform SWOT analysis for companies
- Upload and analyze market data
- Interactive data visualization
- Multiple analysis depth options (summary, in-depth, prediction)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/market-research-agent.git
cd market-research-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.streamlit/secrets.toml` file with your OpenAI API key:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter your market research query in the text input field
2. Select the desired analysis type from the sidebar
3. Optionally upload market data in CSV format
4. Click "Generate Insights" to get AI-powered analysis

## Project Structure

```
market-research-agent/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── .streamlit/           
│   └── secrets.toml      # API keys and secrets
└── README.md             # Project documentation
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
