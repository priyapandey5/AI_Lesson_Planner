
import os
from dotenv import load_dotenv
import time
import json
import google.generativeai as genai
import statistics
from tqdm import tqdm

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")  # better model

def generate_lesson_plan(lesson_details):
    system_message = """
    You are an AI assistant that generates lesson plans. Create a detailed lesson plan based on the provided information.
    Output should be in JSON format with the following structure:
    {
        "Learning outcomes": {
            "knowledge": "",
            "skills": "",
            "understanding": ""
        },
        "Learning experiences": {
            "Prepare": "",
            "Plan": "",
            "Investigate": "",
            "Apply": "",
            "Connect": "",
            "Evaluate": ""
        },
        "Assessment": "",
        "Reflection": ""
    }
    """

    user_message = f"Generate a lesson plan for: {json.dumps(lesson_details)}"

    start_time = time.time()

    prompt = system_message + "\n\n" + user_message

    try:
        response = model.generate_content(prompt)
        end_time = time.time()

        return {
            "response": response.text,
            "time": end_time - start_time,
            "tokens": 0  # Gemini doesn't provide token count
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "response": "",
            "time": 0,
            "tokens": 0
        }


def evaluate_quality(lesson_plan):
    try:
        # Clean Gemini output (important)
        lesson_plan = lesson_plan.strip().replace("```json", "").replace("```", "")
        plan = json.loads(lesson_plan)

        score = 0
        score += len(plan.get("Learning outcomes", {}).get("knowledge", "").split()) / 10
        score += len(plan.get("Learning outcomes", {}).get("skills", "").split()) / 10
        score += len(plan.get("Learning outcomes", {}).get("understanding", "").split()) / 10
        score += sum(len(v.split()) for v in plan.get("Learning experiences", {}).values()) / 50
        score += len(plan.get("Assessment", "").split()) / 20
        score += len(plan.get("Reflection", "").split()) / 20

        return min(score, 10)

    except:
        return 0


def run_performance_test(num_tests=5):  # keep small for free usage
    lesson_details = [
        {"title": "Introduction to Photosynthesis", "subject": "Biology", "grade": 9, "duration": 2},
        {"title": "World War II Overview", "subject": "History", "grade": 11, "duration": 3},
        {"title": "Basic Algebraic Equations", "subject": "Math", "grade": 8, "duration": 1},
        {"title": "Shakespeare's Macbeth", "subject": "Literature", "grade": 10, "duration": 4},
        {"title": "States of Matter", "subject": "Chemistry", "grade": 7, "duration": 2}
    ]

    results = []

    for _ in tqdm(range(num_tests)):
        for details in lesson_details:
            result = generate_lesson_plan(details)
            result['quality'] = evaluate_quality(result['response'])
            results.append(result)

    # Analysis
    avg_time = statistics.mean(r['time'] for r in results if r['time'] > 0)
    avg_quality = statistics.mean(r['quality'] for r in results)

    print(f"Average response time: {avg_time:.2f} seconds")
    print(f"Average quality score: {avg_quality:.2f} / 10")

    with open('performance_results.json', 'w') as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    run_performance_test()