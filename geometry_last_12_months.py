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
# Keep-alive comment: 2025-06-05 19:22:29.070737
# Keep-alive comment: 2025-06-06 06:22:28.730140
# Keep-alive comment: 2025-06-06 17:22:11.557550
# Keep-alive comment: 2025-06-07 04:22:12.974630
# Keep-alive comment: 2025-06-07 15:22:23.176821
# Keep-alive comment: 2025-06-08 02:22:28.495247
# Keep-alive comment: 2025-06-08 13:22:29.952281
# Keep-alive comment: 2025-06-09 00:22:12.789873
# Keep-alive comment: 2025-06-09 11:22:26.856781
# Keep-alive comment: 2025-06-09 22:22:35.107582
# Keep-alive comment: 2025-06-10 09:22:37.120022
# Keep-alive comment: 2025-06-10 20:22:31.532909
# Keep-alive comment: 2025-06-11 07:22:32.483835
# Keep-alive comment: 2025-06-11 18:24:18.601970
# Keep-alive comment: 2025-06-12 05:22:29.643538
# Keep-alive comment: 2025-06-12 16:22:32.592774
# Keep-alive comment: 2025-06-13 03:22:33.977848
# Keep-alive comment: 2025-06-13 14:22:22.733180
# Keep-alive comment: 2025-06-14 01:22:42.940759
# Keep-alive comment: 2025-06-14 12:22:30.556403
# Keep-alive comment: 2025-06-14 23:22:21.508557
# Keep-alive comment: 2025-06-15 10:22:07.285804
# Keep-alive comment: 2025-06-15 21:22:42.674469
# Keep-alive comment: 2025-06-16 08:22:38.248266
# Keep-alive comment: 2025-06-16 19:22:22.589416
# Keep-alive comment: 2025-06-17 06:22:58.650801
# Keep-alive comment: 2025-06-17 17:22:27.187509
# Keep-alive comment: 2025-06-18 04:22:34.379582
# Keep-alive comment: 2025-06-18 15:22:29.649732
# Keep-alive comment: 2025-06-19 02:22:31.665185
# Keep-alive comment: 2025-06-19 13:22:30.292029
# Keep-alive comment: 2025-06-20 00:22:28.273773
# Keep-alive comment: 2025-06-20 11:23:17.219860
# Keep-alive comment: 2025-06-20 22:22:37.129094
# Keep-alive comment: 2025-06-21 09:22:22.984641
# Keep-alive comment: 2025-06-21 20:22:34.656641
# Keep-alive comment: 2025-06-22 07:22:27.869476
# Keep-alive comment: 2025-06-22 18:22:18.476379
# Keep-alive comment: 2025-06-23 05:22:35.142613
# Keep-alive comment: 2025-06-23 16:22:27.331622
# Keep-alive comment: 2025-06-24 03:22:34.026117
# Keep-alive comment: 2025-06-24 14:22:12.355862
# Keep-alive comment: 2025-06-25 01:22:06.867188
# Keep-alive comment: 2025-06-25 12:22:28.496801
# Keep-alive comment: 2025-06-25 23:22:32.137059
# Keep-alive comment: 2025-06-26 10:22:39.568986
# Keep-alive comment: 2025-06-26 21:24:02.770504
# Keep-alive comment: 2025-06-27 08:22:32.742055
# Keep-alive comment: 2025-06-27 19:22:29.607965
# Keep-alive comment: 2025-06-28 06:22:37.650052
# Keep-alive comment: 2025-06-28 17:22:27.962374
# Keep-alive comment: 2025-06-29 04:22:16.896771
# Keep-alive comment: 2025-06-29 15:22:07.471610
# Keep-alive comment: 2025-06-30 02:22:28.865711
# Keep-alive comment: 2025-06-30 13:22:08.974974
# Keep-alive comment: 2025-07-01 00:24:14.585561
# Keep-alive comment: 2025-07-01 11:22:28.929205
# Keep-alive comment: 2025-07-01 22:22:33.870568
# Keep-alive comment: 2025-07-02 09:22:27.441111
# Keep-alive comment: 2025-07-02 20:24:16.025231
# Keep-alive comment: 2025-07-03 07:22:42.188890
# Keep-alive comment: 2025-07-03 18:22:06.475159
# Keep-alive comment: 2025-07-04 05:22:31.117474
# Keep-alive comment: 2025-07-04 16:22:26.924664
# Keep-alive comment: 2025-07-05 03:22:26.564501
# Keep-alive comment: 2025-07-05 14:22:31.820772
# Keep-alive comment: 2025-07-06 01:22:28.450973
# Keep-alive comment: 2025-07-06 12:22:26.362365
# Keep-alive comment: 2025-07-06 23:22:27.243711
# Keep-alive comment: 2025-07-07 10:22:26.930639
# Keep-alive comment: 2025-07-07 21:22:25.943415
# Keep-alive comment: 2025-07-08 08:22:31.200964
# Keep-alive comment: 2025-07-08 19:22:26.199696
# Keep-alive comment: 2025-07-09 06:22:38.226497
# Keep-alive comment: 2025-07-09 17:23:10.566305
# Keep-alive comment: 2025-07-10 04:22:26.772639
# Keep-alive comment: 2025-07-10 15:22:31.253485
# Keep-alive comment: 2025-07-11 02:22:25.904644
# Keep-alive comment: 2025-07-11 13:22:26.041915
# Keep-alive comment: 2025-07-12 00:22:12.807419
# Keep-alive comment: 2025-07-12 11:22:31.449534
# Keep-alive comment: 2025-07-12 22:22:26.614097
# Keep-alive comment: 2025-07-13 09:22:27.421867
# Keep-alive comment: 2025-07-13 20:22:11.684147
# Keep-alive comment: 2025-07-14 07:22:22.513113
# Keep-alive comment: 2025-07-14 18:22:46.019970
# Keep-alive comment: 2025-07-15 05:22:37.398381
# Keep-alive comment: 2025-07-15 16:22:31.059138
# Keep-alive comment: 2025-07-16 03:22:31.485761
# Keep-alive comment: 2025-07-16 14:22:31.129101
# Keep-alive comment: 2025-07-17 01:22:26.878084
# Keep-alive comment: 2025-07-17 12:22:32.375982
# Keep-alive comment: 2025-07-17 23:22:25.278075
# Keep-alive comment: 2025-07-18 10:22:46.098331
# Keep-alive comment: 2025-07-18 21:22:26.454996
# Keep-alive comment: 2025-07-19 08:23:07.257403
# Keep-alive comment: 2025-07-19 19:22:11.789766
# Keep-alive comment: 2025-07-20 06:22:36.642001
# Keep-alive comment: 2025-07-20 17:22:42.256815
# Keep-alive comment: 2025-07-21 04:22:36.790842
# Keep-alive comment: 2025-07-21 15:22:22.300798
# Keep-alive comment: 2025-07-22 02:22:46.173331
# Keep-alive comment: 2025-07-22 13:22:58.135989
# Keep-alive comment: 2025-07-23 00:22:32.991520
# Keep-alive comment: 2025-07-23 11:22:21.903707
# Keep-alive comment: 2025-07-23 22:22:25.747847
# Keep-alive comment: 2025-07-24 09:22:41.576278
# Keep-alive comment: 2025-07-24 20:22:27.160906
# Keep-alive comment: 2025-07-25 07:22:21.842680
# Keep-alive comment: 2025-07-25 18:22:26.290978
# Keep-alive comment: 2025-07-26 05:22:22.473972
# Keep-alive comment: 2025-07-26 16:22:26.296131
# Keep-alive comment: 2025-07-27 03:22:21.820455
# Keep-alive comment: 2025-07-27 14:22:12.090709
# Keep-alive comment: 2025-07-28 01:22:32.654019
# Keep-alive comment: 2025-07-28 12:22:27.538910
# Keep-alive comment: 2025-07-28 23:22:26.118613
# Keep-alive comment: 2025-07-29 10:22:00.879460
# Keep-alive comment: 2025-07-29 21:22:31.906006
# Keep-alive comment: 2025-07-30 08:22:27.616019
# Keep-alive comment: 2025-07-30 19:22:35.934375
# Keep-alive comment: 2025-07-31 06:22:41.382342
# Keep-alive comment: 2025-07-31 17:22:26.847575
# Keep-alive comment: 2025-08-01 04:22:26.033365
# Keep-alive comment: 2025-08-01 15:22:36.220916
# Keep-alive comment: 2025-08-02 02:22:21.845894
# Keep-alive comment: 2025-08-02 13:22:31.969675
# Keep-alive comment: 2025-08-03 00:22:27.518177
# Keep-alive comment: 2025-08-03 11:22:32.441495
# Keep-alive comment: 2025-08-03 22:22:26.777045
# Keep-alive comment: 2025-08-04 09:22:23.137588
# Keep-alive comment: 2025-08-04 20:22:26.547448
# Keep-alive comment: 2025-08-05 07:22:29.827291
# Keep-alive comment: 2025-08-05 18:22:31.001930
# Keep-alive comment: 2025-08-06 05:22:26.619615
# Keep-alive comment: 2025-08-06 16:24:16.643631
# Keep-alive comment: 2025-08-07 03:22:31.078392
# Keep-alive comment: 2025-08-07 14:22:31.638085
# Keep-alive comment: 2025-08-08 01:22:21.097877
# Keep-alive comment: 2025-08-08 12:22:32.012436
# Keep-alive comment: 2025-08-08 23:22:32.745714
# Keep-alive comment: 2025-08-09 10:22:26.789021
# Keep-alive comment: 2025-08-09 21:22:48.161475
# Keep-alive comment: 2025-08-10 08:22:32.741191
# Keep-alive comment: 2025-08-10 19:22:32.768349
# Keep-alive comment: 2025-08-11 06:22:26.672004
# Keep-alive comment: 2025-08-11 17:22:31.661679
# Keep-alive comment: 2025-08-12 04:22:31.245615
# Keep-alive comment: 2025-08-12 15:22:22.213794
# Keep-alive comment: 2025-08-13 02:22:31.690083
# Keep-alive comment: 2025-08-13 13:22:26.624460
# Keep-alive comment: 2025-08-14 00:22:25.803828
# Keep-alive comment: 2025-08-14 11:22:32.545347
# Keep-alive comment: 2025-08-14 22:22:26.256469
# Keep-alive comment: 2025-08-15 09:22:26.013474
# Keep-alive comment: 2025-08-15 20:22:15.788073
# Keep-alive comment: 2025-08-16 07:22:41.178347
# Keep-alive comment: 2025-08-16 18:22:26.369910
# Keep-alive comment: 2025-08-17 05:22:30.691123
# Keep-alive comment: 2025-08-17 16:22:25.977897
# Keep-alive comment: 2025-08-18 03:22:26.883459
# Keep-alive comment: 2025-08-18 14:22:26.694105
# Keep-alive comment: 2025-08-19 01:22:27.043901
# Keep-alive comment: 2025-08-19 12:22:31.542051
# Keep-alive comment: 2025-08-19 23:22:53.667463
# Keep-alive comment: 2025-08-20 10:22:26.854995
# Keep-alive comment: 2025-08-20 21:22:31.242241
# Keep-alive comment: 2025-08-21 08:22:28.086897
# Keep-alive comment: 2025-08-21 19:22:32.104029
# Keep-alive comment: 2025-08-22 06:22:31.840695
# Keep-alive comment: 2025-08-22 17:22:26.866966
# Keep-alive comment: 2025-08-23 04:22:36.913658
# Keep-alive comment: 2025-08-23 15:22:25.964060
# Keep-alive comment: 2025-08-24 02:22:25.949858
# Keep-alive comment: 2025-08-24 13:22:26.627949
# Keep-alive comment: 2025-08-25 00:22:32.484613
# Keep-alive comment: 2025-08-25 11:22:31.571434
# Keep-alive comment: 2025-08-25 22:22:26.543892
# Keep-alive comment: 2025-08-26 09:22:27.021853
# Keep-alive comment: 2025-08-26 20:22:31.266235
# Keep-alive comment: 2025-08-27 07:22:36.382503
# Keep-alive comment: 2025-08-27 18:22:05.934900
# Keep-alive comment: 2025-08-28 05:22:36.812530
# Keep-alive comment: 2025-08-28 16:22:26.511163
# Keep-alive comment: 2025-08-29 03:22:10.988519
# Keep-alive comment: 2025-08-29 14:22:16.337437
# Keep-alive comment: 2025-08-30 01:22:16.163665
# Keep-alive comment: 2025-08-30 12:22:12.006009
# Keep-alive comment: 2025-08-30 23:22:15.564950
# Keep-alive comment: 2025-08-31 10:22:11.056074
# Keep-alive comment: 2025-08-31 21:22:22.831140
# Keep-alive comment: 2025-09-01 08:22:23.457828
# Keep-alive comment: 2025-09-01 19:22:22.942366
# Keep-alive comment: 2025-09-02 06:22:11.113636
# Keep-alive comment: 2025-09-02 17:22:22.093104
# Keep-alive comment: 2025-09-03 04:22:15.524030
# Keep-alive comment: 2025-09-03 15:22:16.745896
# Keep-alive comment: 2025-09-04 02:22:21.166669
# Keep-alive comment: 2025-09-04 13:22:24.008162
# Keep-alive comment: 2025-09-05 00:22:12.007122
# Keep-alive comment: 2025-09-05 11:22:06.733107
# Keep-alive comment: 2025-09-05 22:22:16.324997
# Keep-alive comment: 2025-09-06 09:22:12.790643
# Keep-alive comment: 2025-09-06 20:22:11.483793
# Keep-alive comment: 2025-09-07 07:22:17.390308
# Keep-alive comment: 2025-09-07 18:22:17.421613
# Keep-alive comment: 2025-09-08 05:22:13.205490
# Keep-alive comment: 2025-09-08 16:22:17.124670
# Keep-alive comment: 2025-09-09 03:22:42.088762
# Keep-alive comment: 2025-09-09 14:22:17.111414
# Keep-alive comment: 2025-09-10 01:22:10.980381
# Keep-alive comment: 2025-09-10 12:22:21.868433
# Keep-alive comment: 2025-09-10 23:22:11.387016
# Keep-alive comment: 2025-09-11 10:22:14.142104
# Keep-alive comment: 2025-09-11 21:22:11.855752
# Keep-alive comment: 2025-09-12 08:22:26.314023
# Keep-alive comment: 2025-09-12 19:22:16.917548
# Keep-alive comment: 2025-09-13 06:22:06.226659
# Keep-alive comment: 2025-09-13 17:22:12.797062
# Keep-alive comment: 2025-09-14 04:22:02.407489
# Keep-alive comment: 2025-09-14 15:22:13.955237
# Keep-alive comment: 2025-09-15 02:22:11.369123
# Keep-alive comment: 2025-09-15 13:22:12.460630
# Keep-alive comment: 2025-09-16 00:22:11.775927
# Keep-alive comment: 2025-09-16 11:22:16.636606
# Keep-alive comment: 2025-09-16 22:22:11.041616
# Keep-alive comment: 2025-09-17 09:22:12.513996
# Keep-alive comment: 2025-09-17 20:22:21.802144
# Keep-alive comment: 2025-09-18 07:22:18.808772
# Keep-alive comment: 2025-09-18 18:22:18.002210
# Keep-alive comment: 2025-09-19 05:22:12.906300
# Keep-alive comment: 2025-09-19 16:22:46.670575
# Keep-alive comment: 2025-09-20 03:22:17.189032
# Keep-alive comment: 2025-09-20 14:22:18.052325
# Keep-alive comment: 2025-09-21 01:22:17.168705
# Keep-alive comment: 2025-09-21 12:22:17.042916
# Keep-alive comment: 2025-09-21 23:22:12.463554
# Keep-alive comment: 2025-09-22 10:22:14.398947
# Keep-alive comment: 2025-09-22 21:22:11.105404
# Keep-alive comment: 2025-09-23 08:22:12.367209
# Keep-alive comment: 2025-09-23 19:22:17.888101
# Keep-alive comment: 2025-09-24 06:22:11.756839
# Keep-alive comment: 2025-09-24 17:22:16.442482
# Keep-alive comment: 2025-09-25 04:22:21.506942
# Keep-alive comment: 2025-09-25 15:22:21.362780
# Keep-alive comment: 2025-09-26 02:22:17.496789
# Keep-alive comment: 2025-09-26 13:22:21.533805
# Keep-alive comment: 2025-09-26 19:30:48.515470
# Keep-alive comment: 2025-09-27 05:30:55.085016
# Keep-alive comment: 2025-09-27 15:30:48.899881
# Keep-alive comment: 2025-09-28 01:30:53.189585
# Keep-alive comment: 2025-09-28 11:30:54.181920
# Keep-alive comment: 2025-09-28 21:30:53.665731
# Keep-alive comment: 2025-09-29 07:30:59.404006
# Keep-alive comment: 2025-09-29 17:31:09.502862
# Keep-alive comment: 2025-09-30 03:30:48.271450
# Keep-alive comment: 2025-09-30 13:30:53.922166
# Keep-alive comment: 2025-09-30 23:31:14.162617
# Keep-alive comment: 2025-10-01 09:31:19.790357
# Keep-alive comment: 2025-10-01 19:30:53.616065
# Keep-alive comment: 2025-10-02 05:31:23.073249
# Keep-alive comment: 2025-10-02 15:31:19.680144
# Keep-alive comment: 2025-10-03 01:30:53.566238
# Keep-alive comment: 2025-10-03 11:31:14.304862
# Keep-alive comment: 2025-10-03 21:30:48.624629
# Keep-alive comment: 2025-10-04 07:30:49.280500
# Keep-alive comment: 2025-10-04 17:30:58.911689
# Keep-alive comment: 2025-10-05 03:30:54.234480
# Keep-alive comment: 2025-10-05 13:30:58.967601
# Keep-alive comment: 2025-10-05 23:31:19.276204
# Keep-alive comment: 2025-10-06 09:31:24.305287
# Keep-alive comment: 2025-10-06 19:30:54.199915
# Keep-alive comment: 2025-10-07 05:30:55.906157
# Keep-alive comment: 2025-10-07 15:31:16.525683
# Keep-alive comment: 2025-10-08 01:30:54.542656
# Keep-alive comment: 2025-10-08 11:30:55.103070
# Keep-alive comment: 2025-10-08 21:30:54.584069
# Keep-alive comment: 2025-10-09 07:30:56.379182
# Keep-alive comment: 2025-10-09 17:30:56.021887
# Keep-alive comment: 2025-10-10 03:30:44.769900
# Keep-alive comment: 2025-10-10 13:30:35.488929
# Keep-alive comment: 2025-10-10 23:30:49.241512
# Keep-alive comment: 2025-10-11 09:30:55.163810
# Keep-alive comment: 2025-10-11 19:30:48.630504
# Keep-alive comment: 2025-10-12 05:30:51.980042
# Keep-alive comment: 2025-10-12 15:30:55.905987
# Keep-alive comment: 2025-10-13 01:30:50.520148
# Keep-alive comment: 2025-10-13 11:31:21.839871
# Keep-alive comment: 2025-10-13 21:30:44.962747
# Keep-alive comment: 2025-10-14 07:30:48.778714
# Keep-alive comment: 2025-10-14 17:30:51.447605
# Keep-alive comment: 2025-10-15 03:30:49.012657
# Keep-alive comment: 2025-10-15 13:30:49.833394
# Keep-alive comment: 2025-10-15 23:30:54.549552
# Keep-alive comment: 2025-10-16 09:30:49.776013
# Keep-alive comment: 2025-10-16 19:30:55.479806
# Keep-alive comment: 2025-10-17 05:30:54.713425
# Keep-alive comment: 2025-10-17 15:31:10.800838
# Keep-alive comment: 2025-10-18 01:30:50.400079
# Keep-alive comment: 2025-10-18 11:31:15.513730
# Keep-alive comment: 2025-10-18 21:31:25.049340
# Keep-alive comment: 2025-10-19 07:30:44.969662
# Keep-alive comment: 2025-10-19 17:31:19.925607
# Keep-alive comment: 2025-10-20 03:31:17.164408
# Keep-alive comment: 2025-10-20 13:30:55.000286
# Keep-alive comment: 2025-10-20 23:30:49.786999
# Keep-alive comment: 2025-10-21 09:30:55.444727
# Keep-alive comment: 2025-10-21 19:32:55.198527
# Keep-alive comment: 2025-10-22 05:30:50.914745
# Keep-alive comment: 2025-10-22 15:31:55.371237
# Keep-alive comment: 2025-10-23 01:30:49.867350
# Keep-alive comment: 2025-10-23 11:31:02.285953
# Keep-alive comment: 2025-10-23 21:30:50.988297
# Keep-alive comment: 2025-10-24 07:32:10.931649
# Keep-alive comment: 2025-10-24 17:31:00.520647