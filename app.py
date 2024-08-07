import streamlit as st
import base64

# Define the maximum size for the text input (20MB in base64)
MAX_SIZE = 20 * 1024 * 1024  # 20MB


def sidebar():
    with st.sidebar:
        st.header("How to Use")
        st.info("""
                 + Prepare your base64 text
                 + Copy-paste to the 'Base64 Text Input'
                 + Click 'Submit' button
                 + Enter the filename and extension
                 + Click 'Download' button""")
        st.divider()
        st.write("Raise issues and ⭐ at [github.com/ahmad-alkadri/st-base64tobin](https://github.com/ahmad-alkadri/st-base64tobin)")


def main():
    st.set_page_config(
        page_title="Base64 to Binary File Converter",
        page_icon="🌏",
        initial_sidebar_state="collapsed",
    )
    st.title("Base64 to Binary File Converter")

    sidebar()

    with st.form(key="base64-text-input"):
        text_input = st.text_area("Base64 Text Input", height=300, max_chars=MAX_SIZE)
        st.form_submit_button("Submit")

    if len(text_input) > MAX_SIZE:
        st.error("Input is too large. Please enter text less than 20MB.")
    elif text_input:
        with st.spinner("Decoding, please wait..."):
            try:
                # Decode base64 text to binary data
                binary_data = base64.b64decode(text_input)

                # Prompt for the filename
                filename = st.text_input("Filename (with extension)", "output.bin")

                if filename:
                    # Use st.download_button to create a download button for the binary file
                    st.download_button(
                        label="Download File",
                        data=binary_data,
                        file_name=filename,
                        mime="application/octet-stream",
                    )
            except Exception as e:
                st.error(f"Error decoding base64 text: {e}")


if __name__ == "__main__":
    main()
