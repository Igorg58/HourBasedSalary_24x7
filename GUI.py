import os
import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
# import pandas as pd
from month_results import month_results

csv_path = ''
csv_data = []
entry_widgets = []
month = ''
year = ''


def update_csv_data(month, year):
    csv_path_templ = os.path.join('Config', 'config_{}_{}.csv')
    global csv_path
    csv_path = csv_path_templ.format(month, year)
    if not os.path.isfile(csv_path):
        with open(csv_path, 'w') as scv_fp:
            scv_fp.write('Date,Start,End,Eve Holiday,Holiday,Extra to planned\n')

    global csv_data
    csv_data = []
    required_row_len = 0
    required_rows_num = 20
    with open(csv_path, 'r') as csv_fp:
        for idx, line in enumerate(csv_fp):
            row = line.strip().split(',')
            if idx == 0:
                required_row_len = len(row)
            # Fill row to needed row_len with ''
            row += [''] * (required_row_len - len(row))
            print(row)  # debug
            csv_data.append(row)

        # Fill rows to required number
        current_rows_num = len(csv_data)
        for _ in range(required_rows_num - current_rows_num):
            csv_data.append([''] * required_row_len)
    print(f'Loaded CSV data: {csv_data}, len={len(csv_data)}')


def fill_entry_widgets():
    for i, row in enumerate(csv_data):
        entry_widgets_row = entry_widgets[i]
        for j, cell in enumerate(row):
            entry = entry_widgets_row[j]
            entry.delete(0, tk.END)
            entry.insert(tk.END, cell) # insert does not clear prev cell. Find another solution !


def update_month_dependencies():
    chosen_date = cal.get_displayed_month()  # tuple (<month>, <year>)
    # print(chosen_date, type(chosen_date))
    global month
    month = str(chosen_date[0])
    if len(month) == 1:
        month = '0' + month

    global year
    year = str(chosen_date[1])[2:]
    lbl_month.config(text=f"Month/Year: {month}/{year}")
    update_csv_data(month, year)


def get_month():
    update_month_dependencies()
    fill_entry_widgets()


def save_data():
    # Get updated data
    updated_data = []
    print('Updated data:')
    for entry_widgets_row in entry_widgets:
        row_values = []
        for entry in entry_widgets_row:
            cell_value = entry.get()
            row_values.append(cell_value)
        updated_data.append(row_values)
        print(row_values)

    with open(csv_path, 'w') as fp_csv:
        separator = ','
        for row in updated_data:
            line = separator.join(row).strip(separator)
            if len(line) == 0:
                continue
            fp_csv.write(line + '\n')


def save_and_run():
    # print('Not implemented yet')
    save_data()
    month_results(month, year)


root = tk.Tk()
root.title('Config file Editor')
root.geometry('600x700')


# Add Calendar
yshift = 4
cal = Calendar(root, selectmode='day', firstweekday='sunday', weekenddays=[6, 7])
cal.grid(row=0, column=0, padx=50, pady=20, columnspan=4, rowspan=yshift)

# Add Button and Label
btn_get_month = tk.Button(root, text="Get Month", command=get_month)
btn_get_month.grid(row=0, column=4, columnspan=2, padx=0, pady=0)

lbl_month = tk.Label(root, text="")
lbl_month.grid(row=1, column=4, columnspan=2)
update_month_dependencies()  # Date now is a default

# for idx in range(len(csv_data)):
#     root.columnconfigure(index=idx)

# frame = tk.Frame(master=root)  #, width=600, height=500, relief=tk.SOLID)  #, borderwidth=1, relief=tk.SOLID)

# Add table as Entry widgets and fill it with CSV data
i = j = 0
for i, row in enumerate(csv_data):
    # print(f'i = {i}')
    entry_widgets_row = []
    for j, cell in enumerate(row):
        entry = tk.Entry(root, width=15)
        # entry.insert(tk.END, cell)
        entry.grid(row=i+yshift, column=j, ipadx=0, ipady=0, padx=0, pady=0)
        entry_widgets_row.append(entry)
    entry_widgets.append(entry_widgets_row)
fill_entry_widgets()

# Add Buttons
btn_save = tk.Button(root, text="Save Data", command=save_data, width=10)
btn_save.grid(row=(i+1+yshift), column=1)

btn_run = tk.Button(root, text="Save & Run", command=save_and_run, width=10)
btn_run.grid(row=(i+1+yshift), column=j)

root.mainloop()
