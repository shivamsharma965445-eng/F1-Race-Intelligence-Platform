import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="F1 Race Intelligence", layout="wide", page_icon="F1")

st.markdown("""
    <style>
    .stMetric { background-color: #1e1e2f; padding: 10px; border-radius: 10px; }
    div[data-testid="stSidebar"] { background-color: #0e0e1a; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/master_modern.csv')
    return df

df = load_data()

st.sidebar.title("F1 Race Intelligence")
st.sidebar.caption("Data Engineering + Dashboard by Palak")
page = st.sidebar.radio("Navigate", ["Overview", "Driver Comparison", "Advanced Charts", "Predictions"])

years = sorted(df['year'].unique())

if page == "Overview":
    st.title("Season Overview")
    st.caption("High-level snapshot of a season: who scored, who won, who dominated.")
    selected_year = st.sidebar.selectbox("Select Season", years, index=len(years)-1)
    df_year = df[df['year'] == selected_year]
    teams = sorted(df_year['name_team'].unique())
    selected_team = st.sidebar.selectbox("Select Team (optional)", ["All"] + teams)
    if selected_team != "All":
        df_year = df_year[df_year['name_team'] == selected_team]
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Races", df_year['raceId'].nunique())
    col2.metric("Total Drivers", df_year['driverId'].nunique())
    col3.metric("Total Wins", int(df_year['winner'].sum()))
    st.divider()
    st.subheader(f"Driver Points - {selected_year}")
    driver_points = (df_year.groupby(['forename', 'surname'])['points']
                     .sum().reset_index()
                     .sort_values('points', ascending=False).head(10))
    driver_points['driver'] = driver_points['forename'] + " " + driver_points['surname']
    st.plotly_chart(px.bar(driver_points, x='driver', y='points',
                            title="Top 10 Drivers by Points",
                            color='points', color_continuous_scale='Reds'),
                     use_container_width=True)
    if len(driver_points) > 0:
        gap = driver_points.iloc[0]['points'] - driver_points.iloc[1]['points'] if len(driver_points) > 1 else 0
        st.caption(f"{driver_points.iloc[0]['driver']} led the standings by a margin of {gap:.0f} points over the runner-up.")
    st.subheader(f"Team Points - {selected_year}")
    team_points = (df_year.groupby('name_team')['points']
                   .sum().reset_index().sort_values('points', ascending=False))
    st.plotly_chart(px.bar(team_points, x='name_team', y='points',
                            title="Team Points Comparison",
                            color='points', color_continuous_scale='Blues'),
                     use_container_width=True)
    st.subheader(f"Race Winners - {selected_year}")
    winners = df_year[df_year['winner'] == 1][['name_race', 'forename', 'surname', 'name_team', 'date']].copy()
    winners['driver'] = winners['forename'] + " " + winners['surname']
    winners = winners[['name_race', 'driver', 'name_team', 'date']].sort_values('date')
    st.dataframe(winners, use_container_width=True, hide_index=True)
    if len(winners) > 0:
        top_winner = winners['driver'].value_counts().idxmax()
        wins_count = winners['driver'].value_counts().max()
        st.caption(f"{top_winner} won the most races this season ({wins_count} wins).")

elif page == "Driver Comparison":
    st.title("Driver vs Driver Comparison")
    st.caption("Head-to-head stats across every season in the modern-era dataset.")
    df['driver_name'] = df['forename'] + " " + df['surname']
    all_drivers = sorted(df['driver_name'].unique())
    col1, col2 = st.columns(2)
    with col1:
        driver_a = st.selectbox("Driver A", all_drivers, index=0)
    with col2:
        default_b_index = 1 if len(all_drivers) > 1 else 0
        driver_b = st.selectbox("Driver B", all_drivers, index=default_b_index)
    if driver_a == driver_b:
        st.warning("Pick two different drivers to compare.")
    else:
        df_a = df[df['driver_name'] == driver_a]
        df_b = df[df['driver_name'] == driver_b]
        col1, col2, col3 = st.columns(3)
        col1.metric(f"{driver_a} - Wins", int(df_a['winner'].sum()))
        col2.metric(f"{driver_b} - Wins", int(df_b['winner'].sum()))
        col3.metric("Races in Common", len(set(df_a['raceId']) & set(df_b['raceId'])))
        st.subheader("Points Over Seasons")
        pts_a = df_a.groupby('year')['points'].sum().reset_index()
        pts_a['driver'] = driver_a
        pts_b = df_b.groupby('year')['points'].sum().reset_index()
        pts_b['driver'] = driver_b
        combined = pd.concat([pts_a, pts_b])
        st.plotly_chart(px.line(combined, x='year', y='points', color='driver', markers=True,
                                 title=f"{driver_a} vs {driver_b} - Points by Season"),
                         use_container_width=True)
        st.subheader("Average Finishing Position")
        avg_pos = pd.DataFrame({
            'driver': [driver_a, driver_b],
            'avg_position': [df_a['position'].mean(), df_b['position'].mean()]
        })
        st.plotly_chart(px.bar(avg_pos, x='driver', y='avg_position',
                                title="Lower is better"), use_container_width=True)
        better = driver_a if df_a['position'].mean() < df_b['position'].mean() else driver_b
        st.caption(f"{better} has the better average finishing position across their careers in this dataset.")

elif page == "Advanced Charts":
    st.title("Advanced Analysis")
    st.caption("Deeper patterns across the full modern-era dataset (2014 onward).")
    st.subheader("Grid Position vs Finish Position")
    scatter_df = df.dropna(subset=['grid', 'position'])
    scatter_df = scatter_df[scatter_df['grid'] > 0]
    fig = px.scatter(scatter_df, x='grid', y='position', opacity=0.3,
                      labels={'grid': 'Starting Grid Position', 'position': 'Finish Position'},
                      title="Grid vs Finish Position (all seasons)")
    st.plotly_chart(fig, use_container_width=True)
    corr = scatter_df['grid'].corr(scatter_df['position'])
    st.caption(f"Correlation between grid and finish position: {corr:.2f} - closer to 1 means qualifying strongly determines the race result.")
    st.subheader("Win Rate by Team")
    team_wins = df.groupby('name_team').agg(
        races=('raceId', 'nunique'),
        wins=('winner', 'sum')
    ).reset_index()
    team_wins['win_rate_pct'] = (team_wins['wins'] / team_wins['races'] * 100).round(1)
    team_wins = team_wins.sort_values('win_rate_pct', ascending=False).head(10)
    st.plotly_chart(px.bar(team_wins, x='name_team', y='win_rate_pct',
                            title="Top 10 Teams by Win Rate %",
                            color='win_rate_pct', color_continuous_scale='Viridis'),
                     use_container_width=True)
    if len(team_wins) > 0:
        st.caption(f"{team_wins.iloc[0]['name_team']} converted the highest share of races into wins ({team_wins.iloc[0]['win_rate_pct']}%).")
    st.subheader("Finish Status Breakdown (all seasons)")
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    st.plotly_chart(px.pie(status_counts.head(8), names='status', values='count',
                            title="Top Finish Statuses"), use_container_width=True)
    st.subheader("Points Distribution by Season")
    season_points = df.groupby('year')['points'].sum().reset_index()
    st.plotly_chart(px.line(season_points, x='year', y='points', markers=True,
                             title="Total Points Awarded per Season"), use_container_width=True)
    st.caption("Sharp jumps usually reflect F1 rule changes (more races added, or points system revised).")

elif page == "Predictions":
    st.title("Race Winner Prediction")
    model_path = "models/winner_model.pkl"
    if not os.path.exists(model_path):
        st.warning("No trained model found yet at models/winner_model.pkl. This page will activate once the ML teammate saves the trained model there.")
        st.info("Planned functionality: select a race and see predicted win probability per driver, compare predicted vs actual results, show feature importance.")
    else:
        import pickle
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        st.success("Model loaded successfully!")
        st.write("Prediction UI goes here once feature format is confirmed with the ML teammate.")

st.sidebar.divider()
st.sidebar.caption("F1 Race Intelligence Platform - Data Engineering + Dashboard Module")
