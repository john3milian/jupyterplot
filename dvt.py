import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from ipywidgets import HBox
from ipywidgets import VBox
from matplotlib import pyplot
import matplotlib.pyplot as plt


def dvt(dataframe_object):
#LOADING DATA :-

    data_table = dataframe_object
#data_table = data_table[['gender','ssc_b','hsc_p','degree_p']]

##    !__data_types differentiator__!
    columns_dtype_dict = {}
    for i,j in zip(data_table.dtypes,data_table.columns):
        columns_dtype_dict[str(j)] = str(i)
    
#columns_dtype_dict    
##################################################################################################################

#Dropdown box -X-axis
    Dropdown_x = widgets.Dropdown(
        options= data_table.columns,
        value= data_table.columns[0],
        description='X-axis',
        disabled=False,
    )

#Dropdown box -Y-axis
    Dropdown_y = widgets.Dropdown(
        options= data_table.columns,
        value= data_table.columns[0],
        description='Y-axis',
        disabled=False,
    )

#alpha
#Dropdown_alpha = widgets.Dropdown(options= [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],value= 1,description='Transparency',disabled=False,)

#Slider -height
    Slider_height = widgets.IntSlider(
                min=3,
                max=15,
                step=1,
                description='Size:',
                value=5
    )
#Dropdown box -Graph type
    Dropdown_graff = widgets.Dropdown(
                 options= ['Categorical','Relational','Distribution'],
                 value= 'Categorical',
                 description= 'Graph',
                 disabled= False
                                 )
##__TYPE:__
#Dropdown box -Type of categorical_graph
    Dropdown_cat_graph_type = widgets.Dropdown(
                            options= ['strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar'],#, 'count'],
                            value= 'bar',
                            description='C-Type',
                            disabled=False,
    )

#Dropdown box -Type of relational_graph
    Dropdown_rel_graph_type = widgets.Dropdown(
                            options= ['scatter','line'],#, 'count'],
                            value= 'line',
                            description='R-Type',
                            disabled=False,
    )

#Dropdown box -Type of distribution_graph
    Dropdown_dis_graph_type = widgets.Dropdown(
                            options= ['hist','kde','ecdf'],#, 'count'],
                            value= 'hist',
                            description='D-Type',
                            disabled=False,
    )

#Dropdown box -theme_context
    Dropdown_theme_context = widgets.Dropdown(
                            options= ['notebook','paper','talk','poster'],
                            value= 'notebook',
                            description='context',
                            disabled=False,
    )

#Dropdown box -theme_style
    Dropdown_theme_style = widgets.Dropdown(
                            options= ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks'],
                            value= 'darkgrid',
                            description='style',
                            disabled=False,
    )

#Dropdown box -theme_palette
    Dropdown_theme_palette = widgets.Dropdown(
                            options= ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind'],
                            value= 'deep',
                            description='palette',
                            disabled=False,
    )

#Slider -theme_font_scale
    Slider_theme_font_scale = widgets.FloatSlider(
                            min=1,
                            max=5,
                            step=0.1,
                            description='font size',
                            value=1,
    )

#######################################################################################################################################################
#******************************************************************************************************************************************************
#######################################################################################################################################################

## Categorical_graph_creator:-
    def categorical_graff(x,y,kind,height):

        if columns_dtype_dict[x] == columns_dtype_dict[y]:
            print("Both axes can't be categorical or numeric for Categorical Plots. \nOne axis must be categorical and other a numeric.")
    
        else:
            if kind == 'count':
                y = None
        
            catplot = sns.catplot(data = data_table, kind = kind,#Dropdown_cat_graph_type.value,
                    x= x ,     #numeric 
                    y= y,  #categorical
                    #alpha= alpha,
                    #orient="h",
                    height= height,
                   legend_out=True)
            catplot.despine(left=True)
            return catplot

#sns.set_palette("Set1", 8, .75)

# Relational_graph_creator:-
    def relational_graff(x,y,kind,height):
   
        relplot = sns.relplot(data = data_table, kind = kind,
                          x = x,
                          y = y,
                          height = height,
                          )
        relplot.despine(left=True)
        return relplot
    
    
    def distribution_graff(x,y,kind,height):
    
    #if columns_dtype_dict[x] or columns_dtype_dict[y] == 'object':
    #    print("Both axes must be numeric.")
    #else:
            displot = sns.displot(data = data_table, kind = kind,
                              x = x,
                              y = y,
                              height = height,
                              )
            displot.despine(left=True)
            return displot
#######################################################################################################################################################
#******************************************************************************************************************************************************
#######################################################################################################################################################


#This changes the dropdown box of 'kind' for selected graph type
    Dropdown_graph_type = Dropdown_rel_graph_type

    def dropdown_graff_changer(graff_type):
        if Dropdown_graff.value == 'Relational':
            Dropdown_graph_type = Dropdown_rel_graph_type
            display(Dropdown_graph_type)
        elif Dropdown_graff.value == 'Distribution':
            Dropdown_graph_type = Dropdown_dis_graph_type
            display(Dropdown_graph_type)
        else:
            Dropdown_graph_type = Dropdown_cat_graph_type
            display(Dropdown_graph_type)

#################################################################################################################

#This plots graph for different kind and graph type combinations
    def graff_creator(Dropdown_graff,x,y,kind_rel,kind_cat,kind_dis,height,context,style,palette,font_size):

        sns.set_theme(context= context,
                  style= style, 
                  palette= palette,
                  font='Albertus', 
                  font_scale= font_size, 
                  color_codes=True, 
                  rc=None)
        if Dropdown_graff == 'Categorical':
            return categorical_graff(x,y,kind_cat,height)
    
        elif Dropdown_graff == 'Distribution':
            return distribution_graff(x,y,kind_dis,height)
    
        else:
            return relational_graff(x,y,kind_rel,height)
   
    

#################################################################################################################
    
#Type:
    option_out  =widgets.interactive_output(dropdown_graff_changer,
                                        {'graff_type': Dropdown_graff
                                           })
#Plot:
    out = widgets.interactive_output(graff_creator,                                
                                 {'x': Dropdown_x,
                                  'y': Dropdown_y, 
                                  'kind_rel': Dropdown_rel_graph_type, #
                                  'kind_cat': Dropdown_cat_graph_type,
                                  'kind_dis': Dropdown_dis_graph_type,
                                  #'alpha': Dropdown_alpha,
                                  'height': Slider_height,
                                  'context': Dropdown_theme_context,
                                  'style': Dropdown_theme_style,
                                  'palette': Dropdown_theme_palette,
                                  'font_size': Slider_theme_font_scale,
                                  'Dropdown_graff': Dropdown_graff,
                                                    })

    return widgets.VBox([widgets.HBox([Dropdown_x, Dropdown_y]),
              widgets.HBox([Dropdown_graff, option_out]),#Dropdown_graph_type]),
              widgets.HBox([Slider_height]),
              #widgets.HBox([header_theme]),
              widgets.HBox([Dropdown_theme_context]),
              widgets.HBox([Dropdown_theme_style]),
              widgets.HBox([Dropdown_theme_palette]),
              widgets.HBox([Slider_theme_font_scale]),
              widgets.HBox([out])
             ])