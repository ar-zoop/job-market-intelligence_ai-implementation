import os

from analyzer import analyze_job_description

os.makedirs("jds", exist_ok=True)

SAMPLE_JOB_DESCRIPTION_1 = """
Location: Bengaluru / Hybrid

Experience: 1–3 years

Type: Full-time

About Us

At Lyzr, we’re building the next generation of AI-first products — from autonomous agents to full-stack GenAI applications.

We’re looking for a Backend Engineer to join our core engineering team. If you’re excited about powering intelligent systems, building backend services for GenAI apps, and working with LLMs, this is the role for you.

What You’ll Do

Design and develop backend services that power GenAI applications and platforms

Build APIs and infrastructure to support LLM-based features, tools, and agent workflows

Collaborate with frontend, ML, and product teams to create seamless AI experiences

Optimize backend systems for performance, scalability, and reliability

Work with vector databases, data pipelines, and AI model endpoints (OpenAI, Anthropic, Hugging Face, etc.)

Maintain clean, secure, and production-grade code

Contribute to the architecture and roadmap of our GenAI stack

What We’re Looking For

1–3 years of experience in backend development

Proficient in Python

Strong experience with REST APIs, microservices, and scalable cloud infrastructure

Experience building or supporting GenAI applications and/or LLM-powered products

Comfortable working with vector databases (e.g., Pinecone, Weaviate, FAISS) and RAG pipelines

Exposure to cloud services (AWS, GCP, or Azure) and containerization (Docker, Kubernetes)

Excellent problem-solving, communication, and collaboration skills

Nice to Have

Experience building and scaling AI-powered SaaS products

Contributions to open-source GenAI projects

Understanding of prompt engineering and agent orchestration frameworks

Why Join Us

Work on real GenAI applications with end-user impact

Collaborate with a smart, driven team that ships fast

Total ownership and autonomy — no micromanagement
"""


response = analyze_job_description(JOB_DESCRIPTION)
print(response)
with open("jds/jd_1.json", "w+") as f:
    f.write(response)



JOB_DESCRIPTION_2 = """
This role has been designed as "Hybrid" with an expectation that you will work on average 2 days per week from an HPE office.

Who We Are:

Hewlett Packard Enterprise is the global edge-to-cloud company advancing the way people live and work. We help companies connect, protect, analyze, and act on their data and applications wherever they live, from edge to cloud, so they can turn insights into outcomes at the speed required to thrive in today’s complex world. Our culture thrives on finding new and better ways to accelerate what’s next. We know varied backgrounds are valued and succeed here. We have the flexibility to manage our work and personal needs. We make bold moves, together, and are a force for good. If you are looking to stretch and grow your career our culture will embrace you. Open up opportunities with HPE.

Job Description:

HPE Operations is our innovative IT services organization. It provides the expertise to advise, integrate, and accelerate our customers’ outcomes from their digital transformation. Our teams collaborate to transform insight into innovation. In today’s fast paced, hybrid IT world, being at business speed means overcoming IT complexity to match the speed of actions to the speed of opportunities. Deploy the right technology to respond quickly to market possibilities. Join us and redefine what’s next for you.

What you’ll do:

Responsibilities:
• Responsible for conducting advanced research in AI and machine learning. This includes staying up to date with the latest advancements in the field, exploring emerging technologies, and identifying opportunities to apply cutting-edge techniques to solve complex business problems.
• Knowledge of evaluation of traditional AI/ML and Gen-AI based applications - during development phase and in production.
• Responsible for considering scalability, performance, and maintainability while designing the solution.
• Provides technical guidance and mentorship to junior team members. This includes sharing best practices, reviewing code and designs, and helping team members overcome technical challenges. Participate in technical discussions and provide thought leadership within the organization.
• Works closely with stakeholders, such as product managers, data scientists, and business analysts, to understand their requirements and translate them into technical solutions. Collaborate with cross-functional teams to ensure alignment and successful AI and machine learning project implementation.
• Responsible for driving continuous improvement and innovation in the organization's AI and machine learning practices. This involves identifying areas of improvement, exploring new techniques or technologies, and promoting the adoption of best practices.
• Be involved in evaluating and integrating third-party tools or services that can enhance the capabilities of AI solutions.
• Facilitates design review sessions for your projects, ensuring alignment with project requirements and best practices.
• Mentor junior team members during review sessions.
• Collaborates closely with the engineering manager and team lead to refine and iterating on design and implementation strategies, providing constructive feedback to peers.
• Participates in and coordinates meetings, ensuring effective coordination and communication among team members.
• Independently prepares and delivers detailed presentations and reports to stakeholders, translating complex technical concepts into understandable terms for non-technical audiences.
• May be required to interpret and report data findings and maintain or update specific business intelligence tools, databases, dashboards, systems, or methods
• May be involved in the design and development of solutions to complex application problems, system administration issues, or network concerns, where applicable to the role.

Knowledge and Skills:
• Deep understanding of machine learning algorithms, such as linear regression, decision trees, support vector machines, random forests, deep learning models (e.g., neural networks), and reinforcement learning. Proficient in model selection, hyperparameter tuning, and evaluating model performance using appropriate metrics.
• A strong foundation in mathematics and statistics. In-depth knowledge of linear algebra, calculus, probability theory, and statistical concepts. Understanding and developing complex machine learning models and algorithms.
• Proficiency in programming languages such as Python, R, or Java is expected. Experience developing production-level code and familiarity with software engineering best practices, version control systems (e.g., Git), and software development methodologies are also required. Additionally, knowledge of libraries and frameworks like TensorFlow, PyTorch, sci-kit, and Keras is a plus.
• Tasked with designing and architecting AI solutions for complex problems. This involves analyzing business requirements, understanding constraints, and proposing appropriate machine learning models and algorithms.
• Should have proficiency in using agentic frameworks like langGraph or similar other frameworks. Should be knowledgeable in lineage tracking of agentic architectures in general (like usage of langfuse, langsmith).
• Advanced knowledge and experience in deep learning. Understanding advanced neural network architectures (e.g., convolutional neural networks, recurrent neural networks, transformers) and advanced techniques such as transfer learning, generative models, and optimization algorithms for deep learning.
• Actively staying updated with the latest AI and machine learning research advancements. Experience conducting research, exploring emerging technologies, and identifying opportunities to apply state-of-the-art techniques to solve complex problems.
• Provide technical leadership, mentorship, and guidance to junior team members. Must have excellent communication skills to collaborate with cross-functional teams and stakeholders effectively. Possess strong problem-solving and critical thinking abilities to guide projects, make strategic decisions, and solve complex technical challenges.
"""

analysis_result = analyze_job_description(SAMPLE_JOB_DESCRIPTION_2)
print(analysis_result)
with open("jds/jd_2.json", "w+") as f:
    f.write(analysis_result)



