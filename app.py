from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # type: ignore

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

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
    
    # Convert lists to strings and handle empty sections
    return {k: '\n'.join(v) if v else "No recommendations provided for this section." for k,v in result.items()}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = request.form.get("age")
        weight = request.form.get("weight")
        height = request.form.get("height")
        goal = request.form.get("goal")

        image = request.files.get("image")
        image_path = None
        if image and image.filename:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image.save(image_path)

        model = genai.GenerativeModel("gemini-1.5-flash")  # type: ignore
        prompt = f"""
                I am a {age}-year-old person with a height of {height} cm and weight of {weight} kg. 
                My target goal is to {goal}.

                Provide a personalized lifestyle coaching plan with CLEAR SECTION HEADERS in this exact format:

                Diet Advice:
                [Your diet recommendations here and list of foods to include/exclude. Add bullet points for clarity]

                Workout Plan:
                [List of exercises, duration, and frequency in bullet points]

                Supplement Recommendations:
                [List of supplements, dosages, and timing]

                Make each section detailed but concise, using bullet points or short paragraphs. 
                Avoid using markdown formatting and keep text plain.
                """

        response = model.generate_content(prompt)
        advice_sections = parse_advice(response.text)
        for key in ['diet', 'workout', 'supplements']:
            advice_sections.setdefault(key, "No information available.")

        return render_template("results.html",
                               age=age, weight=weight, height=height, goal=goal,
                               advice=advice_sections,
                               image_path=image_path,) 

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
