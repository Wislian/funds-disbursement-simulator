import streamlit as st
import requests


def main():
    st.set_page_config(
        page_title="Funds Disburment Dashboard Readme",
        page_icon = "💸",
        layout="wide"
    )
    github_url = "https://raw.githubusercontent.com/Wislian/funds-disbursement-simulator/main/README.md"

    try:
        response = requests.get(github_url)
        response.raise_for_status()
        readme_content = response.text
        st.markdown(readme_content, unsafe_allow_html=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to load:\n{str(e)}")

if __name__ == "__main__":
    main()



    

