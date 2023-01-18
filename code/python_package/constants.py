# --------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Constants------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# 1. folders and files name -----------------------------------------------------------------------------/
BROWSER             = "chrome"
PROCESSING_TOOL     = "html.parser"



MARS_NEWS_URL       = "https://static.bc-edx.com/data/web/mars_news/index.html"
MARS_TEMP_URL       = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"
OUTPUT_PATH         = "../Output/"


lng                 = "longitude"
lat                 = "latitude"
time_length         = "12 month"         
tobs                = "Temperatures Observed"
station             = "Station"
freq                = "Frequency"
prcp                = "Precipitation"
MAP_NAME            = "Honolulu"
# -------------------------------------------------------------------------------------------------------/

# 2. defining directories -------------------------------------------------------------------------------/
db_path             = "sqlite:///../Resources/hawaii.sqlite"
# -------------------------------------------------------------------------------------------------------/

# 3. station location (station_location.py) constants ---------------------------------------------------/
SESSION_COLUMN_NAME = ["station", "name", "latitude", "longitude", "elevation", "number_of_colected_data"]

# 4. plot -----------------------------------------------------------------------------------------------/

# a-4) map plot constants

MAP_WEIGTH          = 550
MAP_HEIGHT          = 475
MAP_TOOLS           = "hover"
MARKER_SHAPE        = "triangle_dot"
MARKER_SIZE         = 15
MARKER_FILL_COLOR   = "red"
MARKER_FILL_ALPHA   = 0.5
MARKER_LINE_COLOR   = "black"
MARKER_LINE_ALPHA   = 0.8

# b-4) histogram and line constants
title_font_size     = 15
label_font_size     = 12
ticks_font_size     = 10
legend_font_size    = 10
font_weight         = "bold"
plt_fig_higth       = 10
plt_fig_width       = 8
plt_color           = "tab:blue"
legend_location     = "best"
his_x_label         = "Temperature"
his_y_label         = "Frequency"
line_x_label        = "Date (yyyy-mm-dd)"
line_y_label        = "Inches"
line_width          = 1 
# -------------------------------------------------------------------------------------------------------/


