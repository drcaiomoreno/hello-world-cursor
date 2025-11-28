import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Hello World Databricks App",
    page_icon="👋",
    layout="centered"
)

# Main app
def main():
    st.title("👋 Hello World!")
    st.write("Welcome to your first Databricks App!")
    
    st.markdown("---")
    
    # Add some interactive elements
    name = st.text_input("What's your name?", placeholder="Enter your name here")
    
    if name:
        st.success(f"Hello, {name}! Welcome to Databricks Apps! 🎉")
    
    st.markdown("---")
    
    # Display some information
    st.subheader("About this App")
    st.info("""
    This is a simple Hello World Databricks App built with Streamlit.
    
    **Features:**
    - Simple and clean interface
    - Interactive user input
    - Ready to deploy on Databricks
    """)
    
    # Add a button
    if st.button("Click me!"):
        st.balloons()
        st.write("🎈 Thanks for clicking!")

if __name__ == "__main__":
    main()

