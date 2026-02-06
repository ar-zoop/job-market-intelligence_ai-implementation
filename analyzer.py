"""Job description analyzer module - extracts structured JSON from raw job descriptions."""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
import os

load_dotenv()

JOB_DESCRIPTION_SCHEMA = """
{
  "job_id": "string",
  "role_type": "backend | ai-adjacent | infra | platform",
  "seniority": "junior | mid | senior",
  "required_experience_years": "number",
  "required_skills": ["string"],
  "programming_languages": ["string"],
  "nice_to_have_skills": ["string"],
  "domain": "string"
}
"""

JOB_DESCRIPTION_SYSTEM_PROMPT = SystemMessage(
    content="""
You are a senior technical recruiter with backend engineering experience.

Your task is to analyze a job description and convert it into a structured JSON object.

Rules:
- Infer the TRUE nature of the role based on responsibilities, not just the title.
- If AI/ML is mentioned but responsibilities do NOT include model training, evaluation, or experimentation, classify the role as "ai-adjacent".
- If the role involves designing, training, evaluating, or researching machine learning models
  (including algorithms, deep learning architectures, hyperparameter tuning, or mathematical foundations),
  classify the role as "ai" (core AI), NOT "ai-adjacent".
- Core AI ownership always overrides backend, platform, or infrastructure responsibilities.
- Classify the roles based on the responsibilities and required skills.
- Mark skills as "required" ONLY if they are central to the responsibilities.
- If experience requirements are inflated or inconsistent with responsibilities, downgrade them.
- Do not invent skills that are not present in the text.
- If the required years of experience is given as a range, take the lower bound.
- Skills mentioned as "exposure" or examples should be treated as nice-to-have, not required.
- Do NOT invent or infer authoritative identifiers. If a job ID is not explicitly present, generate a simple, human-readable slug and treat it as a non-authoritative identifier. It should contain the company name + location + role (e.g., "lyzr-bengaluru-backend-engineer").
- Seniority must be derived primarily from explicit years-of-experience requirements.
- If experience is 1–3 years, classify the role as "junior" unless leadership or ownership is explicitly stated.
- If experience is 0-1 years, classify the role as "entry-level".
- Ignore internal level labels (e.g., L3, L4, L5) unless clearly mapped to years of experience.
- Output must strictly follow the provided JSON schema.
- Output ONLY valid JSON. No explanations.
"""
)


def get_llm():
    """Return configured ChatOpenAI instance."""
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://api.deepseek.com",
    )


RESUME_SCHEMA = """
{
  "experience_years": "number",
  "skills": ["string"]
  "role_type": ["backend | ai-adjacent | infra | platform"]
}
"""

RESUME_SYSTEM_PROMPT = SystemMessage(
    content="""
You are a senior technical recruiter with backend engineering experience.

Your task is to analyze a resume and convert it into a structured JSON object.

Rules:
- Calculate total years of experience from all work experience listed in the resume.
- Infer seniority based on total years of experience and responsibilities:
  - 0-2 years: "junior"
  - 3-5 years: "mid"
  - 6+ years: "senior"
- Extract all technical skills mentioned in the resume (tools, frameworks, technologies, programming languages).
- Infer role types based on work experience and responsibilities:
  - "backend" if they've worked on backend services, APIs, microservices
  - "ai-adjacent" if they've worked with AI/ML tools (including if they've designed, trained, or evaluated ML models - use "ai-adjacent" to match job description schema)
  - "infra" if they've worked on infrastructure, DevOps, cloud infrastructure
  - "platform" if they've worked on platform engineering, developer tools, internal platforms
- Only include skills that are explicitly mentioned or clearly inferable from the resume.
- Do not invent skills or experiences that are not present in the text.
- Output must strictly follow the provided JSON schema.
- Output ONLY valid JSON. No explanations.
"""
)


def analyze_job_description(job_description: str) -> str:
    """
    Analyze a job description and return structured JSON.

    Args:
        job_description: Raw job description text.

    Returns:
        JSON string of the analyzed job structure.
    """
    llm = get_llm()
    user_prompt = (
        "Convert the following job description into JSON using this schema: "
        + JOB_DESCRIPTION_SCHEMA
        + " Job Description: "
        + job_description
    )
    response = llm.invoke(
        [
            JOB_DESCRIPTION_SYSTEM_PROMPT,
            {"role": "user", "content": user_prompt},
        ]
    )
    return response.content


def analyze_resume(resume_text: str) -> str:
    """
    Analyze a resume and return structured JSON comparable to job descriptions.

    Args:
        resume_text: Raw resume text.

    Returns:
        JSON string of the analyzed resume structure.
    """
    llm = get_llm()
    user_prompt = (
        "Convert the following resume into JSON using this schema: "
        + RESUME_SCHEMA
        + " Resume: "
        + resume_text
    )
    response = llm.invoke(
        [
            RESUME_SYSTEM_PROMPT,
            {"role": "user", "content": user_prompt},
        ]
    )
    return response.content
