
from jinja2.filters import F
import pandas
from bokeh.layouts import layout
from bokeh.models.glyphs import Circle
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import curdoc, show
from numpy import source
import pandas
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, Band, Toggle
from bokeh.models.annotations import Label, LabelSet, Span, BoxAnnotation
from bokeh.models.widgets import Select, Slider, RadioButtonGroup
from bokeh.layouts import gridplot

data = pandas.read_csv("/Users/tansubaktiran1/Dropbox/LEARNING/PYTHON/HOBBY/GURUR_TEST/DATA.csv", sep=",")

data = data.dropna()

source = ColumnDataSource(data)
#print(source.data)

f = figure(x_range = source.data["REGION"])

f.y_range = Range1d(start=0, end=11)
f.plot_height = 400
f.plot_width = 1200
f.yaxis.visible = False

f.vbar(x="REGION", top=10, bottom = 8, width=.8,color="red", fill_alpha=.8, legend_label="Total Contacted", source=source)
f.vbar(x="REGION", top=8, bottom = 6, width=.6, color="orangered", fill_alpha=.8, legend_label="Total Offered", source=source)
f.vbar(x="REGION", top=6, bottom = 4, width=.4, color="orange", fill_alpha=.8, legend_label="Total First Business", source=source)
f.vbar(x="REGION", top=4, bottom = 2, width=.2, color="limegreen", fill_alpha=.8, legend_label="Total Repeat Business", source=source)

labels1 = LabelSet(x="REGION", y=8, x_offset=30, y_offset=-6, 
background_fill_color= "navy", background_fill_alpha=.5, text_color="white", text="Contacted_perc", source=source)
labels2 = LabelSet(x="REGION", y=6, x_offset=22, y_offset=-6, 
background_fill_color= "navy", background_fill_alpha=.5, text_color="white", text="Offered_perc",  source=source)
labels3 = LabelSet(x="REGION", y=4, x_offset=16, y_offset=-6, 
background_fill_color= "navy", background_fill_alpha=.5, text_color="white", text="Business_perc",  source=source)
labels4 = LabelSet(x="REGION", y=2, x_offset=0, y_offset=-30, 
background_fill_color= "limegreen", background_fill_alpha=.8, text_color="white", text="Total_perc", source=source)
labels5 = LabelSet(x="REGION", y=9, x_offset=-15, y_offset=0, 
background_fill_color= None, background_fill_alpha=1,text_font_size="10pt", text_color="white", text="CONTACTED", source=source)
labels6 = LabelSet(x="REGION", y=7, x_offset=-10, y_offset=0, 
background_fill_color= None, background_fill_alpha=1,text_font_size="10pt", text_color="white", text="OFFERED", source=source)
labels7 = LabelSet(x="REGION", y=5, x_offset=-8, y_offset=0, 
background_fill_color= None, background_fill_alpha=1,text_font_size="10pt", text_color="white", text="BUSINESS", source=source)
labels8 = LabelSet(x="REGION", y=3, x_offset=-2, y_offset=0, 
background_fill_color= None, background_fill_alpha=1,text_font_size="10pt", text_color="white",  text="REPEAT BUSINESS", source=source)

f.add_layout(labels1)
f.add_layout(labels2)
f.add_layout(labels3)
f.add_layout(labels4)
f.add_layout(labels5)
f.add_layout(labels6)
f.add_layout(labels7)
f.add_layout(labels8)

f.legend.orientation = "horizontal"
f.legend.background_fill_alpha = 0.1
f.legend.margin = 2
f.legend.padding = 2
f.legend.click_policy="hide"
f.legend.location = "top_right"

mytext = Label(x=2, y=.25, text='Values at the bottom are the total conversion rates of the funnell-process', text_color="orangered")
f.add_layout(mytext)

f.title.text = "Sales Funnel Conversion Performances"
f.title.text_color = "#FF4500"
f.title.align = "left"
f.title.text_font = "Helvetica"
f.title.text_font_size = "16px"


funnel_layout = gridplot([[f]],plot_width=1200, plot_height=400)

curdoc().add_root(funnel_layout)

#show(f)