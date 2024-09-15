from flask import Blueprint, render_template, request, jsonify, Flask
from speech import Can_to_eng
from speech import Eng_to_can

app = Flask(__name__, static_folder="webpage/static")

# Initialize the speech engine once at the start
Can_to_eng.initialize_speech_engine()
is_listening = False

bp = Blueprint("pages", __name__, template_folder="webpage/templates")


@bp.route("/")
def home():
    return render_template("pages/home.html")


@bp.route("/about")
def about():
    return render_template("pages/about.html")


@bp.route("/translate")
def translate_page():
    return render_template("pages/translate.html")


@bp.route("/translate", methods=["POST"])
def translate():
    translation_type = request.form["type"]

    if translation_type == "cantonese_to_english":
        result = (
            Can_to_eng.translate_cantonese_to_english_speech()
        )  # Cantonese to English translation
        Can_to_eng.SpeakText(result)
        return jsonify({"result": result})

    elif translation_type == "english_to_cantonese":
        # Call the method and capture the recognized text
        recognized_text = Eng_to_can.translate_english_to_cantonese_speech()
        if recognized_text:
            print(f"Captured recognized text: {recognized_text}")
            return jsonify({"result": recognized_text})
        else:
            return jsonify({"error": "No recognized text returned"})

    elif translation_type == "sign_language":
        video_file = request.files["video"]
        result = translate_sign_language(video_file)  # Handle sign language translation
        SpeakText(result)
        return jsonify({"result": result})

    return jsonify({"error": "Invalid translation type"}), 400


@app.route("/start-listening", methods=["POST"])
def start_listening():
    global is_listening
    is_listening = True
    # You can call the function based on which translation is needed (Cantonese to English or vice versa)
    # For simplicity, let's assume we are doing Cantonese to English translation
    result = (
        Can_to_eng.translate_cantonese_to_english_speech()
    )  # This function now returns the result
    print(f"Translation result: {result}")  # Debugging
    return jsonify(
        {"result": result, "input": "Cantonese Speech"}
    )  # Adjusted for demonstration


@app.route("/stop-listening", methods=["POST"])
def stop_listening():
    global is_listening
    is_listening = False
    # Logic to stop the listening process can go here if needed
    return jsonify({"result": "Listening stopped"})


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
