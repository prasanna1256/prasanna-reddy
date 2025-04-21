import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import altair as alt
import streamlit.components.v1 as components

# --- Basic Information ---
name = "Prasanna Reddy Tavanam"
title = "Entry-Level Python Programmer | Python Developer Intern | Python Developer"
email = "prasannareddytavanam@gmail.com"
linkedin_url = "https://www.linkedin.com/in/prasanna-reddy-tavanam-29682123b/"
github_url = "https://github.com/prasanna1256/"
profile_picture = Image.open("profile.jpg")  # Replace

# --- About Section ---
about_me_detailed = """
## About Me

Hi, I'm Prasanna Reddy, a highly skilled recent graduate with a proven track record in Python,SQL,ML,AI,etc.

My journey in B.Tech-IT has been driven by a passion for coding. I excel at Python,SQL,Java,ML,AI,etc., and thrive in collaborative environments.

I'm a lifelong learner, constantly exploring new technologies and methodologies to stay at the forefront of Information Technology & Computer Science. I'm eager to connect with fellow professionals and explore opportunities for innovation.

Key Strengths:
- Problem Solving
- Programming
- Consistent Learner
"""

# --- Interactive Skills Visualization ---
skills_data_detailed = [
    {"name": "Python", "value": 95, "description": "Highly proficient in Python for various applications including data science, machine learning, web development (Streamlit), and automation.", "projects": ["Multimodal Smart Tutor", "TalentScout"]},
    {"name": "Transformers", "value": 95, "description": "proficient in Transformers and used hugging faces to develop multimodal projects.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "Machine Learning", "value": 90, "description": "Extensive experience in developing and deploying various machine learning models for classification, regression, and clustering.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "Artificial Intelligence", "value": 90, "description": "Strong understanding and practical experience in broader AI concepts, including machine learning, deep learning, and natural language processing.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "Java", "value": 90, "description": "Good command of Java for building scalable and robust applications.", "projects": ["Contacts manager"]},
    {"name": "SQL", "value": 88, "description": "Proficient in relational database management systems (RDBMS) and writing complex SQL queries.", "projects": ["Library management System"]},
    {"name": "Streamlit", "value": 92, "description": "Highly skilled in building interactive and user-friendly data science and machine learning web applications using Streamlit.", "projects": ["Multimodal Smart Tutor", "Face Detector and Text Extractor","TalentScout"]},
    {"name": "PyTorch", "value": 80, "description": "Experienced in using PyTorch for deep learning model development and experimentation.", "projects": ["Multimodal Smart Tutor", "Face Detector & Text Extractor"]},
    {"name": "OpenCV", "value": 80, "description": "Competent in using OpenCV for computer vision tasks such as image processing and analysis.", "projects": ["Multimodal Smart Tutor", "Face Detector & Text Extractor"]},
    {"name": "NumPy & Tensorflow", "value": 95, "description": "Expertise in using NumPy,Tensorflow for efficient numerical computations in Python.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "Pandas", "value": 95, "description": "Mastery of Pandas for data manipulation, cleaning, and analysis in Python.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "Matplotlib", "value": 90, "description": "Skilled in creating static, interactive, and animated visualizations in Python using Matplotlib.", "projects": ["Face Detector & Text Extractor"]},
    {"name": "Scikit-learn", "value": 88, "description": "Proficient in using scikit-learn for various machine learning tasks, including model selection and evaluation.", "projects": ["TalentScout"]},
    {"name": "Natural Language Processing (NLP)", "value": 85, "description": "Experienced in applying NLP techniques for text analysis, understanding, and generation.", "projects": ["Multimodal Smart Tutor"]},
    {"name": "GenAI", "value": 82, "description": "Familiar with Generative AI models and their applications.", "projects": ["Multimodal Smart Tutor", "TalentScout"]},
    {"name": "AWS (Basics)", "value": 50, "description": "Basic understanding of Amazon Web Services and some of its core services.", "projects": ["Recipe Creation-Chef Challenge-Vertex AI"]},
]

# --- Dynamic Project Showcase ---
projects_advanced = [
    {
        "title": "Multimodal Educational Assistant With real-time",
        "category": "AI & ML",
        "description": "Developed a Multimodal AI Enhanced Educational Assistant with RealTime Q&A with Python,Tensorflow,NLP,API's.",
        "technologies": ["Python", "TensorFlow", "Generative AI", "Transformers",'NLP',"Gemini"],
        "github": "https://github.com/prasanna1256/Multimodal-Educational-Assistant-with-real-time-QA-and-Dynamic-learning-support/tree/main",
        "live_demo": "https://drive.google.com/file/d/1r0hIOFs4svL94ztrnzeyhAwgHiAc9mHG/view?usp=sharing",
    },
    {
        "title": "TalentScout-The hiring Assistant",
        "category": "AI & ML",
        "description": "Built a dynamic chatbot using Streamlit and it helps in guiding to get a job by checking your skills set based on job desctiption and guides you to focus on weak angles.",
        "technologies": ["Python", "Streamlit", "Pandas", "Generative AI","Gemini"],
        "github": "https://github.com/prasanna1256/TalentScout-An-AI-Hiring-Assistant",
        "live_demo": "https://www.loom.com/share/c060df5d96d240b6a04e7ef4451e587f?sid=96192eac-a2ef-4df8-bd96-ae3ac89f71a6",
    },
    {
        "title": "Face mask Detector using Python",
        "category": "Streamlit Application",
        "description": "Developed a responsive web application for detecting mask on face and it gives with 95 percent accuracy,based on quality of picture.",
        "technologies": ["python", "PyTesseract", "OpenCV", "PyTorch", "Pillow"],
        "github": "https://github.com/prasanna1256/face-mask-detector",
        "live_demo": None,
    },
    # Add more advanced projects
]

project_categories = ["All"] + sorted(list(set(p["category"] for p in projects_advanced)))

# --- Contact Form with EmailJS Placeholder ---
emailjs_service_id = "service_eais0yp"  # Replace with your EmailJS service ID
emailjs_template_id = "template_q0xdkfp"  # Replace with your EmailJS template ID
emailjs_public_key = "U8EDJJJ1O0dX2LG-6"  # Replace with your EmailJS public key

contact_message_advanced = "Let's connect! Feel free to send me a message."

# --- Streamlit App ---
st.set_page_config(page_title=f"Portfolio - {name}", page_icon=":rocket:", layout="wide")

# --- Custom CSS for Enhanced Styling ---
st.markdown(
    """
    <style>
    .big-font {
        font-size:2rem !important;
        font-weight: bold;
    }
    .skill-badge {
        background-color: #f0f2f6;
        color: #333;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        margin-right: 0.3rem;
    }
    .project-card {
        border: 1px solid #ddd;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 5px;
    }
    .project-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .tech-stack {
        font-size: 0.9rem;
        color: #777;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar ---
with st.sidebar:
    st.image(profile_picture, width=200)
    st.header(name)
    st.subheader(title)
    st.write("---")
    st.info(contact_message_advanced)
    st.write(f"[LinkedIn]({linkedin_url})")
    st.write(f"[GitHub]({github_url})")
    st.write(f"Email: {email}")

    st.write("---")
    st.subheader("Navigation")
    menu_items = ["About", "Skills", "Projects", "Contact"]
    selected_menu = st.radio("", menu_items)

# --- Main Content ---
if selected_menu == "About":
    st.markdown("<p class='big-font'>About Me</p>", unsafe_allow_html=True)
    st.markdown(about_me_detailed)

elif selected_menu == "Skills":
    st.markdown("<p class='big-font'>Skills Proficiency</p>", unsafe_allow_html=True)
    st.markdown("Here's a visual representation of my key skills and expertise:")
    options = {
        "series": [
            {
                "type": "gauge",
                "detail": {"formatter": "{value}%"},
                "description": [{"name": skill["name"], "value": skill["value"]} for skill in skills_data_detailed],
                "tooltip": {
                    "formatter": """function(params) {
                        const skill = params.name;
                        const value = params.value;
                        const description = skillsDataDetailed.find(s => s.name === skill).description;
                        return skill + ': ' + value + '%<br>' + description;
                    }"""
                },
                "itemStyle": {"color": "#4CAF50"},
            }
        ],
    }

    with st.expander("More details on my skills"):
        for skill in skills_data_detailed:
            st.subheader(skill["name"])
            st.write(skill["description"])
            st.write(f"Key Projects: {', '.join(skill['projects'])}")
            st.write("---")

elif selected_menu == "Projects":
    st.markdown("<p class='big-font'>Projects</p>", unsafe_allow_html=True)
    st.sidebar.subheader("Filter Projects")
    selected_category_proj = st.sidebar.selectbox("Category", project_categories)

    filtered_projects_adv = projects_advanced if selected_category_proj == "All" else [
        p for p in projects_advanced if p["category"] == selected_category_proj
    ]

    cols = st.columns(2)
    for i, project in enumerate(filtered_projects_adv):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"<p class='project-title'>{project['title']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='tech-stack'>Technologies: {', '.join(project['technologies'])}</p>", unsafe_allow_html=True)
                st.write(project["description"])
                st.write(f"[GitHub]({project['github']})")
                if project["live_demo"]:
                    st.write(f"[Live Demo]({project['live_demo']})")

elif selected_menu == "Contact":
    st.markdown("<p class='big-font'>Contact Me</p>", unsafe_allow_html=True)
    st.info(contact_message_advanced)

    with st.form("contact_form"):
        name_contact = st.text_input("Your Name")
        email_contact = st.text_input("Your Email")
        message_contact = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name_contact and email_contact and message_contact:
                js_code = f"""
                    <script type="text/javascript">
                        emailjs.send('{emailjs_service_id}', '{emailjs_template_id}', {{
                            from_name: '{name_contact}',
                            from_email: '{email_contact}',
                            message: '{message_contact}'
                        }}, '{emailjs_public_key}')
                        .then(function(response) {{
                           alert('Message sent successfully!');
                        }}, function(error) {{
                           alert('Failed to send message. Please try again later.');
                        }});
                    </script>
                """
                components.html(js_code, height=0)
                st.success("Message sent successfully!")
            else:
                st.warning("Please fill in all the fields.")

# --- Footer ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: gray;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(f'<div class="footer">© 2025 {name} - Built with Streamlit</div>', unsafe_allow_html=True)
