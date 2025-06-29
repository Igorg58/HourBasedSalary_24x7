import os
import tkinter as tk
# import pandas as pd

csv_path = os.path.join('Config', 'config_06_25.csv')
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


root = tk.Tk()
root.title('Config Editor')

#--------
root.geometry('600x500')

i = 0
j = 0
entry_widgets = []
for i, row in enumerate(csv_data):
    # print(f'i = {i}')
    entry_widgets_row = []
    for j, cell in enumerate(row):
        # print(f'j = {j}')
        entry = tk.Entry(root, width=15)
        entry.insert(tk.END, cell)
        # print(f'i = {i}, j = {j}')
        entry.grid(row=i, column=j, ipadx=0, ipady=0, padx=0, pady=0)
        entry_widgets_row.append(entry)
        # entry.grid_forget()
    entry_widgets.append(entry_widgets_row)
print(f'')


# def get_data():
    # print('Updated data:')
    # for entry_widgets_row in entry_widgets:
    #     row_values = []
    #     for entry in entry_widgets_row:
    #         cell_value = entry.get()
    #         row_values.append(cell_value)
    #     updated_data.append(row_values)
    #     print(row_values)


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


def run():
    print('Not implemented yet')


# Add Buttons and Label
# btn_get = tk.Button(root, text="Get Data", command=get_data)
# btn_get.grid(row=(i+1), column=1)

btn_save = tk.Button(root, text="Save Data", command=save_data)
btn_save.grid(row=(i+1), column=1)

btn_run = tk.Button(root, text="Run", command=run)
btn_run.grid(row=(i+1), column=j)

#-------

root.mainloop()
