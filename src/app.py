import streamlit as st

# --- Topics Data ---
topics_data = [
    # Category: Algebra & Polynomials
    {
        "id": "index_laws", "title": "The Scroll of Index Laws", "category": "Algebra & Polynomials",
        "explanation": """<p>Index laws (or exponent laws) are rules for simplifying expressions with powers. Here are the key laws:</p>
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
        "explanation": """<p>Factorising is the reverse of expanding brackets. It involves writing an expression as a product of its factors. Some common forms include:</p>
            <ul class="explanation-list">
                <li>Common Factor: $ax + ay = a(x+y)$</li>
                <li>Difference of Two Squares: $a^2 - b^2 = (a-b)(a+b)$</li>
                <li>Trinomials (e.g., $x^2 + bx + c$): Look for two numbers that multiply to $c$ and add to $b$.</li>
                <li>Grouping: For expressions with four terms, group pairs of terms.</li>
            </ul>"""
    },
    {
        "id": "factor_theorem", "title": "The Factor Theorem's Secret", "category": "Algebra & Polynomials",
        "explanation": """<p>The Factor Theorem is a powerful tool for factorising polynomials.</p>
            <ul class="explanation-list">
                <li>It states that if $P(x)$ is a polynomial, then $(x-a)$ is a factor of $P(x)$ if and only if $P(a) = 0$.</li>
                <li>This helps find linear factors of higher-degree polynomials.</li>
            </ul>"""
    },
    # Category: Proof
    {
        "id": "math_proof", "title": "The Essence of Mathematical Proof", "category": "Proof",
        "explanation": """<p>A mathematical proof is a rigorous argument that demonstrates the truth of a mathematical statement.</p>
            <ul class="explanation-list">
                <li>It relies on axioms, definitions, and previously proven theorems.</li>
                <li>Common methods include: Proof by Deduction, Proof by Contradiction, Proof by Induction, and Disproof by Counterexample.</li>
            </ul>"""
    },
    # Category: Quadratics
    {
        "id": "solving_quadratics", "title": "Solving Quadratic Equations", "category": "Quadratics",
        "explanation": """<p>Solving quadratic equations means finding values of $x$ for equations typically in the form $ax^2 + bx + c = 0$. Methods include:</p>
            <ul class="explanation-list">
                <li>By factorisation (if possible).</li>
                <li>Using the quadratic formula, which is $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$</li>
                <li>By completing the square.</li>
            </ul>"""
    },
    {
        "id": "discriminant", "title": "The Revealing Discriminant", "category": "Quadratics",
        "explanation": """<p>The discriminant of a quadratic equation $ax^2+bx+c=0$ is given by the expression $\Delta = b^2-4ac$. The value of the discriminant reveals the nature of the roots:</p>
            <ul class="explanation-list">
                <li>If $\Delta > 0$, there are two distinct real roots.</li>
                <li>If $\Delta = 0$, there is one repeated real root (or two equal real roots).</li>
                <li>If $\Delta < 0$, there are no real roots (instead, there are two complex conjugate roots).</li>
            </ul>"""
    },
    # Category: Coordinate Geometry
    {
        "id": "equation_straight_line", "title": "The Path of Straight Lines", "category": "Coordinate Geometry",
        "explanation": """<p>The equation of a straight line describes its path in the Cartesian plane. Common forms are:</p>
            <ul class="explanation-list">
                <li>The slope-intercept form is $y = mx + c$ (where $m$ is the gradient and $c$ is the y-intercept).</li>
                <li>The general form is $ax + by + c = 0$.</li>
                <li>The point-slope form is $y - y_1 = m(x - x_1)$.</li>
            </ul>"""
    },
    {
        "id": "equation_circle", "title": "The Perfect Form of a Circle", "category": "Coordinate Geometry",
        "explanation": """<p>The equation of a circle describes its shape in the Cartesian plane. Key forms include:</p>
            <ul class="explanation-list">
                <li>The standard form is $(x-h)^2 + (y-k)^2 = r^2$, where the center is $(h,k)$ and the radius is $r$.</li>
                <li>The general form is $x^2 + y^2 + 2gx + 2fy + c = 0$.</li>
            </ul>"""
    },
    # Category: Graphs & Transformations
    {
        "id": "translating_graphs", "title": "Shifting Shapes: Translating Graphs", "category": "Graphs & Transformations",
        "explanation": """<p>Translating a graph means moving it without changing its shape or orientation. For a function $y=f(x)$:</p>
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
        "explanation": """<p>Exponential functions are those where the variable appears in the exponent, for example, a function of the form $f(x) = a^x$.</p>
            <ul class="explanation-list">
                <li>These functions are characterized by rapid growth (if $a > 1$) or decay (if $0 < a < 1$).</li>
                <li>A fundamental exponential function in calculus is the natural exponential function, written as $f(x) = e^x$, where $e \approx 2.71828$.</li>
            </ul>"""
    },
    {
        "id": "laws_logarithms", "title": "Unlocking Logarithmic Laws", "category": "Exponentials & Logarithms",
        "explanation": """<p>Logarithms are the inverse operation of exponentiation. Key laws for manipulating logarithmic expressions include:</p>
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
        "explanation": """<p>The binomial expansion provides a formula to expand expressions of the form $(a+b)^n$ for a positive integer $n$.</p>
            <p>The formula is given by $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$.</p>
            <ul class="explanation-list">
                <li>In this formula, the binomial coefficients are $\binom{n}{k} = \frac{n!}{k!(n-k)!}$, which can also be found using Pascal's Triangle.</li>
            </ul>"""
    },
    # Category: Sequences & Series
    {
        "id": "arithmetic_sequences", "title": "The Order of Arithmetic Sequences", "category": "Sequences & Series",
        "explanation": """<p>An arithmetic sequence is one where the difference between consecutive terms is constant. This constant difference is called the common difference, denoted by $d$.</p>
            <ul class="explanation-list">
                <li>The $n$-th term, $u_n$, can be found using the formula $u_n = a + (n-1)d$, where $a$ is the first term.</li>
                <li>The sum of the first $n$ terms of an arithmetic series is given by $S_n = \frac{n}{2}(2a + (n-1)d)$.</li>
            </ul>"""
    },
    {
        "id": "sum_to_infinity_geometric", "title": "Infinite Sums: Geometric Series", "category": "Sequences & Series",
        "explanation": """<p>A geometric series has a sum to infinity if its common ratio $r$ satisfies the condition $|r| < 1$.</p>
            <ul class="explanation-list">
                <li>The sum to infinity is calculated using the formula $S_\infty = \frac{a}{1-r}$, where $a$ is the first term.</li>
            </ul>"""
    },
    # Category: Trigonometry
    {
        "id": "cosine_rule", "title": "The Law of Cosines (Cosine Rule)", "category": "Trigonometry",
        "explanation": """<p>The Cosine Rule relates the lengths of the sides of any triangle to the cosine of one of its angles. For any triangle ABC, the rules are:</p>
            <ul class="explanation-list">
                <li>$a^2 = b^2 + c^2 - 2bc \cos A$</li>
                <li>$b^2 = a^2 + c^2 - 2ac \cos B$</li>
                <li>$c^2 = a^2 + b^2 - 2ab \cos C$</li>
                <li>This rule can be rearranged to find an angle if the lengths of all three sides are known.</li>
            </ul>"""
    },
    {
        "id": "radian_measure", "title": "Measuring Angles in Radians", "category": "Trigonometry",
        "explanation": """<p>Radian measure is an alternative unit for measuring angles, particularly useful in calculus and higher mathematics.</p>
            <ul class="explanation-list">
                <li>The relationship with degrees is $2\pi$ radians $= 360^\circ$, which simplifies to $\pi$ radians $= 180^\circ$.</li>
                <li>The arc length of a circle segment is found by $s = r\theta$ (where $\theta$ is the angle in radians).</li>
                <li>The area of a sector of a circle is calculated as $A = \frac{1}{2}r^2\theta$ (where $\theta$ is in radians).</li>
            </ul>"""
    },
    # Category: Differentiation
    {
        "id": "differentiating_xn", "title": "The Power Rule of Differentiation", "category": "Differentiation",
        "explanation": """<p>The Power Rule is a fundamental rule for finding derivatives of functions of the form $f(x) = x^n$.</p>
            <ul class="explanation-list">
                <li>The rule states that if $f(x) = x^n$, then its derivative is $f'(x) = nx^{n-1}$.</li>
                <li>This rule applies for any real number $n$.</li>
            </ul>"""
    },
    {
        "id": "stationary_points", "title": "Finding Stationary Points", "category": "Differentiation",
        "explanation": """<p>Stationary points on a curve are points where the gradient is zero, meaning $f'(x)=0$.</p>
            <ul class="explanation-list">
                <li>These points can be classified as local maximums, local minimums, or points of inflection.</li>
                <li>Classification is typically done using the first derivative test (checking the sign change of $f'(x)$ around the point) or the second derivative test (checking the sign of $f''(x)$ at the point).</li>
            </ul>"""
    },
    # Category: Integration
    {
        "id": "definite_integrals", "title": "The Essence of Definite Integrals", "category": "Integration",
        "explanation": """<p>A definite integral calculates the net area between a curve $f(x)$ and the x-axis over a specific interval, from $x=a$ to $x=b$.</p>
            <ul class="explanation-list">
                <li>It is denoted as $\int_a^b f(x) dx$.</li>
                <li>The value is found by calculating $F(b) - F(a)$, where $F(x)$ is the antiderivative (or indefinite integral) of $f(x)$.</li>
            </ul>"""
    },
    {
        "id": "area_under_curves", "title": "Calculating Area Under Curves", "category": "Integration",
        "explanation": """<p>Definite integrals are a primary tool for finding the exact area bounded by a curve, the x-axis, and two vertical lines (the limits of integration).</p>
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

# Header
st.markdown("<h1 style='text-align: center; color: #8B4513; font-family: MedievalSharp, cursive;'>Math Explorer's Compendium</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #A0522D; font-family: IM Fell English SC, serif; font-size: 1.2em;'>Unearth the Scrolls of Mathematical Wisdom!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Main Application Logic ---
if st.session_state.quest_complete:
    st.balloons()
    st.markdown("<div style='background-color: #FFF8DC; border: 3px solid #FFD700; padding: 2.5rem; border-radius: 10px; text-align: center; box-shadow: 0 0 20px rgba(255,215,0,0.5);'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: MedievalSharp, cursive; color: #DAA520; font-size: 3rem; text-shadow: 2px 2px 0px #FFF, 3px 3px 0px #B8860B;'>Treasure Unlocked!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8B4513; font-size: 1.2rem; font-family: IM Fell English SC, serif;'>Thou hast proven a keen explorer of knowledge! All scrolls are revealed.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8B4513; font-size: 1.2rem; font-family: IM Fell English SC, serif;'>May your wisdom shine brightly!</p>", unsafe_allow_html=True)
    
    if st.button("Embark on a New Quest", key="restart_complete"):
        st.session_state.current_topic_index = 0
        st.session_state.max_unlocked_index = 0
        st.session_state.topics_status = [{'unlocked': (i == 0)} for i in range(len(topics_data))]
        st.session_state.quest_complete = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Progress Area
    progress_text = f"Scroll {st.session_state.current_topic_index + 1} of {len(topics_data)} Unfurled | Path Explored: {min(st.session_state.max_unlocked_index + 1, len(topics_data))} scrolls"
    st.markdown(f"<p style='text-align: center; font-family: IM Fell English SC, serif; color: #603813; font-size: 1.1rem;'>{progress_text}</p>", unsafe_allow_html=True)

    unlocked_topic_titles = [
        get_topic_title_for_navigator(topics_data[i]['title'])
        for i, status in enumerate(st.session_state.topics_status) if status['unlocked']
    ]
    
    # Create a mapping from the display title to the original index
    title_to_index_map = {
        get_topic_title_for_navigator(topics_data[i]['title']): i
        for i, status in enumerate(st.session_state.topics_status) if status['unlocked']
    }

    current_selection_title = get_topic_title_for_navigator(topics_data[st.session_state.current_topic_index]['title'])

    selected_topic_title = st.selectbox(
        "Navigate Scrolls:",
        options=unlocked_topic_titles,
        index=unlocked_topic_titles.index(current_selection_title) if current_selection_title in unlocked_topic_titles else 0,
        key="topic_navigator"
    )
    
    if selected_topic_title:
        selected_index = title_to_index_map[selected_topic_title]
        if selected_index != st.session_state.current_topic_index:
            st.session_state.current_topic_index = selected_index
            # No rerun needed here, selectbox change will trigger it if value changes

    st.markdown("---")

    # Explorer Area
    current_topic = topics_data[st.session_state.current_topic_index]
    st.markdown(f"<h2 style='text-align: center; color: #8B4513; font-family: MedievalSharp, cursive; font-size: 2.5em;'>{current_topic['title']}</h2>", unsafe_allow_html=True)
    
    # Custom CSS for the explanation text to match the original style more closely
    st.markdown("""
    <style>
        .explanation-container {
            background-color: #FDF5E6; /* Creamy background */
            border: 2px solid #D2B48C; /* Tan border */
            border-radius: 10px;
            padding: 20px;
            font-family: 'Inter', sans-serif;
            color: #5D4037; /* Dark brown text */
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .explanation-container p {
            margin-bottom: 0.8rem;
            line-height: 1.6;
        }
        .explanation-container ul.explanation-list {
            list-style-type: disc; /* Or 'circle', 'square' */
            margin-left: 25px; /* Indent list */
            padding-left: 0;
        }
        .explanation-container ul.explanation-list li {
            margin-bottom: 0.6rem;
            color: #4E342E; /* Slightly darker list items */
        }
        .explanation-container strong {
            color: #A0522D; /* Sienna for emphasis */
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<div class='explanation-container'>{current_topic['explanation']}</div>", unsafe_allow_html=True)
    
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

# Add some styling for buttons to make them more thematic
st.markdown("""
<style>
    div.stButton > button {
        background-color: #DEB887; /* BurlyWood */
        color: #654321; /* Dark Brown */
        border: 2px solid #8B4513; /* SaddleBrown */
        border-radius: 20px 5px 20px 5px;
        padding: 10px 20px;
        font-family: 'IM Fell English SC', serif;
        font-size: 1.1em;
        font-weight: bold;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 3px 5px rgba(0,0,0,0.2), inset 0 -2px 0px rgba(0,0,0,0.2);
        text-shadow: 1px 1px 0px rgba(255,255,255,0.3);
    }
    div.stButton > button:hover {
        background-color: #CDAD00; /* Brighter Gold */
        color: #FFFFFF;
        transform: translateY(-2px);
        box-shadow: 0 5px 7px rgba(0,0,0,0.3), inset 0 -2px 0px rgba(0,0,0,0.1);
    }
    div.stButton > button:disabled {
        background-color: #A9A9A9; /* DarkGray - disabled */
        border-color: #696969;
        color: #E0E0E0;
        cursor: not-allowed;
        transform: translateY(0);
        box-shadow: inset 0 2px 2px rgba(0,0,0,0.1);
        text-shadow: none;
    }
    /* Style for selectbox */
    div[data-baseweb="select"] > div {
        background-color: #FDF5E6;
        border: 2px solid #B8860B;
        border-radius: 3px;
        font-family: 'IM Fell English SC', serif;
        color: #5D4037;
    }
    /* Style for selectbox dropdown arrow */
    div[data-baseweb="select"] svg {
        color: #8B4513;
    }
</style>
""", unsafe_allow_html=True)

# Add Google Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=MedievalSharp&family=Inter:wght@400;600&family=IM+Fell+English+SC&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Log current state for debugging (optional)
# st.sidebar.write("Current Index:", st.session_state.current_topic_index)
# st.sidebar.write("Max Unlocked Index:", st.session_state.max_unlocked_index)
# st.sidebar.write("Quest Complete:", st.session_state.quest_complete)
# st.sidebar.json(st.session_state.topics_status)
