#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure,curdoc
from bokeh.models.widgets import Select
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool, Title


# In[2]:


# a
latimes_state_totals = pd.read_csv("latimes-state-totals.csv")
latimes_state_totals = latimes_state_totals[(latimes_state_totals["date"] >= "2020-08-01") & (latimes_state_totals["date"] <= "2020-08-31")]
latimes_state_totals['date_time'] = pd.to_datetime(latimes_state_totals['date'])


# In[3]:


p = figure(x_axis_type='datetime', x_axis_label='datetime',y_axis_label='New Confirmed Cases',
           title='New confirmed Coronavirus cases in California in August')


# In[4]:


p.line('date_time', 'new_confirmed_cases', source=latimes_state_totals, color='blue')
p.circle('date_time', 'new_confirmed_cases', source=latimes_state_totals, color='red')


# In[5]:


p.add_tools(HoverTool(
    tooltips=[
        ('date', '@date_time{%Y-%m-%d}'),
        ("new cases", "@new_confirmed_cases")
    ],

    formatters={
        '@date_time': 'datetime',
    }))


# In[6]:


p.add_layout(Title(text="Data source: https://github.com/datadesk/california-coronavirus-data", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data provided by California Department of Public Health", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data published at latimes.com/coronavirustracker", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data of last update: 10/15/2020", text_font_style="italic"), 'above')


# In[ ]:





# In[7]:


#b


# In[8]:


data = pd.read_csv("cdph-race-ethnicity.csv")
race_total = data.loc[data['age'] == 'all']
race_total = race_total[["date", "race", "confirmed_cases_percent", "deaths_percent", "population_percent"]]
total = race_total[["date", "race", "confirmed_cases_percent", "deaths_percent", "population_percent"]]
races = sorted(set(total["race"].tolist()))
death = total["deaths_percent"].tolist()
case = total["confirmed_cases_percent"].tolist()
population = total["population_percent"].tolist()
bar2 = ['confirmed_cases', 'population']
bar3 = ['death', 'population']
date = sorted(set(race_total['date']), reverse=True)

x2 = [(race, bar) for race in races for bar in bar2]
y2 = sum(zip(case, population), ())

source2 = ColumnDataSource(data=dict(x=x2, y=y2))

p2 = figure(x_range=FactorRange(*x2), plot_height=550,plot_width=1030,
            y_axis_label='percent', x_axis_label='race',
            toolbar_location=None, tools="")

p2.y_range.start = 0
p2.x_range.range_padding = 0.1
p2.xaxis.major_label_orientation = 1
p2.xgrid.grid_line_color = None
p2.add_tools(HoverTool(
    tooltips=[
        ('confirmed_case', '@x'),
        ('population', '@y'),
    ]))

p2.title.text = "Confirmed_cases_percent and Population_percent by race"

p2.add_layout(Title(text="Date of last update: 10/15/2020", text_font_style="italic"), 'above')
p2.add_layout(Title(text="Data source: https://github.com/datadesk/california-coronavirus-data", text_font_style="italic"), 'above')
p2.add_layout(Title(text="Data provided by the California Department of Public Health "
                         "'https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx';",
                    text_font_style="italic"), 'above')

r2 = p2.vbar(x='x', top='y', width=0.9, source=source2, line_color="white",
             fill_color=factor_cmap('x', palette=["red", "blue"], factors=bar2, start=1, end=2))


select1 = Select(title="date:", value=date[0], options=date, width=105)


def update2(attrname, old, new):
    selected_data = race_total[race_total['date'] == select1.value]
    a = selected_data['confirmed_cases_percent']
    b = selected_data["population_percent"]
    y = sum(zip(a, b), ())
    r2.data_source.data['y'] = y

select1.on_change('value', update2)


# In[ ]:





# In[9]:


# c


# In[10]:


x3 = [(race, bar) for race in races for bar in bar3]
y3 = sum(zip(death, population), ())

source3 = ColumnDataSource(data=dict(x=x3, y=y3))

p3 = figure(x_range=FactorRange(*x3), plot_height=500,plot_width=1000,
            y_axis_label='percent',
            x_axis_label='race',
            toolbar_location=None, tools="")
p3.title.text = "Death_percent and Population_percent by race"

r3 = p3.vbar(x='x', top='y', width=0.9, source=source3, line_color="white",
             fill_color=factor_cmap('x', palette=["red", "blue"], factors=bar3, start=1, end=2))

p3.y_range.start = 0
p3.x_range.range_padding = 0.1
p3.xaxis.major_label_orientation = 0.8
p3.xgrid.grid_line_color = None
p3.add_tools(HoverTool(
    tooltips=[
        ('death', '@x'),
        ('population', '@y'),
    ]))

p3.add_layout(Title(text="Date of last update: 10/15/2020", text_font_style="italic"), 'above')
p3.add_layout(Title(text="Data source: https://github.com/datadesk/california-coronavirus-data", text_font_style="italic"), 'above')
p3.add_layout(Title(text="Data provided by the California Department of Public Health "
                         "'https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx';",
                    text_font_style="italic"), 'above')

select2 = Select(title="Death date:", value=date[0], options=date, width=105)


def update3(attrname, old, new):
    selected_data = race_total[race_total['date'] == select2.value]
    a = selected_data['deaths_percent']
    b = selected_data["population_percent"]
    y = sum(zip(a, b), ())
    r3.data_source.data['y'] = y

select2.on_change('value', update3)


# In[ ]:





# In[11]:


curdoc().add_root(column(p))
curdoc().add_root(row(p2, select1))
curdoc().add_root(row(p3, select2))


# In[ ]:




