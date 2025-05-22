import streamlit as st

# --- Topics Data ---
topics_data = [
    # Category: Algebra & Polynomials
    {
        "id": "index_laws", "title": "The Scroll of Index Laws", "category": "Algebra & Polynomials",
        "explanation": r"""<p>Index laws (or exponent laws) are rules for simplifying expressions with powers. Here are the key laws:</p>
            <ul class="explanation-list">
                <li>$a^m \times a^n = a^{m+n}$ (Product of powers)</li>
                <li>$a^m \div a^n = a^{m-n}$ (Quotient of powers)</li>
                <li>$(a^m)^n = a^{mn}$ (Power of a power)</li>
                <li>$(ab)^n = a^n b^n$ (Power of a product)</li>
                <li>$(\frac{a}{b})^n = \frac{a^n}{b^n}$ (Power of a quotient)</li>
                <li>$a^0 = 1$ (for $a \neq 0$) (Zero exponent)</li>
                <li>$a^{-n} = \frac{1}{a^n}$ (Negative exponent)</li>
                <li>$a^{m/n} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m$ (Fractional exponent)</li>
            </ul>"""
    },
    {
        "id": "factorising", "title": "The Art of Factorising", "category": "Algebra & Polynomials",
        "explanation": r"""<p>Factorising is the reverse of expanding brackets. It involves writing an expression as a product of its factors. Some common forms include:</p>
            <ul class="explanation-list">
                <li>Common Factor: $ax + ay = a(x+y)$</li>
                <li>Difference of Two Squares: $a^2 - b^2 = (a-b)(a+b)$</li>
                <li>Trinomials (e.g., $x^2 + bx + c$): Look for two numbers that multiply to $c$ and add to $b$.</li>
                <li>Grouping: For expressions with four terms, group pairs of terms.</li>
            </ul>"""
    },
    {
        "id": "factor_theorem", "title": "The Factor Theorem's Secret", "category": "Algebra & Polynomials",
        "explanation": r"""<p>The Factor Theorem is a powerful tool for factorising polynomials.</p>
            <ul class="explanation-list">
                <li>It states that if $P(x)$ is a polynomial, then $(x-a)$ is a factor of $P(x)$ if and only if $P(a) = 0$.</li>
                <li>This helps find linear factors of higher-degree polynomials.</li>
            </ul>"""
    },
    # Category: Proof
    {
        "id": "math_proof", "title": "The Essence of Mathematical Proof", "category": "Proof",
        "explanation": r"""<p>A mathematical proof is a rigorous argument that demonstrates the truth of a mathematical statement.</p>
            <ul class="explanation-list">
                <li>It relies on axioms, definitions, and previously proven theorems.</li>
                <li>Common methods include: Proof by Deduction, Proof by Contradiction, Proof by Induction, and Disproof by Counterexample.</li>
            </ul>"""
    },
    # Category: Quadratics
    {
        "id": "solving_quadratics", "title": "Solving Quadratic Equations", "category": "Quadratics",
        "explanation": r"""<p>Solving quadratic equations means finding values of $x$ for equations typically in the form $ax^2 + bx + c = 0$. Methods include:</p>
            <ul class="explanation-list">
                <li>By factorisation (if possible).</li>
                <li>Using the quadratic formula, which is $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$</li>
                <li>By completing the square.</li>
            </ul>"""
    },
    {
        "id": "discriminant", "title": "The Revealing Discriminant", "category": "Quadratics",
        "explanation": r"""<p>The discriminant of a quadratic equation $ax^2+bx+c=0$ is given by the expression $\Delta = b^2-4ac$. The value of the discriminant reveals the nature of the roots:</p>
            <ul class="explanation-list">
                <li>If $\Delta > 0$, there are two distinct real roots.</li>
                <li>If $\Delta = 0$, there is one repeated real root (or two equal real roots).</li>
                <li>If $\Delta < 0$, there are no real roots (instead, there are two complex conjugate roots).</li>
            </ul>"""
    },
    # Category: Coordinate Geometry
    {
        "id": "equation_straight_line", "title": "The Path of Straight Lines", "category": "Coordinate Geometry",
        "explanation": r"""<p>The equation of a straight line describes its path in the Cartesian plane. Common forms are:</p>
            <ul class="explanation-list">
                <li>The slope-intercept form is $y = mx + c$ (where $m$ is the gradient and $c$ is the y-intercept).</li>
                <li>The general form is $ax + by + c = 0$.</li>
                <li>The point-slope form is $y - y_1 = m(x - x_1)$.</li>
            </ul>"""
    },
    {
        "id": "equation_circle", "title": "The Perfect Form of a Circle", "category": "Coordinate Geometry",
        "explanation": r"""<p>The equation of a circle describes its shape in the Cartesian plane. Key forms include:</p>
            <ul class="explanation-list">
                <li>The standard form is $(x-h)^2 + (y-k)^2 = r^2$, where the center is $(h,k)$ and the radius is $r$.</li>
                <li>The general form is $x^2 + y^2 + 2gx + 2fy + c = 0$.</li>
            </ul>"""
    },
    # Category: Graphs & Transformations
    {
        "id": "translating_graphs", "title": "Shifting Shapes: Translating Graphs", "category": "Graphs & Transformations",
        "explanation": r"""<p>Translating a graph means moving it without changing its shape or orientation. For a function $y=f(x)$:</p>
            <ul class="explanation-list">
                <li>The transformation $y = f(x) + a$ translates the graph vertically by $a$ units upwards.</li>
                <li>The transformation $y = f(x) - a$ translates the graph vertically by $a$ units downwards.</li>
                <li>The transformation $y = f(x-a)$ translates the graph horizontally by $a$ units to the right.</li>
                <li>The transformation $y = f(x+a)$ translates the graph horizontally by $a$ units to the left.</li>
            </ul>"""
    },
    # Category: Exponentials & Logarithms
    {
        "id": "exponential_functions", "title": "The Power of Exponential Functions", "category": "Exponentials & Logarithms",
        "explanation": r"""<p>Exponential functions are those where the variable appears in the exponent, for example, a function of the form $f(x) = a^x$.</p>
            <ul class="explanation-list">
                <li>These functions are characterized by rapid growth (if $a > 1$) or decay (if $0 < a < 1$).</li>
                <li>A fundamental exponential function in calculus is the natural exponential function, written as $f(x) = e^x$, where $e \approx 2.71828$.</li>
            </ul>"""
    },
    {
        "id": "laws_logarithms", "title": "Unlocking Logarithmic Laws", "category": "Exponentials & Logarithms",
        "explanation": r"""<p>Logarithms are the inverse operation of exponentiation. Key laws for manipulating logarithmic expressions include:</p>
            <ul class="explanation-list">
                <li>The Product Rule states $\log_b(MN) = \log_b M + \log_b N$</li>
                <li>The Quotient Rule states $\log_b(M/N) = \log_b M - \log_b N$</li>
                <li>The Power Rule states $\log_b(M^p) = p \log_b M$</li>
                <li>The Change of Base formula is $\log_b A = \frac{\log_c A}{\log_c B}$</li>
            </ul>"""
    },
    # Category: Binomial Expansion
    {
        "id": "binomial_expansion", "title": "Expanding Binomials", "category": "Binomial Expansion",
        "explanation": r"""<p>The binomial expansion provides a formula to expand expressions of the form $(a+b)^n$ for a positive integer $n$.</p>
            <p>The formula is given by $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$.</p>
            <ul class="explanation-list">
                <li>In this formula, the binomial coefficients are $\binom{n}{k} = \frac{n!}{k!(n-k)!}$, which can also be found using Pascal's Triangle.</li>
            </ul>"""
    },
    # Category: Sequences & Series
    {
        "id": "arithmetic_sequences", "title": "The Order of Arithmetic Sequences", "category": "Sequences & Series",
        "explanation": r"""<p>An arithmetic sequence is one where the difference between consecutive terms is constant. This constant difference is called the common difference, denoted by $d$.</p>
            <ul class="explanation-list">
                <li>The $n$-th term, $u_n$, can be found using the formula $u_n = a + (n-1)d$, where $a$ is the first term.</li>
                <li>The sum of the first $n$ terms of an arithmetic series is given by $S_n = \frac{n}{2}(2a + (n-1)d)$.</li>
            </ul>"""
    },
    {
        "id": "sum_to_infinity_geometric", "title": "Infinite Sums: Geometric Series", "category": "Sequences & Series",
        "explanation": r"""<p>A geometric series has a sum to infinity if its common ratio $r$ satisfies the condition $|r| < 1$.</p>
            <ul class="explanation-list">
                <li>The sum to infinity is calculated using the formula $S_\infty = \frac{a}{1-r}$, where $a$ is the first term.</li>
            </ul>"""
    },
    # Category: Trigonometry
    {
        "id": "cosine_rule", "title": "The Law of Cosines (Cosine Rule)", "category": "Trigonometry",
        "explanation": r"""<p>The Cosine Rule relates the lengths of the sides of any triangle to the cosine of one of its angles. For any triangle ABC, the rules are:</p>
            <ul class="explanation-list">
                <li>$a^2 = b^2 + c^2 - 2bc \cos A$</li>
                <li>$b^2 = a^2 + c^2 - 2ac \cos B$</li>
                <li>$c^2 = a^2 + b^2 - 2ab \cos C$</li>
                <li>This rule can be rearranged to find an angle if the lengths of all three sides are known.</li>
            </ul>"""
    },
    {
        "id": "radian_measure", "title": "Measuring Angles in Radians", "category": "Trigonometry",
        "explanation": r"""<p>Radian measure is an alternative unit for measuring angles, particularly useful in calculus and higher mathematics.</p>
            <ul class="explanation-list">
                <li>The relationship with degrees is $2\pi$ radians $= 360^\circ$, which simplifies to $\pi$ radians $= 180^\circ$.</li>
                <li>The arc length of a circle segment is found by $s = r\theta$ (where $\theta$ is the angle in radians).</li>
                <li>The area of a sector of a circle is calculated as $A = \frac{1}{2}r^2\theta$ (where $\theta$ is in radians).</li>
            </ul>"""
    },
    # Category: Differentiation
    {
        "id": "differentiating_xn", "title": "The Power Rule of Differentiation", "category": "Differentiation",
        "explanation": r"""<p>The Power Rule is a fundamental rule for finding derivatives of functions of the form $f(x) = x^n$.</p>
            <ul class="explanation-list">
                <li>The rule states that if $f(x) = x^n$, then its derivative is $f'(x) = nx^{n-1}$.</li>
                <li>This rule applies for any real number $n$.</li>
            </ul>"""
    },
    {
        "id": "stationary_points", "title": "Finding Stationary Points", "category": "Differentiation",
        "explanation": r"""<p>Stationary points on a curve are points where the gradient is zero, meaning $f'(x)=0$.</p>
            <ul class="explanation-list">
                <li>These points can be classified as local maximums, local minimums, or points of inflection.</li>
                <li>Classification is typically done using the first derivative test (checking the sign change of $f'(x)$ around the point) or the second derivative test (checking the sign of $f''(x)$ at the point).</li>
            </ul>"""
    },
    # Category: Integration
    {
        "id": "definite_integrals", "title": "The Essence of Definite Integrals", "category": "Integration",
        "explanation": r"""<p>A definite integral calculates the net area between a curve $f(x)$ and the x-axis over a specific interval, from $x=a$ to $x=b$.</p>
            <ul class="explanation-list">
                <li>It is denoted as $\int_a^b f(x) dx$.</li>
                <li>The value is found by calculating $F(b) - F(a)$, where $F(x)$ is the antiderivative (or indefinite integral) of $f(x)$.</li>
            </ul>"""
    },
    {
        "id": "area_under_curves", "title": "Calculating Area Under Curves", "category": "Integration",
        "explanation": r"""<p>Definite integrals are a primary tool for finding the exact area bounded by a curve, the x-axis, and two vertical lines (the limits of integration).</p>
            <ul class="explanation-list">
                <li>If the function $f(x)$ is non-negative ($f(x) \ge 0$) on the interval $[a,b]$, the area is directly given by the integral: Area $= \int_a^b f(x) dx$.</li>
                <li>If $f(x)$ is negative ($f(x) < 0$) on $[a,b]$, the integral will yield a negative value. The actual area is the absolute value of this integral: Area $= |\int_a^b f(x) dx|$.</li>
            </ul>"""
    }
]

