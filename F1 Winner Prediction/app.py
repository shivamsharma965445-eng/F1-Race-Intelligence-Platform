import streamlit as st
import pandas as pd
import pickle
import base64
import plotly.graph_objects as go

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="F1 Race Intelligence Platform", page_icon="🏎️", layout="wide"
)


# -----------------------------
# Background Video
# -----------------------------
def set_video_background(video_file):
    with open(video_file, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background: transparent;
        }}

        video {{
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100%;
            min-height: 100%;
            object-fit: cover;
            z-index: -1;
        }}

        </style>

        <video autoplay muted loop>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Play Sound
# -----------------------------
def play_sound(sound_file):

    with open(sound_file, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode()

    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Video
# -----------------------------
set_video_background(r"F1 Intro.mp4")

# -----------------------------
# Title
# -----------------------------
col1, col2 = st.columns([1, 8], gap="small")
with col1:
    st.markdown("<div style='padding-top: 14px;'></div>", unsafe_allow_html=True)
    st.image(
        r"pngtree-a-sleek-red-formula-1-race-car-with-low-profile-design-png-image_15491155.png",
        width=120,
    )
with col2:
    st.markdown(
        "<h1 style='margin:0; color:#ffffff; line-height:1.1;'>Formula 1 Race Intelligence Platform</h1>",
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown(
    """
    <style>
    .stApp {
        background: rgba(0, 0, 0, 0.22);
        color: #ffffff;
        backdrop-filter: blur(4px);
    }
    [data-testid="stSidebar"] {
        background: rgba(0, 0, 0, 0.45);
        color: #ffffff;
        padding: 1rem;
        border-right: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(6px);
    }
    .stSidebar .stButton>button, .stButton>button {
        background: #e10600;
        color: #ffffff;
        border-radius: 14px;
        border: 1px solid #c10000;
        padding: 0.75rem 1rem;
        min-width: 12rem;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(225,16,0,0.35);
    }
    .stSidebar .stButton>button:hover {
        background: #c10000;
    }
    .stSidebar .css-1d391kg {
        color: #ffffff;
    }
    .stTextInput>div>input, .stTextInput>div>textarea {
        background: rgba(20, 20, 20, 0.85);
        color: #ffffff;
        border: 1px solid #e10600;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state.page = "HOME"

st.sidebar.image(
    r"New_era_F1_logo.png",
    width=260,
)
st.sidebar.markdown(
    '<div style="font-size:18px; font-weight:700; letter-spacing:0.02em; text-transform:uppercase; color:#ffffff; margin-top:1rem;">NAVIGATION</div>',
    unsafe_allow_html=True,
)

menu_items = [
    "HOME",
    "WINNER PREDICTION",
    "PODIUM PREDICTION",
    "TOP 10 PREDICTION",
    "FINISHING POSITION PREDICTION",
    "DRIVER PERFORMANCE ANALYSIS",
    "DRIVER COMPARISON",
]

for item in menu_items:
    if st.sidebar.button(item, key=f"nav_{item}"):
        st.session_state.page = item

page = st.session_state.page

# =====================================================
# HOME
# =====================================================

if page == "HOME":

    st.header("🏁 WELCOME TO F1 RACE INTELLIGENCE")

    st.markdown(
        """
        <div style="background: rgba(255,255,255,0.06); padding: 28px; border-radius: 24px; border: 1px solid rgba(255,255,255,0.14); box-shadow: 0 18px 40px rgba(0,0,0,0.35); font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">
            <h2 style="margin-bottom: 16px; color: #ffffff; letter-spacing: 1px; font-weight: 700;">F1 Race Intelligence, reimagined.</h2>
            <p style="margin-bottom: 18px; color: #d8d8d8; font-size: 16px; line-height: 1.8;">A premium platform built to transform race data into sleek, actionable insights for every F1 weekend.</p>
            <ul style="margin-left: 22px; color: #f2f2f2; line-height: 2; list-style: none; padding: 0;">
                <li style="margin-bottom: 10px;">✨ <strong>Predict race winners</strong> with fast, data-driven intelligence.</li>
                <li style="margin-bottom: 10px;">🥉 <strong>Forecast podium finishes</strong> with real-time model confidence.</li>
                <li style="margin-bottom: 10px;">🔟 <strong>Estimate Top 10 outcomes</strong> using modern machine learning insights.</li>
                <li style="margin-bottom: 10px;">📊 <strong>Compare drivers and analyze performance</strong> with dynamic charts and stats.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="margin-top: 20px; padding: 22px; border-radius: 20px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;">
            <h4 style="margin-bottom: 12px; color: #ffffff; letter-spacing: 0.5px;">Start here</h4>
            <p style="margin: 0; color: #c8c8c8; font-size: 15px;">Use the sleek left-side navigation to jump into prediction modules, driver analysis, and comparison tools.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "🚀 Choose a module from the sidebar to begin your F1 intelligence journey."
    )

# =====================================================
# WINNER PREDICTION
# =====================================================

elif page == "WINNER PREDICTION":

    st.header("🏆 Race Winner Prediction")

    # -----------------------------
    # Load Model
    # -----------------------------
    @st.cache_resource
    def load_model():
        with open(r"rwp.pkl", "rb") as f:
            return pickle.load(f)

    winner_model = load_model()

    # -----------------------------
    # Load Dataset
    # -----------------------------
    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    # -----------------------------
    # Driver List
    # -----------------------------
    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    col1, col2 = st.columns(2)

    with col1:

        selected_driver = st.selectbox("🏎 Driver", drivers["driver_name"])

    driver_id = drivers.loc[drivers["driver_name"] == selected_driver, "driverId"].iloc[
        0
    ]

    # -----------------------------
    # Team
    # -----------------------------
    teams = df[df["driverId"] == driver_id][
        ["constructorId", "name_team"]
    ].drop_duplicates()

    with col2:

        selected_team = st.selectbox("🏁 Team", teams["name_team"])

    constructor_id = teams.loc[
        teams["name_team"] == selected_team, "constructorId"
    ].iloc[0]

    st.divider()

    # -----------------------------
    # Race
    # -----------------------------
    circuits = (
        df[["circuitId", "name_race", "round"]]
        .drop_duplicates()
        .sort_values("name_race")
    )

    selected_race = st.selectbox("🏟 Grand Prix", circuits["name_race"])

    race_row = circuits[circuits["name_race"] == selected_race].iloc[0]

    circuit_id = race_row["circuitId"]

    round_number = race_row["round"]

    grid = st.slider("🏁 Grid Position", 1, 20, 1)

    st.divider()

    predict = st.button("PREDICT WINNER", use_container_width=True)
    if predict:

        input_data = pd.DataFrame(
            {
                "driverId": [driver_id],
                "constructorId": [constructor_id],
                "grid": [grid],
                "round": [round_number],
                "circuitId": [circuit_id],
            }
        )

        # -----------------------------
        # Loading Animation
        # -----------------------------
        progress = st.progress(0)

        status = st.empty()

        status.text("Loading race history...")

        import time

        for i in range(30):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Analyzing telemetry...")

        for i in range(30, 70):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Running AI Prediction Model...")

        for i in range(70, 100):
            progress.progress(i + 1)
            time.sleep(0.01)

        progress.empty()
        status.empty()

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = winner_model.predict(input_data)[0]

        try:
            probability = winner_model.predict_proba(input_data)[0][1]
        except:
            probability = None

        st.divider()

        st.subheader("🏁 Prediction Result")

        # -----------------------------
        # WIN
        # -----------------------------
        if prediction == 1:

            st.success(f"🏆 **{selected_driver}** is predicted to WIN!")

            if selected_driver == "Max Verstappen":

                play_sound(r"tu-tu-tu-du-max-verstappen.mp3")

            elif selected_driver == "Carlos Sainz":

                play_sound(r"smooth_operator.mp3")

            else:

                play_sound(r"F1 Car PassingBy.mp3")

        # -----------------------------
        # LOSS
        # -----------------------------
        else:

            st.error(f"❌ **{selected_driver}** is NOT predicted to win.")

        # -----------------------------
        # F1 Probability Gauge
        # -----------------------------
        if probability is not None:

            percent = probability * 100

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=percent,
                    number={"suffix": "%", "font": {"size": 42}},
                    title={"text": "Winning Probability", "font": {"size": 22}},
                    gauge={
                        "shape": "angular",
                        "axis": {"range": [0, 100], "tickwidth": 2},
                        "bar": {"color": "red", "thickness": 0.35},
                        "steps": [
                            {"range": [0, 40], "color": "#4A0000"},
                            {"range": [40, 70], "color": "#8B0000"},
                            {"range": [70, 100], "color": "#E10600"},
                        ],
                        "threshold": {
                            "line": {"color": "white", "width": 5},
                            "thickness": 0.8,
                            "value": percent,
                        },
                    },
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(l=40, r=40, t=60, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
            )

            st.plotly_chart(fig, use_container_width=True)

            if percent >= 90:

                st.success("🔥 Race Favourite")

            elif percent >= 75:

                st.success("🟢 High Winning Chance")

            elif percent >= 55:

                st.warning("🟡 Moderate Winning Chance")

            elif percent >= 35:

                st.warning("🟠 Difficult Race")

            else:

                st.error("🔴 Very Low Winning Chance")

        st.divider()

        # -----------------------------
        # Input Summary
        # -----------------------------
        with st.expander("Model Inputs"):

            st.dataframe(input_data, use_container_width=True)

# =====================================================
# PODIUM PREDICTION
# =====================================================

elif page == "PODIUM PREDICTION":

    st.header("🥉 Podium Prediction")

    @st.cache_resource
    def load_podium_model():
        with open(r"pfinish.pkl", "rb") as f:
            return pickle.load(f)

    podium_model = load_podium_model()

    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    col1, col2 = st.columns(2)

    with col1:

        selected_driver = st.selectbox(
            "🏎 Driver", drivers["driver_name"], key="podium_driver"
        )

    driver_id = drivers.loc[drivers["driver_name"] == selected_driver, "driverId"].iloc[
        0
    ]

    teams = df[df["driverId"] == driver_id][
        ["constructorId", "name_team"]
    ].drop_duplicates()

    with col2:

        selected_team = st.selectbox("🏁 Team", teams["name_team"], key="podium_team")

    constructor_id = teams.loc[
        teams["name_team"] == selected_team, "constructorId"
    ].iloc[0]

    st.divider()

    circuits = (
        df[["circuitId", "name_race", "round"]]
        .drop_duplicates()
        .sort_values("name_race")
    )

    selected_race = st.selectbox(
        "🏟 Grand Prix", circuits["name_race"], key="podium_race"
    )

    race_row = circuits[circuits["name_race"] == selected_race].iloc[0]

    circuit_id = race_row["circuitId"]

    round_number = race_row["round"]

    grid = st.slider("🏁 Grid Position", 1, 20, 1, key="podium_grid")

    predict = st.button("PREDICT PODIUM", use_container_width=True, key="podium_button")

    if predict:

        input_data = pd.DataFrame(
            {
                "driverId": [driver_id],
                "constructorId": [constructor_id],
                "grid": [grid],
                "round": [round_number],
                "circuitId": [circuit_id],
            }
        )

        progress = st.progress(0)

        status = st.empty()

        import time

        status.text("Loading Race Data...")

        for i in range(35):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Running AI Model...")

        for i in range(35, 70):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Calculating Podium Probability...")
        for i in range(70, 100):
            progress.progress(i + 1)
            time.sleep(0.01)

        progress.empty()
        status.empty()

        prediction = podium_model.predict(input_data)[0]

        try:
            probability = podium_model.predict_proba(input_data)[0][1]
        except:
            probability = None

        st.divider()

        st.subheader("🥉 Prediction Result")

        if prediction == 1:

            st.success(f"🥉 {selected_driver} is predicted to FINISH ON THE PODIUM!")

            if selected_driver == "Max Verstappen":

                play_sound(r"tu-tu-tu-du-max-verstappen.mp3")

            elif selected_driver == "Carlos Sainz":

                play_sound(r"smooth_operator.mp3")

            else:

                play_sound(r"F1 Car PassingBy.mp3")

        else:

            st.error(f"❌ {selected_driver} is NOT predicted to finish on the podium.")

        if probability is not None:

            percent = probability * 100

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=percent,
                    number={"suffix": "%", "font": {"size": 42}},
                    title={"text": "Podium Probability", "font": {"size": 22}},
                    gauge={
                        "shape": "angular",
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "red", "thickness": 0.35},
                        "steps": [
                            {"range": [0, 40], "color": "#4A0000"},
                            {"range": [40, 70], "color": "#8B0000"},
                            {"range": [70, 100], "color": "#E10600"},
                        ],
                        "threshold": {
                            "line": {"color": "white", "width": 5},
                            "thickness": 0.8,
                            "value": percent,
                        },
                    },
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(l=40, r=40, t=60, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
            )

            st.plotly_chart(fig, use_container_width=True)

            if percent >= 90:

                st.success("🔥 Extremely High Podium Chance")

            elif percent >= 75:

                st.success("🟢 High Podium Chance")

            elif percent >= 55:

                st.warning("🟡 Moderate Podium Chance")

            elif percent >= 35:

                st.warning("🟠 Difficult Podium")

            else:

                st.error("🔴 Very Low Podium Chance")

        st.divider()

        with st.expander("Model Inputs"):

            st.dataframe(input_data, use_container_width=True)
# =====================================================
# TOP 10 PREDICTION
# =====================================================

elif page == "TOP 10 PREDICTION":

    st.header("🔟 Top 10 Prediction")

    @st.cache_resource
    def load_top10_model():
        with open(r"top10finish.pkl", "rb") as f:
            return pickle.load(f)

    top10_model = load_top10_model()

    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    col1, col2 = st.columns(2)

    with col1:

        selected_driver = st.selectbox(
            "🏎 Driver", drivers["driver_name"], key="top10_driver"
        )

    driver_id = drivers.loc[drivers["driver_name"] == selected_driver, "driverId"].iloc[
        0
    ]

    teams = df[df["driverId"] == driver_id][
        ["constructorId", "name_team"]
    ].drop_duplicates()

    with col2:

        selected_team = st.selectbox("🏁 Team", teams["name_team"], key="top10_team")

    constructor_id = teams.loc[
        teams["name_team"] == selected_team, "constructorId"
    ].iloc[0]

    st.divider()

    circuits = (
        df[["circuitId", "name_race", "round"]]
        .drop_duplicates()
        .sort_values("name_race")
    )

    selected_race = st.selectbox(
        "🏟 Grand Prix", circuits["name_race"], key="top10_race"
    )

    race_row = circuits[circuits["name_race"] == selected_race].iloc[0]

    circuit_id = race_row["circuitId"]

    round_number = race_row["round"]

    grid = st.slider("� Grid Position", 1, 20, 1, key="top10_grid")

    predict = st.button("PREDICT TOP 10", use_container_width=True, key="top10_button")

    if predict:

        input_data = pd.DataFrame(
            {
                "driverId": [driver_id],
                "constructorId": [constructor_id],
                "grid": [grid],
                "round": [round_number],
                "circuitId": [circuit_id],
            }
        )

        progress = st.progress(0)

        status = st.empty()

        import time

        status.text("Loading Race Data...")

        for i in range(35):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Running AI Model...")

        for i in range(35, 70):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Calculating Top 10 Probability...")

        for i in range(70, 100):
            progress.progress(i + 1)
            time.sleep(0.01)

        progress.empty()
        status.empty()

        prediction = top10_model.predict(input_data)[0]

        try:
            probability = top10_model.predict_proba(input_data)[0][1]
        except:
            probability = None

        st.divider()

        st.subheader("🔟 Prediction Result")

        if prediction == 1:

            st.success(f"🔟 {selected_driver} is predicted to FINISH IN THE TOP 10!")

            if selected_driver == "Max Verstappen":

                play_sound(r"tu-tu-tu-du-max-verstappen.mp3")

            elif selected_driver == "Carlos Sainz":

                play_sound(r"smooth_operator.mp3")

            else:

                play_sound(r"F1 Car PassingBy.mp3")

        else:

            st.error(f"❌ {selected_driver} is NOT predicted to finish in the Top 10.")

        if probability is not None:

            percent = probability * 100

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=percent,
                    number={"suffix": "%", "font": {"size": 42}},
                    title={"text": "Top 10 Probability", "font": {"size": 22}},
                    gauge={
                        "shape": "angular",
                        "axis": {"range": [0, 100]},
                        "bar": {"color": "red", "thickness": 0.35},
                        "steps": [
                            {"range": [0, 40], "color": "#4A0000"},
                            {"range": [40, 70], "color": "#8B0000"},
                            {"range": [70, 100], "color": "#E10600"},
                        ],
                        "threshold": {
                            "line": {"color": "white", "width": 5},
                            "thickness": 0.8,
                            "value": percent,
                        },
                    },
                )
            )

            fig.update_layout(
                height=350,
                margin=dict(l=40, r=40, t=60, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
            )

            st.plotly_chart(fig, use_container_width=True)

            if percent >= 90:
                st.success("🔥 Extremely High Top 10 Chance")
            elif percent >= 75:
                st.success("🟢 High Top 10 Chance")
            elif percent >= 55:
                st.warning("🟡 Moderate Top 10 Chance")
            elif percent >= 35:
                st.warning("🟠 Difficult Top 10")
            else:
                st.error("🔴 Very Low Top 10 Chance")

        st.divider()

        with st.expander("Model Inputs"):

            st.dataframe(input_data, use_container_width=True)
# =====================================================
# FINISHING POSITION PREDICTION
# =====================================================

elif page == "FINISHING POSITION PREDICTION":

    st.header("Finishing Position Prediction📍")

    @st.cache_resource
    def load_finish_model():
        with open(r"position.pkl", "rb") as f:
            return pickle.load(f)

    finish_model = load_finish_model()

    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    col1, col2 = st.columns(2)

    with col1:

        selected_driver = st.selectbox(
            "🏎 Driver", drivers["driver_name"], key="finish_driver"
        )

    driver_id = drivers.loc[drivers["driver_name"] == selected_driver, "driverId"].iloc[
        0
    ]

    teams = df[df["driverId"] == driver_id][
        ["constructorId", "name_team"]
    ].drop_duplicates()

    with col2:

        selected_team = st.selectbox("🏁 Team", teams["name_team"], key="finish_team")

    constructor_id = teams.loc[
        teams["name_team"] == selected_team, "constructorId"
    ].iloc[0]

    st.divider()

    circuits = (
        df[["circuitId", "name_race", "round"]]
        .drop_duplicates()
        .sort_values("name_race")
    )

    selected_race = st.selectbox(
        "🏟 Grand Prix", circuits["name_race"], key="finish_race"
    )

    race_row = circuits[circuits["name_race"] == selected_race].iloc[0]

    circuit_id = race_row["circuitId"]

    round_number = race_row["round"]

    grid = st.slider("🏁 Grid Position", 1, 20, 1, key="finish_grid")

    predict = st.button(
        "PREDICT FINISHING POSITION", use_container_width=True, key="finish_button"
    )

    if predict:

        input_data = pd.DataFrame(
            {
                "driverId": [driver_id],
                "constructorId": [constructor_id],
                "grid": [grid],
                "round": [round_number],
                "circuitId": [circuit_id],
            }
        )

        progress = st.progress(0)

        status = st.empty()

        import time

        status.text("Loading Race Data...")

        for i in range(35):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Running Regression Model...")

        for i in range(35, 70):
            progress.progress(i + 1)
            time.sleep(0.01)

        status.text("Predicting Finishing Position...")

        for i in range(70, 100):
            progress.progress(i + 1)
            time.sleep(0.01)

        progress.empty()
        status.empty()

        prediction = finish_model.predict(input_data)[0]

        prediction = round(float(prediction))

        if prediction < 1:
            prediction = 1

        if prediction > 20:
            prediction = 20

        st.divider()

        st.subheader("📍 Prediction Result")

        st.metric(label="Predicted Finishing Position", value=f"P{prediction}")

        if prediction == 1:

            st.success("🏆 Predicted Race Winner")

            if selected_driver == "Max Verstappen":

                play_sound(r"tu-tu-tu-du-max-verstappen.mp3")

            elif selected_driver == "Carlos Sainz":

                play_sound(r"smooth_operator.mp3")

            else:

                play_sound(r"F1 Car PassingBy.mp3")

        elif prediction <= 3:

            st.success("🥉 Predicted Podium Finish")

        elif prediction <= 10:

            st.info("🔟 Predicted Top 10 Finish")

        else:

            st.warning("Outside the Top 10 is predicted.")

        st.divider()

        with st.expander("Model Inputs"):

            st.dataframe(input_data, use_container_width=True)
# =====================================================
# DRIVER PERFORMANCE ANALYSIS
# =====================================================

elif page == "DRIVER PERFORMANCE ANALYSIS":

    st.header("📊 Driver Performance Analysis")

    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    selected_driver = st.selectbox(
        "🏎 Select Driver", drivers["driver_name"], key="analysis_driver"
    )

    driver_id = drivers.loc[drivers["driver_name"] == selected_driver, "driverId"].iloc[
        0
    ]

    driver_df = df[df["driverId"] == driver_id].copy()

    total_races = len(driver_df)

    wins = driver_df["winner"].sum() if "winner" in driver_df.columns else 0

    podiums = (
        (driver_df["positionOrder"] <= 3).sum()
        if "positionOrder" in driver_df.columns
        else 0
    )

    top10 = (
        (driver_df["positionOrder"] <= 10).sum()
        if "positionOrder" in driver_df.columns
        else 0
    )

    poles = (driver_df["grid"] == 1).sum()

    avg_finish = (
        round(driver_df["positionOrder"].mean(), 2)
        if "positionOrder" in driver_df.columns
        else "-"
    )

    avg_grid = round(driver_df["grid"].mean(), 2)

    best_finish = (
        driver_df["positionOrder"].min()
        if "positionOrder" in driver_df.columns
        else "-"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("🏁 Total Races", total_races)

    col2.metric("🏆 Wins", wins)

    col3.metric("🥉 Podiums", podiums)

    col4, col5, col6 = st.columns(3)

    col4.metric("🔟 Top 10", top10)

    col5.metric("🎯 Pole Positions", poles)

    col6.metric("⭐ Best Finish", best_finish)

    st.divider()

    col7, col8 = st.columns(2)

    col7.metric("📈 Average Finish", avg_finish)

    col8.metric("🏁 Average Grid", avg_grid)

    st.divider()

    st.subheader("Race History")

    show_cols = [
        c
        for c in ["year", "name_race", "name_team", "grid", "positionOrder", "winner"]
        if c in driver_df.columns
    ]

    st.dataframe(
        driver_df[show_cols].sort_values(by="year", ascending=False),
        use_container_width=True,
    )

    st.divider()
# =====================================================
# DRIVER COMPARISON
# =====================================================

elif page == "DRIVER COMPARISON":

    st.header("⚔ Driver Comparison")

    @st.cache_data
    def load_data():
        return pd.read_csv(r"master_full.csv")

    df = load_data()

    drivers = (
        df[["driverId", "forename", "surname"]].drop_duplicates().sort_values("surname")
    )

    drivers["driver_name"] = drivers["forename"] + " " + drivers["surname"]

    col1, col2 = st.columns(2)

    with col1:

        driver1 = st.selectbox("🏎 Driver 1", drivers["driver_name"], key="driver1")

    with col2:

        driver2 = st.selectbox(
            "🏎 Driver 2", drivers["driver_name"], index=1, key="driver2"
        )

    if driver1 == driver2:

        st.warning("Please select two different drivers.")

    else:

        id1 = drivers.loc[drivers["driver_name"] == driver1, "driverId"].iloc[0]

        id2 = drivers.loc[drivers["driver_name"] == driver2, "driverId"].iloc[0]

        df1 = df[df["driverId"] == id1].copy()
        df2 = df[df["driverId"] == id2].copy()

        def get_stats(driver_df):

            stats = {}

            stats["Total Races"] = len(driver_df)

            if "winner" in driver_df.columns:
                stats["Wins"] = int(driver_df["winner"].sum())
            else:
                stats["Wins"] = 0

            if "positionOrder" in driver_df.columns:

                stats["Podiums"] = int((driver_df["positionOrder"] <= 3).sum())

                stats["Top 10"] = int((driver_df["positionOrder"] <= 10).sum())

                stats["Best Finish"] = int(driver_df["positionOrder"].min())

                stats["Average Finish"] = round(driver_df["positionOrder"].mean(), 2)

            else:

                stats["Podiums"] = "-"

                stats["Top 10"] = "-"

                stats["Best Finish"] = "-"

                stats["Average Finish"] = "-"

            stats["Pole Positions"] = int((driver_df["grid"] == 1).sum())

            stats["Average Grid"] = round(driver_df["grid"].mean(), 2)

            return stats

        stats1 = get_stats(df1)

        stats2 = get_stats(df2)

        st.divider()

        comparison = pd.DataFrame({driver1: stats1, driver2: stats2})

        st.subheader("Comparison Statistics")

        st.dataframe(comparison, use_container_width=True)

        st.divider()

        dashboard_url = st.text_input(
            "Power BI Comparison Dashboard URL (Optional)", key="comparison_dashboard"
        )

        if dashboard_url:

            st.link_button(
                "OPEN COMPARISON DASHBOARD", dashboard_url, use_container_width=True
            )
# =====================================================
# EXTRA ANALYTICS (ADD BELOW DRIVER PERFORMANCE)
# =====================================================

import plotly.express as px

if page == "DRIVER PERFORMANCE ANALYSIS" and "driver_df" in locals():

    st.divider()

    st.subheader("📈 Performance Charts")

    if "year" in driver_df.columns and "positionOrder" in driver_df.columns:

        yearly = driver_df.groupby("year")["positionOrder"].mean().reset_index()

        fig = px.line(
            yearly,
            x="year",
            y="positionOrder",
            markers=True,
            title="Average Finishing Position by Year",
        )

        fig.update_yaxes(autorange="reversed")

        st.plotly_chart(fig, use_container_width=True)

    if "positionOrder" in driver_df.columns:

        finish_count = (
            driver_df["positionOrder"].value_counts().sort_index().reset_index()
        )

        finish_count.columns = ["Position", "Count"]

        fig = px.bar(
            finish_count,
            x="Position",
            y="Count",
            title="Finishing Position Distribution",
        )

        st.plotly_chart(fig, use_container_width=True)

    if "name_team" in driver_df.columns:

        teams = driver_df["name_team"].value_counts().reset_index()

        teams.columns = ["Team", "Races"]

        fig = px.pie(teams, names="Team", values="Races", title="Races by Constructor")

        st.plotly_chart(fig, use_container_width=True)

    if "grid" in driver_df.columns and "positionOrder" in driver_df.columns:

        fig = px.scatter(
            driver_df,
            x="grid",
            y="positionOrder",
            title="Grid Position vs Finish Position",
            trendline="ols",
        )

        fig.update_yaxes(autorange="reversed")

        st.plotly_chart(fig, use_container_width=True)
# =====================================================
# EXTRA COMPARISON CHARTS (ADD BELOW DRIVER COMPARISON)
# =====================================================

import plotly.graph_objects as go

if page == "DRIVER COMPARISON":

    st.divider()

    st.subheader("📊 Visual Comparison")

    radar_categories = ["Wins", "Podiums", "Top 10", "Pole Positions"]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=[
                stats1["Wins"],
                stats1["Podiums"],
                stats1["Top 10"],
                stats1["Pole Positions"],
            ],
            theta=radar_categories,
            fill="toself",
            name=driver1,
        )
    )

    fig.add_trace(
        go.Scatterpolar(
            r=[
                stats2["Wins"],
                stats2["Podiums"],
                stats2["Top 10"],
                stats2["Pole Positions"],
            ],
            theta=radar_categories,
            fill="toself",
            name=driver2,
        )
    )

    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)

    st.plotly_chart(fig, use_container_width=True)

    compare = pd.DataFrame(
        {
            "Statistic": ["Wins", "Podiums", "Top 10", "Pole Positions"],
            driver1: [
                stats1["Wins"],
                stats1["Podiums"],
                stats1["Top 10"],
                stats1["Pole Positions"],
            ],
            driver2: [
                stats2["Wins"],
                stats2["Podiums"],
                stats2["Top 10"],
                stats2["Pole Positions"],
            ],
        }
    )

    fig = px.bar(
        compare,
        x="Statistic",
        y=[driver1, driver2],
        barmode="group",
        title="Head-to-Head Statistics",
    )

    st.plotly_chart(fig, use_container_width=True)
