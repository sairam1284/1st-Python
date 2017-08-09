from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

starting = datetime.datetime(2016, 1, 1)
ending = datetime.datetime(2016, 1, 15)
df = data.DataReader(name="AAPL", data_source="yahoo", start = starting, end= ending)

def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Increase"
    return value
df["Status"] = [inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
df["Height"] = abs(df.Close - df.Open)
hours_12 = 12*60*60*1000
mids = (df.Open + df.Close)/2
inc = df.Close > df.Open
dec = df.Open > df.Close

# print(df)
p = figure(x_axis_type='datetime', width = 600, height=300, title="Candelstick Chart", responsive=True)
p.segment(df.index, df.High, df.index, df.Low, color="Black")
p.rect(df.index[inc], mids[inc], hours_12, df.Height[inc], fill_color = "green", line_color="black")
p.rect(df.index[dec], mids[dec], hours_12, df.Height[dec], fill_color = "red", line_color="black")
p.grid.grid_line_alpha = 0.3

# show(p)
script1, div1 = components(p)
cdn_js = CDN.js_files
cdn_css = CDN.css_files
