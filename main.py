import streamlit as st

class App:
    def __init__(self):
        self.pages = {
            "Home": self.home_page,
            # "House Price Prediction": HousePricePrediction()
        }

    def home_page(self):
        st.title("Machine Learning Prediction App")
        st.write("""
        Welcome to the Machine Learning Prediction App. Use the sidebar to navigate to different prediction pages.
        - **House Price Prediction**: Predict the price of a house based on various features.
        """)

    def run(self):
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Select a Page", list(self.pages.keys()))

        if page == "Home":
            self.home_page()
        else:
            self.pages[page].run()

if __name__ == "__main__":
    app = App()
    app.run()
