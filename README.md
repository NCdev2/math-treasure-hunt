# Math Treasure Hunt Streamlit App

This is a Streamlit application adapted from an HTML/JavaScript math treasure hunt game.

## To Run Locally:

1.  **Clone the repository (or ensure you have the files).**
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run src/app.py
    ```

The application will open in your web browser.

## Project Structure:

```
math-treasure-hunt/
├── src/
│   └── app.py           # Main Streamlit application code
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Features:

*   Browse through various mathematical topics.
*   Topics are unlocked sequentially.
*   Navigate using "Next" and "Previous" buttons or a dropdown menu.
*   A completion message is displayed when all topics are viewed.
*   Thematic styling inspired by ancient scrolls and exploration.
*   Mathematical formulas rendered using LaTeX (via Streamlit's `st.latex` or embedded MathJax in HTML strings).

## Original HTML Version:

The `math_treasure.html` file (if included in the repository or your local copy) is the original single-page web application that this Streamlit app is based on.
