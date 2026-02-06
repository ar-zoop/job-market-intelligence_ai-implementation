"""Flask app for job description analysis - listens on port 8000."""
import json
import os
import time

from flask import Flask, jsonify, request

from analyzer import analyze_job_description, analyze_resume

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "job-market-intelligence"})


@app.route("/analyze-job", methods=["POST"])
def analyze_job():
    """
    Analyze a job description and return structured JSON.

    Request body (JSON):
        {
            "job_description": "raw job description text...",
            "save": false  // optional, if true saves to jds/ folder
        }

    Returns:
        JSON with "result" (parsed structured data) or "error" on failure.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    job_description = data.get("job_description")
    if not job_description:
        return jsonify({"error": "Missing required field: job_description"}), 400

    try:
        result_content = analyze_job_description(job_description)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    try:
        parsed = json.loads(result_content)
    except json.JSONDecodeError:
        parsed = {"raw": result_content}

    save = data.get("save", False)
    if save:
        os.makedirs("jds", exist_ok=True)
        filename = f"jds/jd_{int(time.time() * 1000)}.json"
        with open(filename, "w") as f:
            f.write(
                json.dumps(parsed, indent=2)
                if isinstance(parsed, dict)
                else result_content
            )

    return jsonify({"result": parsed})


@app.route("/analyze-resume", methods=["POST"])
def analyze_resume_endpoint():
    """
    Analyze a resume and return structured JSON comparable to job descriptions.

    Request body (JSON):
        {
            "resume": "raw resume text...",
            "save": false  // optional, if true saves to resumes/ folder
        }

    Returns:
        JSON with "result" (parsed structured data) or "error" on failure.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    resume_text = data.get("resume")
    if not resume_text:
        return jsonify({"error": "Missing required field: resume"}), 400

    try:
        raw_analysis_result = analyze_resume(resume_text)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    try:
        parsed_result = json.loads(raw_analysis_result)
    except json.JSONDecodeError:
        parsed_result = {"raw": raw_analysis_result}

    save = data.get("save", False)
    if save:
        os.makedirs("resumes", exist_ok=True)
        filename = f"resumes/resume_{int(time.time() * 1000)}.json"
        with open(filename, "w") as f:
            f.write(
                json.dumps(parsed_result, indent=2)
                if isinstance(parsed_result, dict)
                else raw_analysis_result
            )

    return jsonify({"result": parsed_result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
