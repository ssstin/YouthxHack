from flask import Blueprint, render_template, request, jsonify, Flask
from can_to_eng import *
from eng_to_can import *

app = Flask(__name__)

# Initialize the speech engine once at the start
initialize_speech_engine()
is_listening = False

bp = Blueprint("pages", __name__, template_folder='templates/pages')

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/translate")
def translate_page():
    return render_template("pages/translate.html")

@bp.route('/translate', methods=['POST'])
def translate():
    translation_type = request.form['type']
    
    if translation_type == 'cantonese_to_english':
        result = translate_cantonese_to_english_speech()  # Cantonese to English translation
        SpeakText(result)
        return jsonify({'result': result})
    
    elif translation_type == 'english_to_cantonese':
        result = translate_english_to_cantonese_speech()  # English to Cantonese translation
        SpeakText(result)
        return jsonify({'result': result})
    
    elif translation_type == 'sign_language':
        video_file = request.files['video']
        result = translate_sign_language(video_file)  # Handle sign language translation
        SpeakText(result)
        return jsonify({'result': result})

    return jsonify({'error': 'Invalid translation type'}), 400

@app.route('/start-listening', methods=['POST'])
def start_listening():
    global is_listening
    is_listening = True
    # You can call the function based on which translation is needed (Cantonese to English or vice versa)
    # For simplicity, let's assume we are doing Cantonese to English translation
    result = translate_cantonese_to_english_speech()  # This function now returns the result
    print(f"Translation result: {result}")  # Debugging
    return jsonify({'result': result, 'input': 'Cantonese Speech'})  # Adjusted for demonstration

@app.route('/stop-listening', methods=['POST'])
def stop_listening():
    global is_listening
    is_listening = False
    # Logic to stop the listening process can go here if needed
    return jsonify({'result': 'Listening stopped'})

if __name__ == '__main__':
    app.run(debug=True)
