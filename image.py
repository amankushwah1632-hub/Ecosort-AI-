import streamlit as st
import google.generativeai as genai
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Fashion & Clothing Analyzer",
    page_icon="🥻",
    layout="wide"
)

st.title("♻️🤖 EcoSort AI")
st.write("Upload a image and get insights using Gemini 3.6 Flash.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
GOOGLE_API_KEY = "AQ.Ab8RN6L487BnSezbrLsJLXqtw-MHpaJZ9OfMEuQPiMag7GGg1Q"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-3.6-flash")

# -----------------------------
# Image Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Analyze Button
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with col2:

        if st.button("Analyze Image"):

            with st.spinner("Analyzing image..."):

                prompt = """
                You are an AI waste-management and environmental-awareness assistant.

                Analyze the uploaded image of the waste item.

                First identify the visible object.

                Then classify it into the most appropriate category:

                - Biodegradable
                - Recyclable
                - Non-recyclable
                - Hazardous
                - Electronic waste
                - Other

                Perform the following analysis:

                1. Object identification
                2. Waste category
                3. Evidence supporting classification
                4. Recommended disposal method
                5. Potential reuse options
                6. Potential recycling options
                7. Environmental impact of improper disposal
                8. Safety precautions, if applicable

                If the object contains multiple materials, explain the classification carefully.

                OUTPUT FORMAT:

                ## ♻️ Object Identification
                ...

                ## 🗑️ Waste Classification
                Category:
                Confidence:

                ## 🔍 Why This Classification?
                ...

                ## 🚮 Recommended Disposal
                ...

                ## 🔄 Reuse/Recycling Possibilities
                ...

                ## 🌍 Environmental Impact
                ...

                ## ⚠️ Safety Considerations
                ...

                Do not classify an object with certainty if the image does not provide sufficient evidence.
                """

                response = model.generate_content(
                    [prompt, image]
                )

                st.subheader("Analysis Result")
                st.write(response.text)
