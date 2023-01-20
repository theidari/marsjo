# --------------------------------------------------------------------------------------------------------
# -------------------- All libraries, variables and functions are defined in this fil --------------------
# --------------------------------------------------------------------------------------------------------

# 1. libraries ------------------------------------------------------------------------------------------/
from python_package.constants import * # constants

# a-1) Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup

# b-1) import relevant libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# -------------------------------------------------------------------------------------------------------/

# 2. function definition --------------------------------------------------------------------------------/
# a-2) line graph
def simple_line (df,param,label=[],addline=[]):
    # data length
    length=len(df.index)
    # plot size
    plt.figure(figsize=(LINE_PLT_WIDTH,LINE_PLT_HIGHT))
    # plot main describtion
    plt.plot(df.index, df[param] , color = LINE_COLOR, linewidth=LINE_WIDTH)
    # ticks definitions
    plt.xticks(np.arange(0,length,50), rotation = 90, rotation_mode = 'anchor',ha = 'right', fontsize=LINE_TICKS_FONT_SIZE)
    plt.yticks(fontsize=LINE_TICKS_FONT_SIZE)
    # lim definitions
    plt.xlim(df.index[0],df.index[-1])
    # label definitions
    plt.xlabel(label[0], fontsize=LINE_LABEL_FONT_SIZE)
    plt.ylabel(label[1], fontsize=LINE_LABEL_FONT_SIZE)
    # title definitions
    plt.title(label[1]+" per "+label[0], fontsize=LINE_TITLE_FONT_SIZE, pad=+20)
    # legend definitions
    plt.legend([label[1]], loc = LEGEND_LOCATION, fontsize=LINE_LEGEND_FONT_SIZE)
    # vertical_line
    if len(addline)==0:
        # plt save
        plt.savefig(OUTPUT_PATH+label[1]+" per "+label[0]+".png",dpi=300, bbox_inches='tight')
        return plt.show()
    else:
        if addline[0]=="v":
            for addline_index in addline[1:]:
                plt.axvline(x=addline_index,color='black',linestyle='dashed',linewidth=LINE_WIDTH)
        elif addline[0]=="h":
            for addline_index in addline[1:]:
                plt.axhline(y=addline_index,color='black',linestyle='dashed',linewidth=LINE_WIDTH)
        # plt save
        plt.savefig(OUTPUT_PATH+label[1]+" per "+label[0]+".png",dpi=300, bbox_inches='tight')
        return plt.show()

# a-3) bar chart
# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
def simple_bar (df,param,x_name,y_name):
    # plot size
    plt.figure(figsize=(PLT_WIDTH,PLT_HIGHT))
    # plot main describtion
    plt.bar(df.index, df[param] , width=BAR_WIDTH, color=BAR_COLOR, alpha=1, align="center")
    plt.xticks(rotation='horizontal', fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.title(y_name+"_per_"+x_name, fontsize=TITLE_FONT_SIZE)
    plt.xlabel(x_name, fontsize=LABEL_FONT_SIZE)
    plt.ylabel(y_name, fontsize=LABEL_FONT_SIZE)
    plt.legend([y_name], loc = LEGEND_LOCATION, fontsize=LEGEND_FONT_SIZE)
    # plt save
    plt.savefig(OUTPUT_PATH+y_name+"_per_"+x_name+".png",dpi=300, bbox_inches="tight")
    return plt.show()
# -------------------------------------------------------------------------------------------------------/
def bar_chart (df,param,error,x_name,y_name):
    # plot size
    plt.figure(figsize=(PLT_WIDTH,PLT_HIGHT))
    # plot main describtion
    plt.bar(df.index, df[param] , yerr=error, width=BAR_WIDTH, color=BAR_COLOR, alpha=1, align="center", ecolor='k', capsize=2)
    plt.xticks(rotation='horizontal', fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.title(y_name+"_per_"+x_name, fontsize=TITLE_FONT_SIZE)
    plt.xlabel(x_name, fontsize=LABEL_FONT_SIZE)
    plt.ylabel(y_name, fontsize=LABEL_FONT_SIZE)
    plt.legend([y_name], loc = LEGEND_LOCATION, fontsize=LEGEND_FONT_SIZE)
    # plt save
    plt.savefig(OUTPUT_PATH+y_name+"_per_"+x_name+".png",dpi=300, bbox_inches="tight")
    return plt.show()
