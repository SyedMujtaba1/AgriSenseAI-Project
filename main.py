import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_ai_solution(problem):
    """
    Takes a farmer's problem and returns an AI-generated farming solution.
    Example: "My wheat leaves are yellow" -> AI suggests cause and treatment.
    """
    prompt = f"""
    You are an intelligent agriculture assistant named AgriSenseAI.
    A farmer describes this problem: "{problem}"
    
    Provide:
    - Likely cause
    - Step-by-step practical solution
    - Preventive measures for future
    Respond in clear and simple English suitable for farmers.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    print("🌾 Welcome to AgriSenseAI — Smart Assistant for Farmers (Gemini Powered) 🌦️")
    while True:
        problem = input("\nDescribe your farming problem (or type 'exit' to quit): ")
        if problem.lower() == 'exit':
            print("👋 Goodbye! May your crops be healthy and your yield abundant!")
            break
        print("\n🤖 Gemini AI Suggestion:\n")
        print(get_ai_solution(problem))
