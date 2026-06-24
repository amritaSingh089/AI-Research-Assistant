from tavily import TavilyClient
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

tavily = TavilyClient(api_key=tavily_api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

topic = input("Enter research topic: ")

print("\nSearching the internet...\n")

search_results = tavily.search(
    query=topic,
    search_depth="advanced",
    max_results=5
)

research = ""
sources = []

for result in search_results["results"]:
    research += result["content"] + "\n\n"
    sources.append(result["url"])

prompt = f"""
You are an AI Research Assistant.

Based on the research below:

{research}

Generate the output in the following format:

TOP 5 INSIGHTS
1.
2.
3.
4.
5.

SHORT SUMMARY
Write a summary in 4-5 lines.

Do not include sources in the summary.
"""

response = model.generate_content(prompt)

print("-" * 100)
print("AI RESEARCH ASSISTANT")
print("-" * 100)

print(response.text)

print("\nSOURCES")
print("-" * 100)

for i, url in enumerate(sources, start=1):
    print(f"{i}. {url}")

print("-" * 100)