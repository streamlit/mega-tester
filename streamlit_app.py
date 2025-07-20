import time

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import pydeck as pdk
import streamlit as st


# Add disable toggle in sidebar
with st.sidebar:
    help = "Tooltip text" if st.toggle("Show tooltips", True) else None
    disabled = st.toggle("Disable widgets", False)
    nav_sections = st.toggle("Page sections", True)
    many_pages = st.toggle("Many pages", False)
    top_nav = st.toggle("Top navigation", False)
    wide_mode = st.toggle("Wide mode", False)
    st.divider()


st.logo("https://streamlit.io/images/brand/streamlit-mark-color.png")
st.title("🎈 Mega tester app")
st.set_page_config("Mega tester app", "🎈", layout="wide" if wide_mode else "centered")

def page1():
    pass


def page2():
    pass


def page3():
    pass


def page4():
    pass


def page5():
    pass


def page6():
    pass


def page7():
    pass


def page8():
    pass


def page9():
    pass


def page10():
    pass


def page11():
    pass


def page12():
    pass


def page13():
    pass


if many_pages:
    pages = {
        "General": [
            st.Page(page1, title="Home", icon=":material/home:"),
            st.Page(page2, title="Data visualizations", icon=":material/monitoring:"),
            st.Page(page3, title="Analytics", icon=":material/analytics:"),
        ],
        "Tools": [
            st.Page(page4, title="Calculator", icon=":material/calculate:"),
            st.Page(page5, title="Editor", icon=":material/edit:"),
            st.Page(page6, title="Viewer", icon=":material/visibility:"),
            st.Page(page7, title="Converter", icon=":material/swap_horiz:"),
        ],
        "Data": [
            st.Page(page8, title="Import", icon=":material/file_upload:"),
            st.Page(page9, title="Export", icon=":material/file_download:"),
            st.Page(page10, title="Transform", icon=":material/transform:"),
        ],
        "Admin": [
            st.Page(page11, title="Settings", icon=":material/settings:"),
            st.Page(page12, title="Users", icon=":material/people:"),
            st.Page(page13, title="Logs", icon=":material/history:"),
        ],
    }
else:
    pages = {
        "General": [
            st.Page(page1, title="Home", icon=":material/home:"),
            st.Page(page2, title="Data visualizations", icon=":material/monitoring:"),
        ],
        "Admin": [st.Page(page3, title="Settings", icon=":material/settings:")],
    }

st.navigation(
    pages if nav_sections else [page for section in pages.values() for page in section],
    position="top" if top_nav else "sidebar"
)


"## Write and magic"
st.write("st.write")
"magic"


"## Text elements"
st.markdown("st.markdown", help=help)
st.markdown(
    "Markdown features: **bold** *italic* ~strikethrough~ [link](https://streamlit.io) `code` $a=b$ 🐶 :cat: :material/home: :streamlit: <- -> <-> -- >= <= ~= :small[small] $$a = b$$"
)
st.markdown("""
Text colors: 

:blue[blue] :green[green] :orange[orange] :red[red] :violet[violet] :gray[gray] :rainbow[rainbow] :primary[primary]

:blue-background[blue] :green-background[green] :orange-background[orange] :red-background[red] :violet-background[violet] :gray-background[gray] :rainbow-background[rainbow] :primary-background[primary]

:blue-badge[blue] :green-badge[green] :orange-badge[orange] :red-badge[red] :violet-badge[violet] :gray-badge[gray] :primary-badge[primary]
""")
st.title("st.title", help=help)
st.header("st.header", help=help)
st.header("st.header with blue divider", divider="blue", help=help)
st.header("st.header with green divider", divider="green", help=help)
st.header("st.header with orange divider", divider="orange", help=help)
st.header("st.header with red divider", divider="red", help=help)
st.header("st.header with violet divider", divider="violet", help=help)
st.header("st.header with gray divider", divider="gray", help=help)
st.header("st.header with rainbow divider", divider="rainbow", help=help)
st.subheader("st.subheader", help=help)
st.badge("st.badge", icon=":material/home:", color="green")
st.caption("st.caption", help=help)
st.code("# st.code\na = 1234")
st.code("# st.code with line numbers\na = 1234", line_numbers=True)
st.code(
    '# st.code with line wrapping\na = "This is a very very very very very very very very very very very very long string"',
    wrap_lines=True,
)
with st.echo():
    st.write("st.echo")
st.latex(r"\int a x^2 \,dx", help=help)
st.text("st.text", help=help)
st.divider()


"## Data elements"
np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

