#Date : 2024-10-27
#Creator : John Raul Rebollos
#Description: This script is use for plotting csv file, color grouping, y vs y
#


import pandas as pd
import os
import getpass
from datetime import datetime
import color_list
import marker_list
import matplotlib.pyplot    as plt
import matplotlib.patches   as patches
from matplotlib.ticker import EngFormatter  # Import EngFormatter

class csvPlotter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.read_csv()
        self.plot_type      =   "line"
        self.x              =   None  
        self.y              =   None  
        self.y_ref          =   None
        self.color_group    =   []
        self.input_vars     =   None
        self.xscale         =   "linear"
        self.yscale         =   "linear"
        self.show_plot      =   True 
        self.figsize        =   (10, 10)
        self.show_input_var =   True
        self.show_date      =   True 
        self.show_user      =   True
        self.save_name      =   "plot"
        #For colorbar
        self.c              =   None
        self.cmap           =   "viridis"
        # end of colorbar
        self.fullscreen     =   False
        self.notation       =   "engineering"
        self.save           =   False
        self.format         =   "svg"
        self.filter         =   ""
        self.linewidth      =   0.5
        self.legend_fontsize=   8
        self.yscale2        =   "linear"
        self.xscale2        =   "linear"
        self.watermark      =   False
        self.username       =   os.getenv('USERNAME') or getpass.getuser()
        self.date           =   datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.markers        =   marker_list.markers
        self.colors         =   color_list.colors
        self.markersize     = 10
        
 
    def read_csv(self):
        try:
            # Read only the header row of the file
            self.data = pd.read_csv(self.file_path)
            # Store column names
            self.columns = list(self.data.columns)
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: There was an error parsing the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def plot(self):
            # ANSI escape code for red text
        red_text    = "\033[91m"
        green_text  = "\033[92m"
        orange_text = "\033[93m"
        yellow_text = "\033[93m"
        reset_color = "\033[0m"
        #Checking some possible errors
        if self.plot_type in ["line","scatter", "scatter_colorbar"]:
            if len(self.x)%2 == 0:
                row_line_plot =  int(len(self.x)/2)
                col_line_plot =  2
            else:
                row_line_plot =  1
                col_line_plot =  len(self.x)
            # Create a list to store all combinations of rows and columns
            subplot_combinations = []
            # Generate all combinations of rows and columns
            for row in range(row_line_plot):
                for col in range(col_line_plot):
                    subplot_combinations.append([row, col])
        #Creating a figure and how many rows and columns for the window
        fig, axs = plt.subplots(row_line_plot, col_line_plot, figsize=self.figsize)  # 2 rows, 1 column   
        #Main Loop
        for iter_x in range(len(self.x)):         
            color_group_list = []
            grouped_by_list = self.input_vars[:]
            color_g_val =   []
            color_g_val.clear()
            #Getting the elements in color_group list
            if self.color_group:
                if len(self.color_group) == 1 and len(self.color_group) != len(self.x):
                    print(orange_text + "Warning: Mismatch in size of color_group and x.." + reset_color)     
                    color_g_val = self.color_group[0]           
                elif len(self.color_group)== 0:
                    color_g_val = self.color_group[0]
                elif len(self.color_group) == len(self.x):
                    color_g_val = self.color_group[iter_x]
                if not isinstance(color_g_val, list):
                    color_g_val = [color_g_val]  
                for index, value in reversed(list(enumerate(color_g_val))):
                    #print(value)
                    grouped_by_list.insert(0,grouped_by_list.pop(grouped_by_list.index(value)))   
            else:
                color_g_val = ['None']
            try:
                grouped_by_list.pop(grouped_by_list.index(self.x[iter_x]))
            except:
                None
            # Group the DataFrame by color_group to create separate data series for each elements value
            grouped = self.data.groupby(grouped_by_list)  

            for (sub_group), group in grouped:
                
                combined_string =  ', '.join(str(item) for item in sub_group[0:len(color_g_val)])  
                if self.plot_type == "line":          
                    if combined_string not in color_group_list:
                        if self.color_group:
                            if self.color_group[iter_x]:
                                color_group_list.append(combined_string)
                                label = f"{color_g_val}={combined_string}"
                                label1 = label
                                color = self.colors[color_group_list.index(combined_string)]
                                marker= self.markers[color_group_list.index(combined_string)] 
                        else:
                            color_group_list.append(combined_string)
                            marker= self.markers[0]
                            color = 'b'
                            label = self.y
                            if self.plot_type == 'line_drift_percent':
                                label1 = self.y + "_Drift(%)" 
                            if self.plot_type == 'line_drift':
                                label1 = self.y + "_Drift" 

                        if row_line_plot>1:
                            axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].plot(group[self.x[iter_x]], group[y],    label=label,  color=color, linewidth=linewidth, marker= marker, markersize = self.markersize )
                        else:
                            axs[iter_x].plot(group[self.x[iter_x]], group[self.y],    label=f"{color_g_val}={combined_string}",  color= color, linewidth=self.linewidth, marker= marker, markersize = self.markersize )
                        
                    else:
                        if row_line_plot>1:
                            axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].plot(group[self.x[iter_x]], group[self.y], color=color, linewidth=self.linewidth, marker= marker, markersize = self.markersize )
                        else:
                            axs[iter_x].plot(group[self.x[iter_x]], group[self.y], color=color, linewidth=self.linewidth, marker= marker, markersize = self.markersize )

                # Add labels and title for the first subplot
                    if row_line_plot>1:
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xlabel(self.x[iter_x])
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_ylabel(self.y)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_xscale(self.xscale)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].set_yscale(self.yscale)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].legend(loc='best', fontsize=self.legend_fontsize,framealpha=0.4)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(True)
                        axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].minorticks_on()
                        #axs[subplot_combinations[iter_x][0],subplot_combinations[iter_x][1]].grid(which='minor', linestyle='--', self.linewidth=0.5, color='gray')
                        
                    else:
                        axs[iter_x].set_xlabel(self.x[iter_x])
                        axs[iter_x].set_ylabel(self.y)
                        axs[iter_x].set_xscale(self.xscale)
                        axs[iter_x].set_yscale(self.yscale)
                        axs[iter_x].legend(loc='best', fontsize=self.legend_fontsize,framealpha=0.4)
                        axs[iter_x].grid(True)
                        axs[iter_x].minorticks_on()
                        #axs[iter_x].grid(which='minor', linestyle='--', self.linewidth=0.5, color='gray')


                    if self.notation == "engineering":
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
        my_input_vars_str = []
        get_input_var = self.input_vars[:]
        

        for index_num in range(len(get_input_var)):  
            #print("None")
            my_input_vars_str.append(get_input_var[index_num] + "=" + str(self.data[get_input_var[index_num]].unique())) 

        plt.tight_layout(rect=[0, 0.05, 1, 0.96])

        title_str = []
        if self.show_date == True:
            title_str.append(f"Date created: {self.date}\n")
        if self.show_user == True:
            title_str.append(f"Created by: {self.username}\n")
        
        plt.suptitle(f"{''.join(title_str)}", wrap=True, fontsize=10, fontweight='normal', x=0.0, y=0.96, ha='left', va='center')
                        #bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2')) 
        if self.show_input_var == True:
            plt.annotate(f"Input variables: {my_input_vars_str}",xy=(0.5,0.03),fontweight='normal',xycoords='figure fraction',  # Use figure-relative coordinates
            fontsize=12,  # Adjust the font size as needed
            ha='center',  # Horizontal alignment ('center' for center alignment)
            wrap=True
            )
        if self.watermark == True:
            #plt.text(0.8, 1, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2,ha='center', va='center', rotation=30)
            #plt.text(0.5, 0.5, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2,ha='center', va='center', rotation=30)
            #plt.text(0.2, 0, 'Nordicsemiconductor', transform=ax.transAxes,fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)    
            plt.figtext(0.8, 0.6, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
            plt.figtext(0.5, 0.5, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
            plt.figtext(0.2, 0.4, 'Nordicsemiconductor', fontsize=40, color='gray', alpha=0.2, ha='center', va='center', rotation=30)
        if self.fullscreen == True:
            manager = plt.get_current_fig_manager()
            manager.window.showMaximized()
        if self.save == True:
            plt.savefig(self.save_name + "." + self.format, format= self.format)
            print('Vector file created: ' + self.save_name)
        if self.show_plot == True:
            plt.show()
        else:
            plt.close()
        print("Complete!")

# Usage example
file_path = "csvplotter/csvplotter/timing_syson.csv"  # Replace with your CSV file path
plot1 = csvPlotter(file_path)

print(plot1.columns)
plot1.x=["vdd_dut","temperature"]
plot1.input_vars = ['ConfigView', 'vdd_dut', 'temperature', 'nod22_mos.scs', 'nod22_bip_dio.scs', 'nod22_noise.scs', 'nod22_pre_simu.scs', 'nod22_cap.scs', 'nod22_res.scs']
plot1.y="PropagationDelayRising"
plot1.color_group=["temperature","temperature"]
plot1.save = True
plot1.plot()
#print(reader.columns)