# --- Initialize Session State ---
if 'current_topic_index' not in st.session_state:
    st.session_state.current_topic_index = 0
if 'max_unlocked_index' not in st.session_state:
    st.session_state.max_unlocked_index = 0
if 'topics_status' not in st.session_state:
    st.session_state.topics_status = [{'unlocked': (i == 0)} for i in range(len(topics_data))]
if 'quest_complete' not in st.session_state:
    st.session_state.quest_complete = False

# --- Helper Functions ---
def get_topic_title_for_navigator(title):
    prefixes_to_remove = ["The Scroll of ", "The Art of ", "The Essence of ", "The Secret of "]
    for prefix in prefixes_to_remove:
        if title.startswith(prefix):
            return title[len(prefix):]
    return title

# --- UI Rendering ---
st.set_page_config(page_title="Math Explorer's Compendium", layout="wide")

# Inject custom CSS for the UI Makeover - BRIGHT THEME
st.markdown(r"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&family=Inter:wght@400;600&family=IM+Fell+English+SC&display=swap');

    :root {
        /* Bright Theme Palette */
        --primary-bg: #FAF0E6; /* Linen - Main background */
        --secondary-bg: #FDF5E6; /* Old Lace - Slightly off-white for elements */
        --content-area-bg: #FFF8DC; /* Cornsilk - Parchment-like for content */
        --text-color-dark: #5D4037; /* Dark Brown - Primary text */
        --text-color-medium: #8B4513; /* SaddleBrown - Secondary text, headers */
        --accent-color: #D2691E; /* Chocolate - Accent, buttons, links */
        --accent-hover: #A0522D; /* Sienna - Accent hover */
        --border-color: #D2B48C; /* Tan - Borders */
        --button-text: #FFFFFF; /* White text on accent buttons */
        --button-hover-brightness: 1.1;
    }

    /* Apply bright theme to the main body */
    body {
        background-color: var(--primary-bg);
        color: var(--text-color-dark);
    }
    /* Ensure Streamlit's main content area also gets the bright background */
    .main .block-container {
        background-color: var(--primary-bg);
        color: var(--text-color-dark);
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Header styles - Streamlit's default header is harder to override directly without affecting sidebar too much.
       We will style our custom markdown headers instead. */

    /* Main title and subtitle */
    .title-main {
        font-family: 'MedievalSharp', cursive;
        color: var(--text-color-medium); /* Darker text for title on light bg */
        text-align: center;
        font-size: 3em; /* Adjusted size */
        margin-bottom: 0.2em;
    }
    .subtitle-main {
        font-family: 'IM Fell English SC', serif;
        color: var(--text-color-medium); /* Darker text for subtitle on light bg */
        text-align: center;
        font-size: 1.5em; /* Adjusted size */
        margin-bottom: 2rem;
    }

    /* Progress text styling */
    .progress-text-streamlit {
        text-align: center;
        font-family: 'IM Fell English SC', serif;
        color: var(--text-color-medium);
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }

    /* Topic title styling */
    .topic-title-streamlit {
        text-align: center;
        font-family: 'MedievalSharp', cursive;
        color: var(--accent-color); /* Accent color for topic titles */
        font-size: 2.5em; /* Adjusted size */
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    /* Explanation container - Parchment style */
    .explanation-container-streamlit {
        background-color: var(--content-area-bg);
        border: 2px solid var(--border-color);
        border-radius: 15px;
        padding: 25px;
        color: var(--text-color-dark); /* Ensure text inside is dark */
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* Softer shadow for light theme */
        margin-bottom: 1.5rem;
    }
    .explanation-container-streamlit p {
        margin-bottom: 0.8rem;
        line-height: 1.6;
    }
    .explanation-container-streamlit ul.explanation-list {
        list-style-type: disc;
        margin-left: 25px;
        padding-left: 0;
    }
    .explanation-container-streamlit ul.explanation-list li {
        margin-bottom: 0.6rem;
    }
    .explanation-container-streamlit strong {
        color: var(--accent-color);
    }

    /* Streamlit button styling */
    div.stButton > button {
        background-color: var(--accent-color);
        color: var(--button-text);
        border: 2px solid var(--accent-color);
        border-radius: 8px; /* Simplified radius */
        padding: 10px 20px;
        font-family: 'IM Fell English SC', serif;
        font-size: 1.1em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }
    div.stButton > button:hover {
        background-color: var(--accent-hover);
        border-color: var(--accent-hover);
        color: var(--button-text);
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    div.stButton > button:disabled {
        background-color: #C0C0C0; /* Silver for disabled */
        border-color: #A9A9A9;
        color: #696969;
        cursor: not-allowed;
        box-shadow: none;
    }

    /* Streamlit selectbox styling */
    div[data-baseweb="select"] > div {
        background-color: var(--secondary-bg);
        border: 2px solid var(--border-color);
        border-radius: 8px; /* Simplified radius */
        font-family: 'IM Fell English SC', serif;
        color: var(--text-color-dark);
    }
    div[data-baseweb="select"] svg { /* Dropdown arrow */
        color: var(--accent-color);
    }
    
    /* Horizontal rule style */
    hr {
        border-top: 2px solid var(--border-color);
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* Completion message styling */
    .completion-container-streamlit {
        background-color: var(--content-area-bg);
        border: 3px solid var(--accent-color);
        padding: 2.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 0 20px rgba(210, 105, 30, 0.3); /* Shadow based on accent */
    }
    .completion-title-streamlit {
        font-family: 'MedievalSharp', cursive;
        color: var(--accent-color);
        font-size: 3rem;
        text-shadow: 1px 1px 0px #FFF, 2px 2px 0px var(--border-color);
    }
    .completion-text-streamlit {
        color: var(--text-color-medium);
        font-size: 1.2rem;
        font-family: 'IM Fell English SC', serif;
    }

</style>
""", unsafe_allow_html=True)

# Header
# st.markdown("<h1 class='title-main'>Math Explorer's Compendium</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subtitle-main'>Unearth the Scrolls of Mathematical Wisdom!</p>", unsafe_allow_html=True)
# Using st.title and st.caption for more Streamlit-native feel, then styling them if needed
st.markdown("<div style='text-align: center;'><h1 class='title-main'>Math Explorer's Compendium</h1><p class='subtitle-main'>Unearth the Scrolls of Mathematical Wisdom!</p></div>", unsafe_allow_html=True)
st.markdown("---")


# --- Main Application Logic ---
if st.session_state.quest_complete:
    st.balloons()
    st.markdown("<div class='completion-container-streamlit'>", unsafe_allow_html=True)
    st.markdown("<h2 class='completion-title-streamlit'>Treasure Unlocked!</h2>", unsafe_allow_html=True)
    st.markdown("<p class='completion-text-streamlit'>Thou hast proven a keen explorer of knowledge! All scrolls are revealed.</p>", unsafe_allow_html=True)
    st.markdown("<p class='completion-text-streamlit'>May your wisdom shine brightly!</p>", unsafe_allow_html=True)
    
    if st.button("Embark on a New Quest", key="restart_complete", use_container_width=True):
        st.session_state.current_topic_index = 0
        st.session_state.max_unlocked_index = 0
        st.session_state.topics_status = [{'unlocked': (i == 0)} for i in range(len(topics_data))]
        st.session_state.quest_complete = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Progress Area
    progress_text = f"Scroll {st.session_state.current_topic_index + 1} of {len(topics_data)} Unfurled | Path Explored: {min(st.session_state.max_unlocked_index + 1, len(topics_data))} scrolls"
    st.markdown(f"<p class='progress-text-streamlit'>{progress_text}</p>", unsafe_allow_html=True)

    st.markdown("---")

    # Explorer Area
    current_topic = topics_data[st.session_state.current_topic_index]
    st.markdown(f"<h2 class='topic-title-streamlit'>{current_topic['title']}</h2>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='explanation-container-streamlit'>{current_topic['explanation']}</div>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Navigation Buttons
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        if st.button("📜 Previous Scroll", key="prev_button", disabled=st.session_state.current_topic_index == 0, use_container_width=True):
            st.session_state.current_topic_index -= 1
            st.rerun()

    with col3:
        is_last_topic = st.session_state.current_topic_index == len(topics_data) - 1
        all_unlocked = st.session_state.max_unlocked_index == len(topics_data) - 1
        
        next_button_text = "🎉 Quest Complete!" if is_last_topic and all_unlocked else "Reveal Next Scroll 📜"
        
        if st.button(next_button_text, key="next_button", disabled=is_last_topic and not all_unlocked, use_container_width=True):
            if is_last_topic and all_unlocked:
                st.session_state.quest_complete = True
            else:
                st.session_state.current_topic_index += 1
                if st.session_state.current_topic_index > st.session_state.max_unlocked_index:
                    st.session_state.max_unlocked_index = st.session_state.current_topic_index
                st.session_state.topics_status[st.session_state.current_topic_index]['unlocked'] = True
            st.rerun()
            
    # Restart button (always available at the bottom if not complete)
    st.markdown("---")
    if st.button("🔄 Restart Expedition", key="restart_main", use_container_width=True):
        st.session_state.current_topic_index = 0
        st.session_state.max_unlocked_index = 0
        st.session_state.topics_status = [{'unlocked': (i == 0)} for i in range(len(topics_data))]
        st.session_state.quest_complete = False
        st.rerun()
