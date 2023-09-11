#This file is used for plotting csv file.
#Date created: 09/05/2023
#Creator : John Raul Rebollos
#Used for documentation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter  # Import EngFormatter
import matplotlib.patches as patches
from datetime import datetime
import os
import getpass

def plot(
        df              =   None,
        csvfile         =   '',
        plot_type       =   'line',
        x               =   None,  
        y               =   None,  
        reference       =   None,
        color_group     =   '',
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
        filter          =   ''
        
        ):    

    



    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # ANSI escape code for red text
    red_text = "\033[91m"
    green_text = "\033[92m"

    # Reset ANSI escape code to default color
    reset_color = "\033[0m"

    # Print Messages
    print(green_text+"Plotting.........."+reset_color)

    if len(csvfile) == 0 and df.empty == True:
        print(red_text + "Error: No csvfile or data." + reset_color)
        return 
    if len(csvfile) > 0 and df.empty == False:
        print(red_text + "Error: Both csvfile and df input variables are entered. Please choose only one." + reset_color)
        return 
    if len(csvfile) == 0 and df.empty == False:
        pass
    if len(csvfile) > 0 and df.empty == True:
        df = pd.read_csv(csvfile)

    #Applying filtering
    if len(filter)>0:
        df = df.query(filter)   
        
    #List of colors for plotting    
    color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple', 'brown', 'pink', 'lime', 
                'indigo', 'gray', 'olive', 'teal','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'orange', 
                'purple', 'brown', 'pink', 'lime', 'indigo', 'gray', 'olive', 'teal','b', 'g', 'r', 
                'c', 'm', 'y', 'k', 'w', 'orange', 'purple', 'brown', 'pink', 'lime', 'indigo', 'gray', 
                'olive', 'teal','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple', 'brown', 'pink',
                'lime', 'indigo', 'gray', 'olive', 'teal','b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple', 
                'brown', 'pink', 'lime', 'indigo', 'gray', 'olive', 'teal']

    #Changing input variables to list type.
    if not isinstance(x, list):
        x_list = [x]
    else:
        x_list = x[:]
    if not isinstance(c, list):
        c = [c]
    else:
        c = c[:]
    if not isinstance(color_group, list):
        color_g_list = [color_group]
    else:
        color_g_list = color_group[:]

    if not isinstance(reference, list):
        reference_list = [reference]
    else:
        reference_list = reference[:]

    if file_name is not None:
        save = True    

    #Checking some possible errors
    if plot_type == "line_drift_percent" or plot_type == "line_drift":
        #for x_val in x_list:
        for iter in range(len(x_list)):
            if reference_list[iter] not in  df[x_list[iter]].unique():
                print(red_text + "The reference value is not within the range of x values." +reset_color)

        fig, axs = plt.subplots(2, len(x_list), figsize=figsize)  # 2 rows, 1 column   
        col_line_plot =len(x_list)
        
    if plot_type == "line"  or plot_type == "scatter" or plot_type == "scatter2p5":
        if len(x_list)%2 == 0:
            row_line_plot =  int(len(x_list)/2)
            col_line_plot =  2
            #print(row_line_plot,col_line_plot)
            fig, axs = plt.subplots(row_line_plot,col_line_plot, figsize=figsize)  # 2 rows, 1 column
        else:
            row_line_plot =  1
            col_line_plot =  len(x_list)
            fig, axs = plt.subplots(row_line_plot,col_line_plot, figsize=figsize)  # 2 rows, 1 column
            if len(x_list) == 1:
                axs = [axs]   

        
        # Create a list to store all combinations of rows and columns
        subplot_combinations = []
        # Generate all combinations of rows and columns
        for row in range(row_line_plot):
            for col in range(col_line_plot):
                subplot_combinations.append([row, col])
       
    
    for iter in range(len(x_list)): 
        #Getting the elements in color_group list
        color_g_val = color_g_list[iter]
        
        if not isinstance(color_g_val, list):
            color_g_val = [color_g_val]                    
        
        if plot_type == "line_drift_percent" or plot_type == "line_drift":
            reference_element= reference_list[iter]
            color_group_list    = []
            grouped_by_list = input_vars[:]
            
            #Prioritizing color_group elements in the list.
            for index, value in reversed(list(enumerate(color_g_val))):
                grouped_by_list.insert(0,grouped_by_list.pop(grouped_by_list.index(value)))

            #Removing the x axis in the grouped by list    
            grouped_by_list.pop(grouped_by_list.index(x_list[iter]))

            # Group the DataFrame by color_group to create separate data series for each elements value
            grouped = df.groupby(grouped_by_list)        

            for (sub_group), group in grouped:
                if plot_type == "line_drift_percent" or plot_type == "line_drift":
                    #Getting the reference values
                    reference_df = group[group[x_list[iter]] == reference_element]
                    reference_value = reference_df[y].values[0]  # Get the reference value
                    
                    if plot_type == "line_drift_percent":
                        delta_y = ((group[y] - reference_value) / reference_value) * 100
                    if plot_type == "line_drift":
                        delta_y = group[y] - reference_value
                
                combined_string =  ', '.join(str(item) for item in sub_group[0:len(color_g_val)])  
                

                if combined_string not in color_group_list:
                    color_group_list.append(combined_string)
                    if col_line_plot>1:
                        axs[0,iter].plot(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                        axs[1,iter].plot(group[x_list[iter]], delta_y,     label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].plot(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                        axs[iter+1].plot(group[x_list[iter]], delta_y,     label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                    
                else:
                    if col_line_plot>1:
                        axs[0,iter].plot(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])
                        axs[1,iter].plot(group[x_list[iter]], delta_y,  color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].plot(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])
                        axs[iter+1].plot(group[x_list[iter]], delta_y,  color= color_list[color_group_list.index(combined_string)])

            # Add labels and title for the first subplot
            if col_line_plot>1:
                axs[0,iter].set_xlabel(x_list[iter])
                axs[0,iter].set_ylabel(y)
                axs[0,iter].set_xscale(xscale)
                axs[0,iter].set_yscale(yscale)
                axs[0,iter].legend(loc='best')
                axs[0,iter].grid(True)

                # Add labels and title for the second subplot
                axs[1,iter].set_xlabel(x_list[iter])
                
                if plot_type == 'line_drift_percent':
                    axs[1,iter].set_ylabel(y+'_Drift'+"(%)")
                if plot_type == 'line_dri':
                    axs[1,iter].set_ylabel(y+'_Drift')
                axs[1,iter].set_xscale(xscale)
                axs[1,iter].set_yscale(yscale)
                axs[1,iter].legend(loc='best')
                axs[1,iter].grid(True)
                
                
            else:
                axs[iter].set_xlabel(x_list[iter])
                axs[iter].set_ylabel(y)
                axs[iter].set_xscale(xscale)
                axs[iter].set_yscale(yscale)
                axs[iter].legend(loc='best')
                axs[iter].grid(True)

                # Add labels and title for the second subplot
                axs[iter+1].set_xlabel(x_list[iter])
                if plot_type == 'line_drift_percent':
                    axs[iter+1].set_ylabel(y+'_Drift'+"(%)")
                if plot_type == 'line_drift':
                    axs[iter+1].set_ylabel(y+'_Drift')
                axs[iter+1].set_xscale(xscale)
                axs[iter+1].set_yscale(yscale)
                axs[iter+1].legend(loc='best')
                axs[iter+1].grid(True)

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

            color_group_list    = []
            grouped_by_list = input_vars[:]
            
            #Prioritizing color_group elements in the list.
            for index, value in reversed(list(enumerate(color_g_val))):
                grouped_by_list.insert(0,grouped_by_list.pop(grouped_by_list.index(value)))

            #Removing the x axis in the grouped by list    
            grouped_by_list.pop(grouped_by_list.index(x_list[iter]))

            # Group the DataFrame by color_group to create separate data series for each elements value
            grouped = df.groupby(grouped_by_list)        
            
            for (sub_group), group in grouped:
                combined_string =  ', '.join(str(item) for item in sub_group[0:len(color_g_val)])  
                

                if combined_string not in color_group_list:
                    color_group_list.append(combined_string)
                    if row_line_plot>1:
                        axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].plot(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].plot(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                    
                else:
                    if row_line_plot>1:
                        axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].plot(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].plot(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])

            # Add labels and title for the first subplot
            if row_line_plot>1:
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xlabel(x_list[iter])
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_ylabel(y)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xscale(xscale)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_yscale(yscale)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].legend(loc='best')
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].grid(True)
            else:
                axs[iter].set_xlabel(x_list[iter])
                axs[iter].set_ylabel(y)
                axs[iter].set_xscale(xscale)
                axs[iter].set_yscale(yscale)
                axs[iter].legend(loc='best')
                axs[iter].grid(True)


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

        if plot_type == "scatter":

            color_group_list    = []
            grouped_by_list = input_vars[:]
            
            #Prioritizing color_group elements in the list.
            for index, value in reversed(list(enumerate(color_g_val))):
                grouped_by_list.insert(0,grouped_by_list.pop(grouped_by_list.index(value)))

            #Removing the x axis in the grouped by list    
            grouped_by_list.pop(grouped_by_list.index(x_list[iter]))

            # Group the DataFrame by color_group to create separate data series for each elements value
            grouped = df.groupby(grouped_by_list)        
            
            for (sub_group), group in grouped:

                combined_string =  ', '.join(str(item) for item in sub_group[0:len(color_g_val)])  

                if combined_string not in color_group_list:
                    color_group_list.append(combined_string)
                    if row_line_plot>1:
                        axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].scatter(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].scatter(group[x_list[iter]], group[y],    label=f"{color_g_val}={combined_string}",  color= color_list[color_group_list.index(combined_string)])
                else:
                    if row_line_plot>1:
                        axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].scatter(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])
                    else:
                        axs[iter].scatter(group[x_list[iter]], group[y], color= color_list[color_group_list.index(combined_string)])

            # Add labels and title for the first subplot¨
           
            
            if row_line_plot>1:
                
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xlabel(x_list[iter])
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_ylabel(y)
                
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_yscale(yscale)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].legend(loc='best')
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].grid(True)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if group[x_list[iter]].dtype == object:
                    pass
                else:
                    axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xscale(xscale)
                    axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    
            else: 
                
                axs[iter].set_xlabel(x_list[iter])
                axs[iter].set_ylabel(y)
                axs[iter].legend(loc='best')
                axs[iter].grid(True)
                axs[iter].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if group[x_list[iter]].dtype == object:
                    pass
                else:
                    
                    axs[iter].set_xscale(xscale)
                    axs[iter].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[iter].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    
                    
        if plot_type == "scatter2p5":
            if row_line_plot>1:
                scatter = axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].scatter(df[x_list[iter]], df[y], c=df[c[iter]], cmap=cmap)
                colorbar = plt.colorbar(scatter, ax=axs[subplot_combinations[iter][0],subplot_combinations[iter][1]])
                colorbar.set_label(c[iter])  # Set the label for the colorbar

            else:
                scatter = axs[iter].scatter(df[x_list[iter]], df[y], c=df[c[iter]], cmap=cmap)
                colorbar = plt.colorbar(scatter, ax=axs[iter])
                colorbar.set_label(c[iter])  # Set the label for the colorbar

                
            # Add labels and title for the first subplot
            if row_line_plot>1:
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xlabel(x_list[iter])
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_ylabel(y)
                
                
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_yscale(yscale)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].legend(loc='best')
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].grid(True)
                axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if group[x_list[iter]].dtype == object:
                    pass
                else:
                    axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[subplot_combinations[iter][0],subplot_combinations[iter][1]].set_xscale(xscale)
            else:                
                axs[iter].set_xlabel(x_list[iter])
                axs[iter].set_ylabel(y)
                axs[iter].legend(loc='best')
                axs[iter].grid(True)
                axs[iter].yaxis.set_major_formatter(EngFormatter(useMathText=True))
                if df[x_list[iter]].dtype == object:
                    pass
                else:
                    axs[iter].xaxis.set_major_formatter(EngFormatter(useMathText=True))
                    axs[iter].set_xscale(xscale)   
    my_input_vars_str = []
    get_input_var = input_vars[:]
    

    for index_num in range(len(get_input_var)):  
        #print("None")
        my_input_vars_str.append(get_input_var[index_num] + "=" + str(df[get_input_var[index_num]].unique())) 
    
    
    
    username = os.getenv('USERNAME') or getpass.getuser()

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])

    title_str = []
    if show_date == True:
        title_str.append(f"Date created: {current_date}\n")
    if show_user == True:
        title_str.append(f"Created by: {username}\n")

    plt.suptitle(f"{''.join(title_str)}", wrap=True, fontsize=10, fontweight='normal', x=0.0, y=0.97, ha='left', va='center')
                    #bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2')) 
    if show_input_var == True:
        plt.annotate(f"Input variables: {my_input_vars_str}",xy=(0.5,0.03),fontweight='normal',xycoords='figure fraction',  # Use figure-relative coordinates
        fontsize=12,  # Adjust the font size as needed
        ha='center',  # Horizontal alignment ('center' for center alignment)
        wrap=True
        )

    #ax.text(0.95, 0.01, f"Date: {current_date}", transform=ax.transAxes, fontsize=10, ha="right")
    #plt.tight_layout()
    if fullscreen == True:
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()


    if save == True:
        plt.savefig(file_name, format= format)
        print('Vector file created: ' + file_name)
        plt.close()
    if show_plot == True:
        plt.show()
    
    print("Done..")





