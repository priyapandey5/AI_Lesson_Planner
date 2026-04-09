import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import date

load_dotenv()  # load .env file

# Set your OpenAI API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# 3️⃣ Port config (for Render)
port = int(os.environ.get("PORT", 8501))

# Define the system message for lesson generation
system_message = """
You are an AI English teacher who is really good and knows how to teach children of all standards. You will be provided with lesson strategy plan queries. You have to assist teachers and schools to make 
new lesson plans that are more interactive for students. Explain all following processes in detail so teachers 
will understand what you mean and what to do. Also provide a strategy so teachers will know step-wise when and what to show, for example, the video you provide.

The lesson strategy plan query will be delimited with #### characters.

You will get input in JSON format from users that are school teachers in the following format:
'Lesson Title': <It will be the string that describes the lesson title>
'Subject': <The user will give you the Subject name>
'Grade': <The user will provide which grade the students are, so you have to explain it related to the respective grade and consider the student understanding at that age>
'Duration': <Will be an integer, for example 1 or 2, based on the integer provided you have to write a lesson strategy plan. Keep in mind each session is 50 minutes>
'Key vocabulary': <It will be in python list format that gives you an understanding of which part to focus on more.>
'Supporting Materials and resources': <It will be the options like video, Microsoft office, etc. If any are available, you have to use that method or tools in strategy material. For video, you have to suggest a video or tutorial from the internet.>

You have to give a lesson plan that will help teachers to teach the topic in their classrooms.

NOTE: The output should be in a detailed lesson plan format for easy reading and application in a classroom.
"""

delimiter = "####"

# Function to get a response from OpenAI based on messages
@st.cache_data
def get_completion_from_messages(messages):
    try:
        # Combine messages into single prompt
        prompt = ""
        for msg in messages:
            prompt += f"{msg['role'].upper()}: {msg['content']}\n\n"

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while generating the lesson plan: {str(e)}")
        return None

# Streamlit app starts here
st.set_page_config(page_title="Lesson Plan Generator", page_icon="📚", layout="wide")
st.title("📚 Lesson Plan Generator")
st.write("Enter the details below to generate a comprehensive lesson plan.")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    lesson_title = st.text_input("Lesson Title", help="Enter the title of your lesson")
    subject = st.text_input("Subject", help="Enter the subject of the lesson")
    grade = st.number_input("Grade", min_value=1, max_value=12, step=1, help="Select the grade level")

with col2:
    duration = st.number_input("Duration (in hours)", min_value=1, max_value=10, step=1, help="Enter the duration of the lesson in hours")
    key_vocabulary = st.text_input("Key Vocabulary", help="Enter key vocabulary words, separated by commas")
    supporting_materials = st.text_area("Supporting Materials and Resources", help="List any supporting materials or resources, separated by commas")

# When user submits the form
if st.button("Generate Lesson Plan", type="primary"):
    with st.spinner("Generating your lesson plan... This may take a moment."):
        # Parse inputs
        key_vocabulary_list = [item.strip() for item in key_vocabulary.split(",")]
        materials_list = [item.strip() for item in supporting_materials.split(",")]

        # Prepare user message for OpenAI
        user_message = f""""Lesson Title": "{lesson_title}"\n"Subject": "{subject}"\n"Grade": "{grade}"
        \n"Duration": "{duration}"\n"Key Vocabulary": {key_vocabulary_list}
        \n"Supporting Materials and Resources": {materials_list}"""

        messages = [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': f"{delimiter}{user_message}{delimiter}"},
        ]

        # Get response from OpenAI
        lesson_plan_response = get_completion_from_messages(messages)
        
        if lesson_plan_response:
            st.success("Lesson Plan Generated Successfully!")
            
            # Display the lesson plan in a more structured way
            st.subheader("📘 Lesson Plan")
            st.markdown(lesson_plan_response, unsafe_allow_html=True)

            # Option to download the lesson plan as a text file
            st.download_button(
                label="Download Lesson Plan (Text)",
                data=lesson_plan_response,
                file_name=f"lesson_plan_{date.today()}.txt",
                mime="text/plain"
            )
        else:
            st.warning("Failed to generate the lesson plan. Please try again.")

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Your AI Lesson Planner")

