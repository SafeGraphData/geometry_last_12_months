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
# Keep-alive comment: 2025-04-15 22:23:06.972566
# Keep-alive comment: 2025-04-16 09:23:46.255556
# Keep-alive comment: 2025-04-16 20:23:36.538278
# Keep-alive comment: 2025-04-17 07:23:07.559660
# Keep-alive comment: 2025-04-17 18:25:31.057899
# Keep-alive comment: 2025-04-18 05:22:52.031579
# Keep-alive comment: 2025-04-18 16:22:57.333209
# Keep-alive comment: 2025-04-19 03:23:22.487131
# Keep-alive comment: 2025-04-19 14:22:33.277336
# Keep-alive comment: 2025-04-20 01:22:31.981097
# Keep-alive comment: 2025-04-20 12:23:26.991401
# Keep-alive comment: 2025-04-20 23:23:01.686920
# Keep-alive comment: 2025-04-21 10:23:47.844164
# Keep-alive comment: 2025-04-21 21:23:11.246265
# Keep-alive comment: 2025-04-22 08:23:22.015912
# Keep-alive comment: 2025-04-22 19:23:22.141590
# Keep-alive comment: 2025-04-23 06:22:56.196156
# Keep-alive comment: 2025-04-23 17:22:57.811594
# Keep-alive comment: 2025-04-24 04:23:02.382504
# Keep-alive comment: 2025-04-24 15:23:58.256228
# Keep-alive comment: 2025-04-25 02:22:33.720017
# Keep-alive comment: 2025-04-25 13:23:57.156163
# Keep-alive comment: 2025-04-25 16:08:08.361266
# Keep-alive comment: 2025-04-25 16:18:03.471763
# Keep-alive comment: 2025-04-26 00:23:37.392457
# Keep-alive comment: 2025-04-26 11:23:33.114476
# Keep-alive comment: 2025-04-26 22:22:32.215230
# Keep-alive comment: 2025-04-27 09:23:02.795526
# Keep-alive comment: 2025-04-27 20:22:57.458058
# Keep-alive comment: 2025-04-28 07:23:09.973676
# Keep-alive comment: 2025-04-28 18:23:47.668385
# Keep-alive comment: 2025-04-29 05:23:17.571906
# Keep-alive comment: 2025-04-29 16:24:01.135155
# Keep-alive comment: 2025-04-30 03:22:52.524035
# Keep-alive comment: 2025-04-30 14:23:01.910560
# Keep-alive comment: 2025-05-01 01:23:31.700813
# Keep-alive comment: 2025-05-01 12:23:02.454345
# Keep-alive comment: 2025-05-01 23:22:35.756697
# Keep-alive comment: 2025-05-02 10:23:21.413319
# Keep-alive comment: 2025-05-02 21:22:31.691386
# Keep-alive comment: 2025-05-03 08:22:56.278785
# Keep-alive comment: 2025-05-03 19:23:16.361449
# Keep-alive comment: 2025-05-04 06:23:21.530414
# Keep-alive comment: 2025-05-04 17:22:30.918687
# Keep-alive comment: 2025-05-05 04:23:41.283635
# Keep-alive comment: 2025-05-05 15:22:56.579252
# Keep-alive comment: 2025-05-06 02:23:51.018188
# Keep-alive comment: 2025-05-06 13:22:52.019839
# Keep-alive comment: 2025-05-07 00:22:52.035681
# Keep-alive comment: 2025-05-07 11:22:51.729212
# Keep-alive comment: 2025-05-07 22:23:01.520137
# Keep-alive comment: 2025-05-08 09:22:51.719998
# Keep-alive comment: 2025-05-08 20:22:51.581706
# Keep-alive comment: 2025-05-09 07:23:02.209625
# Keep-alive comment: 2025-05-09 18:23:22.265901
# Keep-alive comment: 2025-05-10 05:23:01.609214
# Keep-alive comment: 2025-05-10 16:22:55.928624
# Keep-alive comment: 2025-05-11 03:22:55.965174
# Keep-alive comment: 2025-05-11 14:22:47.844810
# Keep-alive comment: 2025-05-12 01:22:53.163921
# Keep-alive comment: 2025-05-12 12:23:22.271340
# Keep-alive comment: 2025-05-12 23:22:56.367405
# Keep-alive comment: 2025-05-13 10:23:51.985600
# Keep-alive comment: 2025-05-13 21:22:56.474974
# Keep-alive comment: 2025-05-14 08:23:15.207371
# Keep-alive comment: 2025-05-14 19:23:21.981003
# Keep-alive comment: 2025-05-15 06:23:22.561415
# Keep-alive comment: 2025-05-15 17:23:46.677533
# Keep-alive comment: 2025-05-16 04:23:08.561118
# Keep-alive comment: 2025-05-16 15:22:07.535942
# Keep-alive comment: 2025-05-17 02:22:26.664960
# Keep-alive comment: 2025-05-17 13:23:03.432889
# Keep-alive comment: 2025-05-18 00:22:27.850816
# Keep-alive comment: 2025-05-18 11:22:56.835691
# Keep-alive comment: 2025-05-18 22:22:54.170988
# Keep-alive comment: 2025-05-19 09:23:24.907749
# Keep-alive comment: 2025-05-19 20:22:26.811959
# Keep-alive comment: 2025-05-20 07:22:44.172868
# Keep-alive comment: 2025-05-21 05:22:29.149361
# Keep-alive comment: 2025-05-21 16:22:37.167751
# Keep-alive comment: 2025-05-22 03:22:31.469712
# Keep-alive comment: 2025-05-22 14:22:27.649421
# Keep-alive comment: 2025-05-23 01:22:34.044744
# Keep-alive comment: 2025-05-23 12:22:34.077780
# Keep-alive comment: 2025-05-23 23:22:39.012842
# Keep-alive comment: 2025-05-24 10:22:36.957694
# Keep-alive comment: 2025-05-24 21:22:33.306333
# Keep-alive comment: 2025-05-25 08:22:32.776382
# Keep-alive comment: 2025-05-25 19:22:38.756985
# Keep-alive comment: 2025-05-26 06:22:23.185435
# Keep-alive comment: 2025-05-26 17:22:28.162498
# Keep-alive comment: 2025-05-27 04:22:34.037024
# Keep-alive comment: 2025-05-27 15:22:37.464394
# Keep-alive comment: 2025-05-28 02:22:47.743038
# Keep-alive comment: 2025-05-28 13:22:35.334918
# Keep-alive comment: 2025-05-29 00:22:32.133648
# Keep-alive comment: 2025-05-29 11:22:26.794573
# Keep-alive comment: 2025-05-29 22:22:41.716369
# Keep-alive comment: 2025-05-30 09:22:26.223699
# Keep-alive comment: 2025-05-30 20:22:27.142085
# Keep-alive comment: 2025-05-31 07:22:39.046671
# Keep-alive comment: 2025-05-31 18:22:34.686439
# Keep-alive comment: 2025-06-01 05:22:33.272925
# Keep-alive comment: 2025-06-01 16:22:46.688416
# Keep-alive comment: 2025-06-02 03:22:47.989755
# Keep-alive comment: 2025-06-02 14:22:37.721322
# Keep-alive comment: 2025-06-03 01:22:29.012896
# Keep-alive comment: 2025-06-03 12:22:42.435496
# Keep-alive comment: 2025-06-03 23:22:36.660729
# Keep-alive comment: 2025-06-04 10:22:38.034889
# Keep-alive comment: 2025-06-04 21:22:16.718919
# Keep-alive comment: 2025-06-05 08:22:39.564798