import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(
    page_title="Geometry Summary Statistics - Last 12 Months",
    layout="wide"
)

#### Last 12 Months Geometry ####

global_places_df = read_from_gsheets("Global Places")
global_places_df = global_places_df[["Release month", "Country", "POI with polygons"]]

for i, value in enumerate(global_places_df['Release month']):
    try:
        global_places_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%b %Y').strftime('%Y-%m')
    except ValueError:
        global_places_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%B %Y').strftime('%Y-%m')

start_date_str = (datetime.now() - timedelta(days=365)).strftime("%Y-%m")

global_places_df["Release month"] = pd.to_datetime(global_places_df["Release month"])
last_12_months_df = global_places_df[
    (global_places_df["Release month"] >= start_date_str) & (global_places_df["Release month"] <= datetime.now()) &
    (global_places_df["Country"] != "Grand Total")
]
last_12_months_df["Release month"] = pd.to_datetime(last_12_months_df["Release month"])+ pd.DateOffset(1)
last_12_months_df["Release month"] = last_12_months_df["Release month"].dt.strftime('%Y-%m-%dT%H:%M:%SZ')
last_12_months_df['POI with polygons'] = pd.to_numeric(last_12_months_df['POI with polygons'])

# st.dataframe(last_12_months_df)

last_12_months_geometry = alt.Chart(last_12_months_df).mark_bar().encode(
    x=alt.X('Release month', timeUnit='yearmonth'),
    y='POI with polygons',
    color='Country',
    tooltip=[alt.Tooltip('Release month', timeUnit='yearmonth', title='Release month'),
             alt.Tooltip('Country'),
             alt.Tooltip('POI with polygons', format=',')]
).properties(
    width=900,
    height=500,
    title=alt.TitleParams(
        text='Total POI with Polygon Count - Last 12 months',
        fontSize=18
    )
).configure_axisY(
    labelAngle=20
).configure_axisX(
    title=None,
    labelAngle=45
)

st.altair_chart(last_12_months_geometry, use_container_width=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)
