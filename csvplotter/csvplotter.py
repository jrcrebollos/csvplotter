#This file is used for plotting csv file.
#Date created: 09/05/2023
#Creator : John Raul Rebollos
#Used for documentation
import os
import getpass
import pandas   as pd
import numpy    as np
import matplotlib.pyplot    as plt
import matplotlib.patches   as patches
from datetime import datetime
from matplotlib.ticker import EngFormatter  # Import EngFormatter


def plot(
        df              =   pd.DataFrame(),
        csvfile         =   '',
        plot_type       =   'line',
        x               =   None,  
        y               =   None,  
        reference       =   None,
        color_group     =   [],
        input_vars      =   None,
        file_name       =   None, 
        xscale          =   'linear',
        yscale          =   'linear',
        show_plot       =   False, 
        figsize         =   (22, 20), 
        show_input_var  =   False,
        show_date       =   True, 
        show_user       =   True,
        c               =   None,
        cmap            =   'viridis',
        fullscreen      =   False,
        notation        =   "engineering",
        save            =   False,
        format          =   'svg',
        filter          =   '',
        linewidth       =   0.5,
        legend_fontsize =   8,
        yscale2         =   "linear",
        xscale2         =   "linear",
        watermark       =   False,
        markersize      =   10,
        ):    

    
    
    # Get the username
    username            = os.getenv('USERNAME') or getpass.getuser()

    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # ANSI escape code for red text
    red_text    = "\033[91m"
    green_text  = "\033[92m"
    orange_text = "\033[93m"
    yellow_text = "\033[93m"
    reset_color = "\033[0m"

    # Info, Warnings and Errors Messages
    INFO_MSG1   = green_text+"Plotting.........."+reset_color
    ERROR_MSG1  = red_text + "Error: No csvfile or data." + reset_color
    

    
    # Initialize input variables as lists
    c           = [c]           if not isinstance(c, list) else c[:]
    x_list      = [x]           if not isinstance(x, list) else x[:]
    y_list      = [y]           if not isinstance(y, list) else y[:]
    reference   = [reference]   if not isinstance(reference, list) else reference[:]
    color_group = [color_group] if not isinstance(color_group, list) else color_group[:]
    
    # Check if a file name is provided for saving the plot
    if file_name is not None:
        save = True    

    # Print Messages to know it is starting processing
    print(INFO_MSG1)

    # Check for errors and load data if needed
    if len(csvfile) == 0 and df.empty == True:
        print(ERROR_MSG1)
        return 
    if len(csvfile) > 0 and df.empty == False:
        print(red_text + "Error: Both csvfile and df input variables are entered. Please choose only one." + reset_color)
        return 
    if len(csvfile) == 0 and df.empty == False:
        pass
    if len(csvfile) > 0 and df.empty == True:
        df = pd.read_csv(csvfile)
        
    # Print warning messages,
    if plot_type == "line_drift" or plot_type == "line_drift_percent":
        if len(x) != len(color_group) and len(x) != len(reference):
            print(orange_text + "Warning: size of x are not equal with size of color_group. Please check if this is okay." + reset_color)
        if len(x) != len(reference):
            print(red_text + "Error: Size of x doesn't match with the size of reference. Please check!" + reset_color)
            return

    #Applying filtering
    if len(filter)>0:
        print("Applying filter...")
        df = df.query(filter)   
    print("Done loading csv file..")   
    #df = df.sort_values(by=list(df.columns), ascending=False)
    color_list = [
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    '#1f77b4',  # Blue
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#ff7f0e',  # Orange
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#9467bd',  # Purple
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',   # Teal
    ]

    color_list   = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF',
                    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF','#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#1a55FF', '#FF661A', '#0DFF42', '#FF0D42', '#00B4FF']
 
    markers_list = ['o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd',
                    'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd','o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']

    #Checking some possible errors
    if plot_type in ["line_drift_percent", "line_drift"]:
        for iter_x in range(len(x_list)):
            if reference[iter_x] not in  df[x_list[iter_x]].unique():
                print(red_text + "The reference value is not within the range of x values." + reset_color)
                return
        col_line_plot = len(x_list)
        row_line_plot = 2  

    if plot_type == "line"  or plot_type == "scatter" or plot_type == "scatter_colorbar":
        if len(x_list)%2 == 0:
            row_line_plot =  int(len(x_list)/2)
            col_line_plot =  2
        else:
            row_line_plot =  1
            col_line_plot =  len(x_list)

        # Create a list to store all combinations of rows and columns
        subplot_combinations = []
        # Generate all combinations of rows and columns
        for row in range(row_line_plot):
            for col in range(col_line_plot):
                subplot_combinations.append([row, col])

    #Creating a figure and how many rows and columns for the window
    fig, axs = plt.subplots(row_line_plot, col_line_plot, figsize=figsize)  # 2 rows, 1 column   

    if plot_type == "line"  or plot_type == "scatter" or plot_type == "scatter_colorbar":
        if not len(x_list)%2 == 0:
            if len(x_list) == 1:
                axs = [axs]

    #Main Loop
    for iter_x in range(len(x_list)):         
        color_group_list = []
        grouped_by_list = input_vars[:]
        color_g_val =   []
        color_g_val.clear()
        #Getting the elements in color_group list
        if color_group:
            if len(color_group) == 1 and len(color_group) != len(x_list):
                print(orange_text + "Warning: Mismatch in size of color_group and x.." + reset_color)     
                color_g_val = color_group[0]           
            elif len(color_group)== 0:
                color_g_val = color_group[0]
            elif len(color_group) == len(x_list):
                color_g_val = color_group[iter_x]
            if not isinstance(color_g_val, list):
                color_g_val = [color_g_val]  
            for index, value in reversed(list(enumerate(color_g_val))):
                #print(value)
                grouped_by_list.insert(0,grouped_by_list.pop(grouped_by_list.index(value)))   
        else:
            color_g_val = ['None']
        
        grouped_by_list.pop(grouped_by_list.index(x_list[iter_x]))
   
        # Group the DataFrame by color_group to create separate data series for each elements value
        grouped = df.groupby(grouped_by_list)  

        for (sub_group), group in grouped:
            
            combined_string =  ', '.join(str(item) for item in sub_group[0:len(color_g_val)])  
            
            if plot_type == "line_drift_percent" or plot_type == "line_drift":
                
                #Getting the reference values
                reference_element= reference[iter_x]
                reference_df = group[group[x_list[iter_x]] == reference_element]
                reference_value = reference_df[y].values[0]  # Get the reference value
                
                if plot_type == "line_drift_percent":
                    delta_y = ((group[y] - reference_value) / reference_value) * 100
                if plot_type == "line_drift":
                    delta_y = group[y] - reference_value

                if combined_string not in color_group_list:
                    if color_group:
                        
                        color_group_list.append(combined_string)
                        label = f"{color_g_val}={combined_string}"
                        label1 = label
                        color = color_list[color_group_list.index(combined_string)]
                        marker= markers_list[color_group_list.index(combined_string)]    
                    else:
                        color_group_list.append(combined_string)
                        color = 'b'
                        marker= markers_list[0]
                        label = y
                        if plot_type == 'line_drift_percent':
                            label1 = y + "_Drift(%)" 
                        if plot_type == 'line_drift':
                            label1 = y + "_Drift" 
                        

                    if col_line_plot>1:
                        axs[0,iter_x].plot(group[x_list[iter_x]], group[y],    label=label,  color= color, marker= marker ,markersize = markersize,linewidth=linewidth)
                        axs[1,iter_x].plot(group[x_list[iter_x]], delta_y,     label=label1,  color= color, marker= marker, linewidth=linewidth)
                    else:
                        axs[iter_x].plot(group[x_list[iter_x]], group[y],      label=label,  color= color, marker= marker,markersize = markersize, linewidth=linewidth)
                        axs[iter_x+1].plot(group[x_list[iter_x]], delta_y,     label=label1,  color= color, marker= marker, markersize = markersize,linewidth=linewidth)
                    
                else:
                    if col_line_plot>1:
                        axs[0,iter_x].plot(group[x_list[iter_x]],   group[y], color= color, marker= marker,markersize = markersize, linewidth=linewidth)
                        axs[1,iter_x].plot(group[x_list[iter_x]],   delta_y,  color= color, marker= marker, markersize = markersize,linewidth=linewidth)
                    else:
                        axs[iter_x].plot(group[x_list[iter_x]],     group[y], color= color, marker= marker,markersize = markersize, linewidth=linewidth)
                        axs[iter_x+1].plot(group[x_list[iter_x]],   delta_y,  color= color, marker= marker,markersize = markersize, linewidth=linewidth)

                # Add labels and title for the first subplot
                if col_line_plot>1:
                    axs[0,iter_x].set_xlabel(x_list[iter_x])
                    axs[0,iter_x].set_ylabel(y)
                    axs[0,iter_x].set_xscale(xscale)
                    axs[0,iter_x].set_yscale(yscale)
                    axs[0,iter_x].legend(loc='best', fontsize=legend_fontsize)
                    axs[0,iter_x].grid(True)
                    axs[0,iter_x].minorticks_on()
                    axs[0,iter_x].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                    # Add labels and title for the second subplot
                    axs[1,iter_x].set_xlabel(x_list[iter_x])
                    
                    if plot_type == 'line_drift_percent':
                        axs[1,iter_x].set_ylabel(y+'_Drift'+"(%)")
                    if plot_type == 'line_drift':
                        axs[1,iter_x].set_ylabel(y+'_Drift')
                    axs[1,iter_x].set_xscale(xscale2)
                    axs[1,iter_x].set_yscale(yscale2)
                    axs[1,iter_x].legend(loc='best', fontsize=legend_fontsize)
                    axs[1,iter_x].grid(True)
                    axs[1,iter_x].minorticks_on()
                    axs[1,iter_x].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                    
                else:
                    axs[iter_x].set_xlabel(x_list[iter_x])
                    axs[iter_x].set_ylabel(y)
                    axs[iter_x].set_xscale(xscale)
                    axs[iter_x].set_yscale(yscale)
                    axs[iter_x].legend(loc='best', fontsize=legend_fontsize)
                    axs[iter_x].grid(True)
                    axs[iter_x].minorticks_on()
                    axs[iter_x].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')

                    # Add labels and title for the second subplot
                    axs[iter_x+1].set_xlabel(x_list[iter_x])
                    if plot_type == 'line_drift_percent':
                        axs[iter_x+1].set_ylabel(y+'_Drift'+"(%)")
                    if plot_type == 'line_drift':
                        axs[iter_x+1].set_ylabel(y+'_Drift')
                    axs[iter_x+1].set_xscale(xscale2)
                    axs[iter_x+1].set_yscale(yscale2)
                    axs[iter_x+1].legend(loc='best', fontsize=legend_fontsize)
                    axs[iter_x+1].grid(True)
                    axs[iter_x+1].minorticks_on()
                    axs[iter_x+1].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                if notation == "engineering":
                    if col_line_plot > 1:
                        for row in axs:
                            for ax in row:
                                ax.yaxis.set_major_formatter(EngFormatter(useMathText=True))
                                ax.xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    else:
                        for ax in axs:
                            ax.yaxis.set_major_formatter(EngFormatter(useMathText=True))
                            ax.xaxis.set_major_formatter(EngFormatter(useMathText=True))
                            #ax.text(0.95, 0.01, f"Date: {current_date}", transform=ax.transAxes, fontsize=10, ha="right")
            if plot_type == "line":          
                if combined_string not in color_group_list:
                    if color_group:
                        if color_group[iter_x]:
                            color_group_list.append(combined_string)
                            label = f"{color_g_val}={combined_string}"
                            label1 = label
                            color = color_list[color_group_list.index(combined_string)]
                            marker= markers_list[color_group_list.index(combined_string)] 
                    else:
                        color_group_list.append(combined_string)
                        marker= markers_list[0]
                        color = 'b'
                        label = y
                        if plot_type == 'line_drift_percent':
                            label1 = y + "_Drift(%)" 
                        if plot_type == 'line_drift':
                            label1 = y + "_Drift" 

                    if row_line_plot>1:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].plot(group[x_list[iter_x]], group[y],    label=label,  color=color, linewidth=linewidth, marker= marker, markersize = markersize )
                    else:
                        axs[iter_x].plot(group[x_list[iter_x]], group[y],    label=f"{color_g_val}={combined_string}",  color= color, linewidth=linewidth, marker= marker, markersize = markersize )
                    
                else:
                    if row_line_plot>1:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].plot(group[x_list[iter_x]], group[y], color=color, linewidth=linewidth, marker= marker, markersize = markersize )
                    else:
                        axs[iter_x].plot(group[x_list[iter_x]], group[y], color=color, linewidth=linewidth, marker= marker, markersize = markersize )

            # Add labels and title for the first subplot
                if row_line_plot>1:
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xlabel(x_list[iter_x])
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_ylabel(y)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xscale(xscale)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_yscale(yscale)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].legend(loc='best', fontsize=legend_fontsize,framealpha=0.4)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(True)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].minorticks_on()
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                    
                else:
                    axs[iter_x].set_xlabel(x_list[iter_x])
                    axs[iter_x].set_ylabel(y)
                    axs[iter_x].set_xscale(xscale)
                    axs[iter_x].set_yscale(yscale)
                    axs[iter_x].legend(loc='best', fontsize=legend_fontsize,framealpha=0.4)
                    axs[iter_x].grid(True)
                    axs[iter_x].minorticks_on()
                    axs[iter_x].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')


                if notation == "engineering":
                    if row_line_plot > 1:
                        for row in axs:
                            for ax in row:
                                ax.yaxis.set_major_formatter(EngFormatter(useMathText=True))
                                ax.xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    else:
                        for ax in axs:
                            ax.yaxis.set_major_formatter(EngFormatter(useMathText=True))
                            ax.xaxis.set_major_formatter(EngFormatter(useMathText=True))
                            #ax.text(0.95, 0.01, f"Date: {current_date}", transform=ax.transAxes, fontsize=10, ha="right")
                #print(df)
            if plot_type == "scatter":

                if combined_string not in color_group_list:

                    color_group_list.append(combined_string)
                    label = f"{color_g_val}={combined_string}"
                    color = color_list[color_group_list.index(combined_string)]
                    marker= markers_list[color_group_list.index(combined_string)]

                    if row_line_plot>1:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].scatter(group[x_list[iter_x]], group[y],    label=label,  color= color, marker = marker, s = markersize)
                    else:
                        axs[iter_x].scatter(group[x_list[iter_x]], group[y],    label=f"{color_g_val}={combined_string}",  color= color , marker = marker, s = markersize)
                else:
                    if row_line_plot>1:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].scatter(group[x_list[iter_x]], group[y], color= color, marker = marker, s = markersize)
                    else:
                        axs[iter_x].scatter(group[x_list[iter_x]], group[y], color= color, marker = marker, s = markersize)

                # Add labels and title for the first subplot¨
            
                
                if row_line_plot>1:
                    
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xlabel(x_list[iter_x])
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_ylabel(y)
                    
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_yscale(yscale)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].legend(loc='best', fontsize=legend_fontsize,framealpha=0.4)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(True)
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].minorticks_on()
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                    if group[x_list[iter_x]].dtype == object:
                        pass
                    else:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xscale(xscale)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                        
                else: 
                    
                    axs[iter_x].set_xlabel(x_list[iter_x])
                    axs[iter_x].set_ylabel(y)
                    axs[iter_x].set_yscale(yscale)
                    axs[iter_x].legend(loc='best', fontsize=legend_fontsize ,framealpha=0.4)
                    axs[iter_x].grid(True)
                    axs[iter_x].minorticks_on()
                    axs[iter_x].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[iter_x].grid(which='minor', linestyle='--', linewidth=0.5, color='gray')
                    if group[x_list[iter_x]].dtype == object:
                        pass
                    else:
                        
                        axs[iter_x].set_xscale(xscale)
                        axs[iter_x].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                        axs[iter_x].xaxis.set_major_formatter(EngFormatter(useMathText=True))        
        
        if plot_type == "scatter_colorbar":
            if len(c) == 1:
                c_val = c[0]
            else:
                c_val = c[iter_x]
            if row_line_plot>1:
                scatter = axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].scatter(df[x_list[iter_x]], df[y], c=df[c_val], cmap=cmap)
                colorbar = plt.colorbar(scatter, ax=axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]])
                colorbar.set_label(c_val)  # Set the label for the colorbar

            else:
                scatter = axs[iter_x].scatter(df[x_list[iter_x]], df[y], c=df[c_val], cmap=cmap)
                colorbar = plt.colorbar(scatter, ax=axs[iter_x])
                colorbar.set_label(c_val)  # Set the label for the colorbar

                
            # Add labels and title for the first subplot
            if row_line_plot>1:
                axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xlabel(x_list[iter_x])
                axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_ylabel(y)
                
                
                axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_yscale(yscale)
                
                axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(True)
                axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if group[x_list[iter_x]].dtype == object:
                    pass
                else:
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xscale(xscale)
                #axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].legend(loc='best')
            else:                
                axs[iter_x].set_xlabel(x_list[iter_x])
                axs[iter_x].set_ylabel(y)
                
                axs[iter_x].grid(True)
                axs[iter_x].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if df[x_list[iter_x]].dtype == object:
                    pass
                else:
                    axs[iter_x].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[iter_x].set_xscale(xscale)  
                #axs[iter_x].legend(loc='best') 
    my_input_vars_str = []
    get_input_var = input_vars[:]
    

    for index_num in range(len(get_input_var)):  
        #print("None")
        my_input_vars_str.append(get_input_var[index_num] + "=" + str(df[get_input_var[index_num]].unique())) 

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])

    title_str = []
    if show_date == True:
        title_str.append(f"Date created: {current_date}\n")
    if show_user == True:
        title_str.append(f"Created by: {username}\n")
    
    plt.suptitle(f"{''.join(title_str)}", wrap=True, fontsize=10, fontweight='normal', x=0.0, y=0.96, ha='left', va='center')
                    #bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2')) 
    if show_input_var == True:
        plt.annotate(f"Input variables: {my_input_vars_str}",xy=(0.5,0.03),fontweight='normal',xycoords='figure fraction',  # Use figure-relative coordinates
        fontsize=12,  # Adjust the font size as needed
        ha='center',  # Horizontal alignment ('center' for center alignment)
        wrap=True
        )
    if watermark == True:
        #plt.text(0.8, 1, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2,ha='center', va='center', rotation=30)
        #plt.text(0.5, 0.5, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2,ha='center', va='center', rotation=30)
        #plt.text(0.2, 0, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)    
        plt.figtext(0.8, 0.6, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
        plt.figtext(0.5, 0.5, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
        plt.figtext(0.2, 0.4, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
    if fullscreen == True:
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
    if save == True:
        plt.savefig(file_name, format= format)
        print('Vector file created: ' + file_name)
    if show_plot == True:
        plt.show()
    else:
        plt.close()
    print("Complete!")





