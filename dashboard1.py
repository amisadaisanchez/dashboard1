#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pathlib import Path
import pandas as pd
from taipy.gui import Gui
import taipy.gui.builder as tgb
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()

# accessing and printing value
print(os.getenv("MY_KEY"))
print(os.getenv("PYTHON_VERSION"))

this_dir = Path.cwd()
wb_file_path = this_dir / 'schools_dash_6-9-25.xlsx'

data = pd.read_excel(wb_file_path,
    sheet_name='Schools dashboard',
)
#Define filter options
status = data['Status'].unique().tolist()
print(status)
#Filter function
def filter_data(selected_status):
    filtered_data = data[(data['Status'].isin(selected_status))]
    return filtered_data
#Initializing
filtered_data1 = filter_data([u'Opened'])
filtered_data2 = filter_data([u'Deal'])
filtered_data3 = filter_data([u'Migrated'])
filtered_data4 = filter_data([u'Negotiation'])

with tgb.Page() as page:
    tgb.text("Schools dashboard", class_name="h1")
    with tgb.layout("1 1 1"):
        with tgb.part():
            tgb.text("##Industry number:", mode="md")
            tgb.text("{data['School market'].sum()}", class_name="h4")
            tgb.text("##Leads:", mode="md")
            tgb.text(f"{data['School'].count()}", class_name="h4")
            tgb.text("##Migrated companies:", mode="md")
            tgb.text(f"{filtered_data3['School'].count()}", class_name="h4")
            tgb.text("##Companies in negotiation:", mode="md")
            tgb.text(f"{filtered_data4['School'].count()}", class_name="h4")
            tgb.text("##Deals:", mode="md")
            tgb.text(f"{filtered_data2['School'].count()}", class_name="h4")
        with tgb.part():
            tgb.table("{filtered_data1}")
        with tgb.part():
            tgb.table("{filtered_data2}")

if __name__=="__main__":
   Gui(page).run(
       host="0.0.0.0",
       port= 10000,
       title="Schools dashboard",
       use_reloader=False,
       debug=False,
       allow_unsafe_werkzeug=True,
   )

