import streamlit as st
import joblib
from pypdf import PdfReader


# --------------------------------------------------
# Load trained model
# --------------------------------------------------

model = joblib.load("resume_classifier.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="centered"
)


# --------------------------------------------------
# Custom styling
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #666666;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">📄 Resume Screening System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Upload a resume and use the trained machine learning model '
    'to classify it as <b>Shortlist</b> or <b>Review</b>.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# File upload
# --------------------------------------------------

st.subheader("Upload Resume")

uploaded_file = st.file_uploader(
    "Select a PDF resume",
    type=["pdf"]
)


# --------------------------------------------------
# Analyze resume
# --------------------------------------------------

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    st.write(
        f"File size: {uploaded_file.size / 1024:.1f} KB"
    )

    if st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    ):

        # --------------------------------------------------
        # Read PDF
        # --------------------------------------------------

        reader = PdfReader(uploaded_file)

        # --------------------------------------------------
        # Extract text
        # --------------------------------------------------

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        # --------------------------------------------------
        # Check extraction
        # --------------------------------------------------

        if resume_text.strip() == "":

            st.error(
                "Unable to extract readable text from this PDF."
            )

        else:

            # --------------------------------------------------
            # Make prediction
            # --------------------------------------------------

            prediction = model.predict([resume_text])[0]

            # --------------------------------------------------
            # Get probabilities
            # --------------------------------------------------

            probabilities = model.predict_proba([resume_text])[0]

            classes = model.classes_

            shortlist_probability = probabilities[
                list(classes).index("shortlist")
            ] * 100

            review_probability = probabilities[
                list(classes).index("review")
            ] * 100

            confidence = max(probabilities) * 100

            # --------------------------------------------------
            # Display result
            # --------------------------------------------------

            st.divider()

            st.subheader("Screening Result")

            if confidence < 70:

                st.warning(
        "⚠️ LOW CONFIDENCE — HUMAN REVIEW RECOMMENDED"
                         )

                st.write(
                "The model is not sufficiently confident in this prediction. "
                "Please review the resume manually."
                )

            elif prediction == "shortlist":

                st.success(
        "✅ RECOMMENDATION: SHORTLIST"
            )

                st.write(
        "The model classified this resume "
        "as a potential shortlist candidate."
        )

            else:

                st.warning(
        "⚠️ RECOMMENDATION: REVIEW"
                 )

                st.write(
        "The model recommends that this resume "
        "be reviewed further."
            )

# --------------------------------------------------
# Display probabilities
# --------------------------------------------------

        st.metric(
            "Model Confidence",
             f"{confidence:.1f}%"
            )

        st.write(
            f"**Shortlist probability:** "
                f"{shortlist_probability:.1f}%"
            ) 

        st.write(
         f"**Review probability:** "
            f"{review_probability:.1f}%"
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "AI-Powered Resume Screening System"
)