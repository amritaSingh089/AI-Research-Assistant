# AI Research Assistant

## About

This project is an AI Research Assistant built using **Python**, **Tavily Search API**, and **Google Gemini AI**.

It searches the internet for a given topic and provides:

* Top 5 Insights
* Short Summary
* Sources

## Technologies Used

* Python
* Tavily API
* Gemini API

## Files

* `app.py` – Main Python program
* `.env` – Stores API keys
* `README.md` – Project information

## Installation

Install the required libraries:

```bash
pip install tavily-python google-generativeai python-dotenv
```

## API Keys

Create a `.env` file and add:

```env
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

## Run the Project

```bash
python app.py
```

Enter a topic, for example:

```text
AI in agriculture
```

## Output

The program displays:

TOP 5 INSIGHTS
1.  The AI in Agriculture Market is projected for substantial growth, from USD $1.7 billion in 2023 to USD $4.7 billion by 2028, highlighting its increasing economic impact and adoption.
2.  AI fundamentally enhances efficiency and productivity in agriculture by automating repetitive tasks, optimizing resource use (water, fertilizer, pesticides), and providing data-driven insights for strategic decision-making and improved yields.
3.  Precision farming is a core application, where AI leverages sensor data, satellite imagery, and drones for real-time crop health monitoring, early detection of issues, optimized irrigation, and informed soil management.
4.  AI significantly contributes to sustainable agriculture by enabling predictive analytics for weather and crop stress, reducing loss, conserving resources, and supporting practices like nutrient management and reduced till farming.
5.  Successful AI integration requires addressing challenges such as data quality and accuracy, and necessitates strategic investments in infrastructure, governance, skills, and an inclusive, ethical approach, particularly to benefit smallholder farmers globally.

SHORT SUMMARY
AI is revolutionizing agriculture by offering farmers powerful, data-driven tools for increased efficiency and productivity. It drives precision farming through real-time monitoring, predictive analytics, and optimized resource allocation, leading to higher yields and reduced waste. Beyond operational improvements, AI fosters sustainable practices by conserving resources and mitigating environmental impact. While transforming the farmer's role into an innovator, successful AI adoption hinges on overcoming data quality challenges and ensuring inclusive implementation for global food security.

SOURCES
----------------------------------------------------------------------------------------------------
1. https://www.bpm.com/insights/ai-in-agriculture
2. https://www.ffa.org/technology/how-ai-can-impact-agriculture
3. https://www.basic.ai/blog-post/7-applications-of-ai-in-agriculture
4. https://www.stineseed.com/blog/harnessing-the-power-of-ai-and-machine-learning-in-agriculture
5. https://www.worldbank.org/en/topic/agriculture/publication/harnessing-artificial-intelligence-for-agricultural-transformation
----------------------------------------------------------------------------------------------------


**Name:** Amrita Singh
