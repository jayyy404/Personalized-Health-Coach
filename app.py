from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # type: ignore

app = Flask(__name__)

def parse_advice(response_text):
    sections = {
        'diet': ['Diet Advice:', 'Diet Plan:', 'Nutritional Recommendations:'],
        'workout': ['Workout Plan:', 'Exercise Plan:', 'Training Program:'],
        'supplements': ['Supplement Recommendations:', 'Supplement Plan:', 'Supplementation:']
    }
    
    result = {
        'diet': [],
        'workout': [],
        'supplements': []
    }
    
    current_section = None
    lines = response_text.split('\n')
    
    for line in lines:
        line = line.strip()
        found_section = False
        for section, headers in sections.items():
            if any(line.startswith(header) for header in headers):
                current_section = section
                found_section = True
                break
        
        if found_section:
            continue
            
        if current_section and line:
            result[current_section].append(line)
    
    return {k: '\n'.join(v) if v else "No recommendations provided for this section." for k,v in result.items()}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = request.form.get("age")
        weight = request.form.get("weight")
        height = request.form.get("height")
        goal = request.form.get("goal")

        model = genai.GenerativeModel("gemini-1.5-flash")  # type: ignore
        prompt = f"""
                You are a certified lifestyle coach specializing in personalized wellness plans.

                I am a {age}-year-old individual, {height} cm tall, weighing {weight} kg. My primary goal is to {goal}.

                Based on this information, create a comprehensive and personalized lifestyle plan divided into the following sections, each with clear headers:

                Provide a personalized lifestyle coaching plan with CLEAR SECTION HEADERS in this exact format:

                Diet Advice:
                - Provide specific dietary recommendations tailored to my goal.
                - List foods to include and avoid.
                - Suggest meal timing and portion sizes.
                - Use bullet points for clarity.

                Workout Plan:
                - Outline a weekly exercise regimen suitable for my fitness level and goal.
                - Include types of exercises, duration, frequency, and intensity.
                - Mention any necessary equipment or alternatives.
                - Present the plan in bullet points.

                Supplement Recommendations:
                - Recommend supplements that support my goal.
                - Specify dosages, timing, and any precautions.
                - Use bullet points for easy reference.

                Make each section detailed but concise, using bullet points or short paragraphs.
                Avoid using markdown formatting and keep text plain.
                """

        response = model.generate_content(prompt)
        advice_sections = parse_advice(response.text)
        for key in ['diet', 'workout', 'supplements']:
            advice_sections.setdefault(key, "No information available.")

        return render_template("results.html",
                               age=age, weight=weight, height=height, goal=goal,
                               advice=advice_sections)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
