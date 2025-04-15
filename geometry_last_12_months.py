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

global_places_df = (read_from_gsheets("Global Places").query('Country  != "Excluding US"').reset_index(drop=True))
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
    color=alt.Color('Country', scale=alt.Scale(scheme='redyellowblue')),
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

# Keep-alive comment: 2025-03-29 14:27:08.415106
# Keep-alive comment: 2025-03-31 15:59:09.818782
# Keep-alive comment: 2025-03-31 19:24:48.200776
# Keep-alive comment: 2025-04-01 06:22:29.223829
# Keep-alive comment: 2025-04-01 17:23:23.020682
# Keep-alive comment: 2025-04-02 04:23:08.869239
# Keep-alive comment: 2025-04-02 15:23:07.828741
# Keep-alive comment: 2025-04-03 02:22:42.478793
# Keep-alive comment: 2025-04-03 13:23:48.207059
# Keep-alive comment: 2025-04-04 00:24:09.838430
# Keep-alive comment: 2025-04-04 11:23:40.992448
# Keep-alive comment: 2025-04-04 22:22:52.728463
# Keep-alive comment: 2025-04-05 09:22:42.888752
# Keep-alive comment: 2025-04-05 20:23:58.440709
# Keep-alive comment: 2025-04-06 07:23:28.003493
# Keep-alive comment: 2025-04-06 18:22:59.551322
# Keep-alive comment: 2025-04-07 05:23:23.206188
# Keep-alive comment: 2025-04-07 16:24:22.223844
# Keep-alive comment: 2025-04-08 03:23:38.690834
# Keep-alive comment: 2025-04-08 14:23:54.468847
# Keep-alive comment: 2025-04-09 01:23:22.431636
# Keep-alive comment: 2025-04-09 12:23:03.512647
# Keep-alive comment: 2025-04-09 23:23:23.013807
# Keep-alive comment: 2025-04-10 10:22:31.475077
# Keep-alive comment: 2025-04-10 21:22:56.398527
# Keep-alive comment: 2025-04-11 08:25:07.267080
# Keep-alive comment: 2025-04-11 19:25:27.908505
# Keep-alive comment: 2025-04-12 06:23:03.632137
# Keep-alive comment: 2025-04-12 17:23:16.984420
# Keep-alive comment: 2025-04-13 04:22:32.941430
# Keep-alive comment: 2025-04-13 15:23:31.346660
# Keep-alive comment: 2025-04-14 02:23:52.438305
# Keep-alive comment: 2025-04-14 13:23:16.124038
# Keep-alive comment: 2025-04-15 00:23:01.430993
# Keep-alive comment: 2025-04-15 11:23:23.251469