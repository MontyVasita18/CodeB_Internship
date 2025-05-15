import streamlit as st
import pickle
import numpy as np

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("🔐 Phishing Website Detection App")
st.write("Enter the following URL characteristics to detect if it's phishing or legitimate.")

# INPUTS — these are example features, adjust as needed
length_url = st.number_input("Length of URL", min_value=0)
length_hostname = st.number_input("Length of Hostname", min_value=0)
ip = st.selectbox("Is there an IP in URL?", [0, 1])  # 1 = Yes, 0 = No
nb_dots = st.number_input("Number of Dots in URL", min_value=0)
nb_hyphens = st.number_input("Number of Hyphens", min_value=0)
nb_at = st.number_input("Number of '@' symbols", min_value=0)
nb_qm = st.number_input("Number of '?' in URL", min_value=0)
nb_eq = st.number_input("Number of '=' in URL", min_value=0)
http_in_path = st.selectbox("Contains 'http' in path?", [0, 1])
https_token = st.selectbox("Contains 'https' token in URL?", [0, 1])
ratio_digits_url = st.slider("Ratio of digits in URL", 0.0, 1.0, 0.0)
domain_registration_length = st.number_input("Domain Registration Length (in days)", min_value=0)
domain_age = st.number_input("Domain Age (in days)", min_value=0)
web_traffic = st.slider("Web Traffic (0 = low, 1 = high)", 0.0, 1.0, 0.5)
dns_record = st.selectbox("DNS Record Available?", [0, 1])
google_index = st.selectbox("Indexed by Google?", [0, 1])
page_rank = st.slider("Page Rank (0 = low, 1 = high)", 0.0, 1.0, 0.5)

# Collect input values in the correct order (as expected by the model)
input_features = np.array([[length_url, length_hostname, ip, nb_dots, nb_hyphens, nb_at,
                            nb_qm, nb_eq, http_in_path, https_token, ratio_digits_url,
                            domain_registration_length, domain_age, web_traffic, dns_record,
                            google_index, page_rank]])

# Predict
if st.button("🔍 Predict"):
    result = model.predict(input_features)
    if result[0] == 1:
        st.error("⚠️ Phishing Website Detected!")
    else:
        st.success("✅ This URL appears to be Legitimate.")