"st.dataframe"
st.dataframe(data)

"st.data_editor"
st.data_editor(data, disabled=disabled)

"st.column_config"
data_df = pd.DataFrame(
    {
        "column": ["foo", "bar", "baz"],
        "text": ["foo", "bar", "baz"],
        "number": [1, 2, 3],
        "checkbox": [True, False, True],
        "selectbox": ["foo", "bar", "foo"],
        "datetime": pd.to_datetime(
            ["2021-01-01 00:00:00", "2021-01-02 00:00:00", "2021-01-03 00:00:00"]
        ),
        "date": pd.to_datetime(["2021-01-01", "2021-01-02", "2021-01-03"]),
        "time": pd.to_datetime(["00:00:00", "01:00:00", "02:00:00"]),
        "list": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "link": [
            "https://streamlit.io",
            "https://streamlit.io",
            "https://streamlit.io",
        ],
        "image": [
            "https://picsum.photos/200/300",
            "https://picsum.photos/200/300",
            "https://picsum.photos/200/300",
        ],
        "area_chart": [[1, 2, 1], [2, 3, 1], [3, 1, 2]],
        "line_chart": [[1, 2, 1], [2, 3, 1], [3, 1, 2]],
        "bar_chart": [[1, 2, 1], [2, 3, 1], [3, 1, 2]],
        "progress": [0.1, 0.2, 0.3],
        "json": [
            {
                "foo": "bar",
            },
            {
                "numbers": [123, 4.56],
            },
            {
                "level1": {"level2": {"level3": {"a": "b"}}},
            },
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "column": st.column_config.Column(
            "Column", help="A column tooltip", pinned=True
        ),
        "text": st.column_config.TextColumn("TextColumn"),
        "number": st.column_config.NumberColumn("NumberColumn"),
        "checkbox": st.column_config.CheckboxColumn("CheckboxColumn"),
        "selectbox": st.column_config.SelectboxColumn(
            "SelectboxColumn", options=["foo", "bar", "baz"]
        ),
        "datetime": st.column_config.DatetimeColumn("DatetimeColumn"),
        "date": st.column_config.DateColumn("DateColumn"),
        "time": st.column_config.TimeColumn("TimeColumn"),
        "list": st.column_config.ListColumn("ListColumn"),
        "link": st.column_config.LinkColumn("LinkColumn"),
        "image": st.column_config.ImageColumn("ImageColumn"),
        "area_chart": st.column_config.AreaChartColumn("AreaChartColumn"),
        "line_chart": st.column_config.LineChartColumn("LineChartColumn"),
        "bar_chart": st.column_config.BarChartColumn("BarChartColumn"),
        "progress": st.column_config.ProgressColumn("ProgressColumn"),
        "json": st.column_config.JsonColumn("JSONColumn"),
    },
)

"st.table"
st.table(data.iloc[0:5])

col1, col2 = st.columns(2)
col1.metric("st.metric positive", 1234, 123, help=help)
col2.metric("st.metric negative", 1234, -123, help=help)

col1, col2 = st.columns(2)
col1.metric("st.metric with border positive", 1234, 123, border=True, help=help)
col2.metric("st.metric with border negative", 1234, -123, border=True, help=help)

"st.json"
st.json(
    {
        "foo": "bar",
        "numbers": [
            123,
            4.56,
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)


"## Chart elements"
data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
"st.area_chart"
stack = st.segmented_control(
    "stack",
    [True, False, "normalize", "center"],
    key="area_chart_stack",
)
st.area_chart(data, x_label="x label", y_label="y label", stack=stack)
"st.bar_chart"
horizontal = st.toggle("horizontal", False)
stack = st.segmented_control(
    "stack",
    [True, False, "normalize", "center"],
    key="bar_chart_stack",
)
st.bar_chart(
    data, x_label="x label", y_label="y label", horizontal=horizontal, stack=stack
)
"st.line_chart"
st.line_chart(data, x_label="x label", y_label="y label")
"st.scatter_chart"
st.scatter_chart(data, x_label="x label", y_label="y label")

"st.map"
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(df)

"st.pyplot"
fig, ax = plt.subplots()
ax.hist(data, bins=20)
st.pyplot(fig)

"st.altair_chart"
st.altair_chart(
    alt.Chart(data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"]),
    use_container_width=True,
)

"st.vega_lite_chart"
st.vega_lite_chart(
    data,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
    use_container_width=True,
)

"st.plotly_chart"
df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
st.plotly_chart(fig, use_container_width=True)

"st.bokeh_chart"
if st.toggle("Show Bokeh chart (has some issues)", False):
    from bokeh.plotting import figure

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
    p.line(x, y, legend_label="Trend", line_width=2)
    st.bokeh_chart(p, use_container_width=True)

"st.pydeck_chart"
data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

"st.graphviz_chart"
st.graphviz_chart(
    """
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
    """
)


"## Input widgets"
if st.button("st.button", help=help, icon=":material/home:", disabled=disabled):
    st.write("You pressed the button!")

if st.button("st.button primary", type="primary", help=help, icon=":material/home:", disabled=disabled):
    st.write("You pressed the button!")

if st.button("st.button tertiary", type="tertiary", help=help, icon=":material/home:", disabled=disabled):
    st.write("You pressed the button!")

st.download_button("st.download_button", data="Hello!", icon=":material/home:", help=help, disabled=disabled)

"st.feedback"
st.feedback("thumbs", disabled=disabled)
st.feedback("faces", disabled=disabled)
st.feedback("stars", disabled=disabled)

st.link_button("st.link_button", "https://streamlit.io", icon=":material/home:", help=help, disabled=disabled)

st.page_link("https://streamlit.io", label="st.page_link", icon=":material/home:", help=help, disabled=disabled)

checkbox_input = st.checkbox("st.checkbox", True, help=help, disabled=disabled)
st.write(f"Your checkbox input is {checkbox_input}!")

toggle_input = st.toggle("st.toggle", True, help=help, disabled=disabled)
st.write(f"Your toggle input is {toggle_input}!")

radio_input = st.radio("st.radio", ["cat", "dog"], help=help, disabled=disabled)
st.write(f"Your radio input is {radio_input}!")

radio_input = st.radio("st.radio horizontal", ["cat", "dog"], horizontal=True, help=help, disabled=disabled)
st.write(f"Your radio input is {radio_input}!")

selectbox_input = st.selectbox(
    "st.selectbox", ["cat", "dog", "monkey", "snake", "bird"], help=help, disabled=disabled
)
st.write(f"Your selectbox input is {selectbox_input}!")

multiselect_input = st.multiselect(
    "st.multiselect",
    ["cat", "dog", "monkey", "snake", "bird"],
    default=["cat", "monkey"],
    disabled=disabled,
    help=help,
)
st.write(f"Your multiselect input is {multiselect_input}!")

pills_input = st.pills(
    "st.pills",
    ["cat", "dog", "monkey", "snake", "bird"],
    selection_mode="multi",
    default=["cat", "monkey"],
    disabled=disabled,
    help=help,
)
st.write(f"Your pills input is {pills_input}!")

segmented_control_input = st.segmented_control(
    "st.segmented_control",
    ["cat", "dog", "monkey", "snake", "bird"],
    selection_mode="multi",
    default=["cat", "monkey"],
    disabled=disabled,
    help=help,
)
st.write(f"Your segmented control input is {segmented_control_input}!")

color_input = st.color_picker("st.color_picker", disabled=disabled, help=help)
st.write(f"Your color input hex is {color_input}!")

number_input = st.number_input("st.number_input", disabled=disabled, help=help)
st.write(f"Your number input is {number_input}!")

range_sliders = st.toggle("Range sliders", False)

slider_input = st.slider("st.slider", value=[30, 60] if range_sliders else 30, disabled=disabled, help=help)
st.write(f"Your slider input is {slider_input}!")

select_slider_input = st.select_slider(
    "st.select_slider",
    options=["xsmall", "small", "medium", "large", "xlarge"],
    value=["small", "large"] if range_sliders else "small",
    disabled=disabled,
    help=help,
)
st.write(f"Your select_slider input is {select_slider_input}!")

date_input = st.date_input("st.date_input", disabled=disabled, help=help)
st.write(f"Your date input is {date_input}!")

time_input = st.time_input("st.time_input", disabled=disabled, help=help)
st.write(f"Your time input is {time_input}!")

text_input = st.text_input("st.text_input", disabled=disabled, help=help)
st.write(f"Your text input is {text_input}!")

text_area_input = st.text_area("st.text_area", disabled=disabled, help=help)
st.write(f"Your text_area input is {text_area_input}!")

audio_input = st.audio_input("st.audio_input", disabled=disabled, help=help)
st.write(f"Your audio input is {audio_input}!")

file_input = st.file_uploader("st.file_input", disabled=disabled, help=help)

if st.toggle("Show camera input (requires camera permission)", False):
    cam_input = st.camera_input("st.camera_input", disabled=disabled, help=help)
    st.write(f"Your cam input is {cam_input}!")


"## Media elements"
"st.image"
st.image("https://picsum.photos/200/300")

"st.audio"
st.audio(
    "https://file-examples.com/storage/fe8d06553067e519a994eaa/2017/11/file_example_MP3_700KB.mp3"
)

"st.video"
st.video(
    "https://file-examples.com/storage/fe8d06553067e519a994eaa/2017/04/file_example_MP4_480_1_5MG.mp4"
)


"## Layouts and containers"

"st.columns"
a, b = st.columns(2)
a.write("column 1")
b.write("column 2")

c = st.container()
c.write("st.container")


@st.dialog("Test dialog")
def dialog():
    st.write("Hello there!")
    if st.button("Close", disabled=disabled):
        st.rerun()


if st.button("Open st.dialog"):
    dialog()

a = st.empty()
a.write("st.empty")

with st.expander("st.expander"):
    st.write("works!")

with st.popover("st.popover", disabled=disabled, help=help):
    st.write("works!")

st.sidebar.write("st.sidebar")

with st.sidebar:
    st.selectbox("st.selectbox sidebar", ["cat", "dog", "monkey", "snake", "bird"], disabled=disabled)
    st.button("st.button sidebar", disabled=disabled)
    st.checkbox("st.checkbox sidebar", True, disabled=disabled)
    st.info("st.info sidebar")
    st.expander("st.expander sidebar").write("works!")

"st.tabs"
tab_a, tab_b = st.tabs(["tab 1", "tab 2"])
tab_b.write("tab 1 content")
tab_a.write("tab 2 content")


"## Chat elements"

"st.chat_input"
if st.toggle("Show chat input at the bottom of the screen", False):
    st.chat_input(accept_file="multiple", disabled=disabled)
else:
    st.container().chat_input(accept_file="multiple", disabled=disabled)

"st.chat_message"
st.chat_message("assistant").write("Hello there!")

if st.button("Start st.status"):
    with st.status("Working on it...", expanded=True) as status:
        time.sleep(1)
        st.write("Some content...")
        time.sleep(1)
        st.write("Some content...")
        time.sleep(1)
        st.write("Some content...")
        status.update(label="Done!", state="complete")


if st.button("Start st.write_stream"):

    def stream():
        for i in ["hello", " streaming", " world"]:
            time.sleep(0.5)
            yield i

    st.write_stream(stream)


"## Status elements"
if st.button("st.progress"):
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
        time.sleep(0.05)

if st.button("st.spinner"):
    with st.spinner("Wait!", show_time=True):
        time.sleep(3)
        st.write("spinner works if you saw it!")

if st.button("st.toast"):
    st.toast("Hello there!", icon="🎈")

if st.button("st.balloons"):
    st.balloons()

if st.button("st.snow"):
    st.snow()

st.success("st.success")
st.success("st.success with icon", icon=":material/home:")
st.info("st.info")
st.info("st.info with icon", icon=":material/home:")
st.warning("st.warning")
st.warning("st.warning with icon", icon=":material/home:")
st.error("st.error")
st.error("st.error with icon", icon=":material/home:")
st.exception(RuntimeError("st.exception"))


"## Execution flow"

"st.fragment"


@st.fragment
def my_fragment():
    if st.button("Wait 1s inside the fragment"):
        time.sleep(1)


my_fragment()

if st.button("st.rerun"):
    st.rerun()

if st.button("st.stop"):
    st.stop()
    st.write("if you see this, st.stop does not work")

with st.form(key="tester"):
    "st.form"
    text_tester = st.text_input("Your text", disabled=disabled, help=help)
    st.form_submit_button("Submit", disabled=disabled, help=help)
st.write("Your text is:", text_tester)


st.write("## Utilities")

"st.help"
st.help(st.write)

st.write("## State Management")

"st.session_state"
if "foo" not in st.session_state:
    st.session_state["foo"] = "bar"
st.write(st.session_state)

if st.button("Add st.query_params"):
    st.query_params["foo"] = "bar"

"st.context.cookies"
st.write(st.context.cookies)

"st.context.headers"
st.write(st.context.headers)

"st.context.ip_address"
st.write(st.context.ip_address)

"st.context.is_embedded"
st.write(st.context.is_embedded)

"st.context.locale"
st.write(st.context.locale)

"st.context.theme.type"
st.write(st.context.theme.type)

"st.context.timezone"
st.write(st.context.timezone)

"st.context.timezone_offset"
st.write(st.context.timezone_offset)

"st.context.url"
st.write(st.context.url)
