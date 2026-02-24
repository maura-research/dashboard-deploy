import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode

st.set_page_config(layout="wide")
theme_colors = [
        "#2f4554",
        "#c23531",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ]

### DATA INPUT ###
df_database = pd.read_csv("./data/processed_data.csv")

########################
### LABELS AND TEXTS ###
########################
unique_year = np.unique(df_database["School Year"]).tolist()
unique_major = np.unique(df_database.Major).tolist()

y_n_pns = ['Yes', 'No', 'Prefer not to say']
aspects = ["All responses", "Gender", "School Year", "International Students", "First-Generation Students", "Low-income Students", "Transgender Students", "Students with Disabilities"]
aspects_bundles = {"Gender": ['Man', 'Woman', 'Other'], "School Year": ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Fifth year+', 'Graduate Student'],
"International Students": y_n_pns, "First-Generation Students": y_n_pns, "Low-income Students":y_n_pns, "Transgender Students":y_n_pns, "Students with Disabilities": y_n_pns}

race_labels = ["African American/Black", "Hispanic/Latine", "Middle Eastern/North African", "Asian", "Pacific Islander/Hawaiian", "Native America/Alaskan Native/First Nations", "White"]
lgbq_labels = ['Asexual', 'Bisexual', 'Gay/Lesbian', 'Heterosexual', 'Pansexual', 'Queer', 'Other']

confidence_labels = ['confident', 'intimidated', 'pressure']
confidence_answers = {"confident": "I feel confident studying computer science and related fields", 
"intimidated": "I feel intimidated studying computer science and related fields",
"pressure": "I feel pressure to find internships, job opportunities, and/or extracurricular activities"}

aggression_labels = ['Microagression', 'Interrupted', 'Respected in Group']
aggression_answers = {'Microagression': 'I have experienced microaggression',  
'Interrupted': 'I have been interrupted or talked to condescendingly by someone who assumed they knew more', 
'Respected in Group': 'In a group project, my opinion is as respected as that of other group members'}

respect_labels = ['peer_respect', 'staff_respect', 'prove_myself' , 'tell_peers', 'tell_professors']
respect_answers = {'peer_respect': 'My peers respect me',
'staff_respect': 'My professors and TAs respect me', 
'prove_myself': 'I have to prove myself before being taken seriously in academic settings',
'tell_peers': 'I would tell my peers if they made discriminatory or inappropriate comments',
'tell_professors': 'I would tell my professors, TAs, or another authoritative figure if a discriminatory or inappropriate comment was made during class or office hours, either by another student, a TA, or the professor'}

comfortable_labels = ['Asks in Lecture', 'Asks in OH', 'Professor Same Background', 'OH Same Background', 'Asks on Forum']
comfortable_answers = {'Asks in Lecture': 'I generally feel comfortable asking questions during lectures',
'Asks in OH': 'I generally feel comfortable asking questions in office hours',
'Professor Same Background': 'I feel more comfortable in a class taught by a professor who shares a similar background',
'OH Same Background': 'I prefer to go to office hours led by someone who shares a similar background',
'Asks on Forum': 'I ask questions on a class forum, anonymously or publicly'}

#Someone has once claimed to me that _____ has unfairly contributed to my acceptance
#to [Campus Name]. Check all that applies to you.
acceptance_labels = ['Acceptance Race', 'Acceptance Gender', 'Acceptance Orientation', 'Acceptance Disability', 
'Acceptance FirstGen', 'Acceptance Income']
acceptance_answers = {'Acceptance Race': 'Race/Ethnicity',
'Acceptance Gender': 'Gender Indentity', 
'Acceptance Orientation': 'Sexual Orientation', 
'Acceptance Disability': 'Disability', 
'Acceptance FirstGen': 'Being a First Generation student', 
'Acceptance Income': 'Income Status'}

#Someone has once claimed to me that _____ has unfairly given me an advantage in
#gaining job opportunities. Check all that applies to you.
job_labels = ['Job Race', 'Job Gender', 'Job Orientation', 'Job Disability', 
'Job FirstGen', 'Job Income']
job_answers = {'Job Race': 'Race/Ethnicity',
'Job Gender': 'Gender Indentity', 
'Job Orientation': 'Sexual Orientation', 
'Job Disability': 'Disability', 
'Job FirstGen': 'Being a First Generation student', 
'Job Income': 'Income Status'}

#Check all of the following that you agree with. I believe that conscious and unconscious
#biases against certain groups based on ______ still exist today.
bias_labels = ['Bias Race', 'Bias Gender', 'Bias Orientation', 'Bias Disability', 
'Bias ParentEducation', 'Bias Income', 'Bias Other']
bias_answers = {'Bias Race': 'Race/Ethnicity',
'Bias Gender': 'Gender Indentity', 
'Bias Orientation': 'Sexual Orientation', 
'Bias Disability': 'Disability', 
'Bias ParentEducation': 'Parental Education', 
'Bias Income': 'Income Status',
'Bias Other': 'Other'}

topic_bundles = {"confidence": {"text": "How Confident Are the Students?", "labels":confidence_labels, "answers":confidence_answers},
"microaggression": {"text": "Have Students Experienced Microaggression?", "labels":aggression_labels, "answers":aggression_answers},
"respect": {"text": "Do Students Feel Respected?", "labels":respect_labels, "answers":respect_answers},
"comfort": {"text": "How Comfortable Do Students Feel About Asking Questions?", "labels":comfortable_labels, "answers":comfortable_answers},
"acceptance": {"text": "Someone Has Once Claimed to Students that Their ______ Has Unfairly Contributed to Their Acceptance to Their Schools", "labels":acceptance_labels, "answers":acceptance_answers},
"job": {"text": "Someone Has Once Claimed to Students that Their ______ Has Unfairly Given Them An Advantage In Gaining Job Opportunities", "labels":job_labels, "answers":job_answers},
"bias": {"text": "Students Believe That Conscious and Unconscious Biases Against Certain Groups Based on ______ Still Exist Today", "labels":bias_labels, "answers":bias_answers},
"roleModel":"Do Students Have A Faculty Whom They Perceive As a Role Model?",
"leaving": "Have Students Ever Considered Leaving Their Study?",
"dropOut": "Has a Faculty Member or an Administrator Ever Encouraged Students to Drop Out?",
"equal": "Do Students Feel that Students From Every Background Have an Equal Chance to Succeed in Their School?",
"department": "Do Students Adequately Supported By Their Major Department and the Resources Offered By the Department?",
"groups": "Do Students Believe Organizations Whose Purpose is to Support Underrepresented or Marginalized Groups Are Still Needed Today?"}

###########################
### INTERFACE - SIDEBAR ###
###########################
st.sidebar.text('')
st.sidebar.text('')

st.sidebar.markdown("**First choose the data you want to analyze (display all data by default):** 👇")
st.sidebar.caption("Select and deselect the categories you would like to include in the analysis. You can clear the current selection by clicking the corresponding x-button on the right")

selected_years = st.sidebar.multiselect("School Year", unique_year, default =  unique_year)
selected_majors = st.sidebar.multiselect("Major", unique_major, default =  unique_major)

##################################
### DATA PRCOCESSING FUNCTIONS ###
##################################
# filter data based on what users select through the sidebar
def filter_data(df_data):
    df_filtered = pd.DataFrame()
    df_filtered = df_data[df_data['School Year'].isin(selected_years)] # the first to be filtered on should use df_database
    df_filtered = df_filtered[df_filtered['Major'].isin(selected_majors)]
    return df_filtered

df_filtered = filter_data(df_database)
respondents_num = df_filtered.shape[0]

# return necessary data input for pie chart generation
def pie_chart_data(demographic_factor):
    df_summary =  df_filtered.groupby(demographic_factor)[demographic_factor].count()
    keys = df_summary.index.values.tolist()
    sum_values = df_summary.values.tolist()
    zipped = list(zip(keys, sum_values))

    source_data = []
    for key, sum_value in zipped:
        source_data.append({"value": sum_value, "name": key})

    return source_data

# return a list of percentages for each answer under a multi-selection question - raw bar chart data
def metrics_percent(df_data, metrics_label):
    precent_list = []
    df_metrics_data = df_data[metrics_label]
    counts = df_metrics_data.sum().tolist()
    for count in counts:
        percent_num = round((count/respondents_num)*100, 1)
        if metrics_label == race_labels or metrics_label == lgbq_labels:
            precent_list.append(percent_num)
        else:
            precent_list.append([percent_num])
    return precent_list

def metrics_group_percent(df_grouped, labels):
    counts_lists = []
    for label in labels:
        counts_lists.append(df_grouped[label].tolist())
    
    group_sum = df_grouped.sum(axis=1).tolist()
    precent_lists = []

    for counts in counts_lists:
        raw_res = [a/b for a,b in zip(counts,group_sum)]
        res = list(np.around(np.array(raw_res)*100,1))
        precent_lists.append(res)

    return precent_lists

# return necessary data input for bar chart generation that looks like
#     "source": [
#     ['product', '2015', '2016', '2017'],
#     ['Matcha Latte', 43.3, 85.8, 93.7],
#     ['Milk Tea', 83.1, 73.4, 55.1],
#     ]
def bar_chart_source_data(labels, answers, selected_aspect):
    source_data = []

    if selected_aspect == "All responses":
        percents = metrics_percent(df_filtered, labels)
    else:
        percents = metrics_group_percent(df_grouped, labels)
        groups = df_grouped.index.values.tolist()
        groups.insert(0,'Groups')
        source_data.append(groups)

    for i in range(len(labels)):
        key = [answers[labels[i]]]
        key.extend(percents[i])
        source_data.append(key)
    
    return source_data

def bar_chart_source_data_ctg(topic, selected_aspect):
    source_data = [['Yes'], ['No'], ['Maybe']]
    if selected_aspect == "All responses":
        counts = df_filtered[topic].value_counts().sort_index(ascending=False).tolist()
        total = 0
        for count in counts:
            total += count
        for j in range(3):
            source_data[j].append(round((counts[j]/total)*100, 1))
    
    else:
        groups = aspects_bundles[selected_aspect].copy()
        for i in range(len(groups)):
            counts = df_grouped[groups[i]].tolist()
            total = 0
            for cnt in counts:
                total += cnt
            for x in range(3):
                source_data[x].append(round((counts[x]/total)*100, 1))
    
        groups.insert(0,'Groups')
        source_data.insert(0, groups)
            
    return source_data

##########################
### PLOTTING FUNCTIONS ###
##########################
# return config input for pie chart generation
def pie_plot_series(position, source_data_set):
    if position == "left":
        data = source_data_set[0]
        center = ["25%", "60%"]
    else:
        data = source_data_set[1]
        center = ["75%", "60%"]

    series = {
            "type": 'pie',
            "data": data,
            "radius": "55%",
            "center": center,
            "label": {
                "formatter": "{b}", "color": 'auto', "fontSize":12,
                "fontWeight": "normal", "overflow": "break", "width": 100
            },
            "labelLayout": "string", # show otherwise hidden label
            "emphasis": {"focus": "none", "scale": True, "scaleSize": 10} 
            }
    return series

def pie_plot_config(source_data_set, factors):
    dataset = source_data_set
    options = {
        "title": [{
            "subtext": factors[0],
            "left": "24%",
            "top": "10%",
            "textAlign": 'center',
            "subtextStyle": {"color": "#333","fontSize": 18, "fontStyle": 'normal', "fontWeight": "bolder"}
        }, {
            "subtext": factors[1],
            "left": "74%",
            "top": "10%",
            "textAlign": 'center',
            "subtextStyle": {"color": "#333","fontSize": 18, "fontStyle": 'normal', "fontWeight": "bolder"}
        }],
        "color": theme_colors,
        "tooltip": {
            "trigger": 'item',
            "formatter": "{b}: {d}%",
            },
        "series": [pie_plot_series("left", dataset), pie_plot_series("right", dataset)]
    }
    return options

# return config input for demographic barplot generation
def demo_barplot_config(source_data, topic):
    title = topic
    if topic == "Ethnicity":
        data = race_labels
    else:
        data = lgbq_labels

    options = {
    "title": {"text": title, "left": "center"},
    "tooltip": {
       "trigger": 'item',
       "axisPointer": 'shadow',
       "formatter": "{b}: {c}%",
    },
    "yAxis": { 
        "type": 'category',
        "data": data,
        "axisTick": { "show": False },
        "axisLabel":{"show": False,"interval": "auto", "overflow": "break", "width": 150, "height": 300}
    },
    "xAxis": {},
    "series": { "type": 'bar', "data": source_data},
    "label": {
        "show": True, 
        "formatter": "{b}",
        "distance": 10, 
        "fontSize": 12, 
        "position": "right", 
        "fontWeight": "normal"
    }
    }
    return options

# return config input for bar chart generation
def bar_plot_config(source_data, selected_aspect):
    xAxis_config = { 
            "type": 'category',
            "axisLabel":{"interval": 0, "overflow": "break", "width": 120, "height": 400}
            }
    yAxis_config = {}
    
    if selected_aspect == "All responses":
        series = { "type": 'bar' }
    else:
        series = []
        group_size = len(source_data[0])-1
        for _ in range(group_size):
            series.append({ "type": 'bar' })
        if group_size > 6:
            xAxis_config = {}
            yAxis_config = { 
            "type": 'category',
            "axisLabel":{"interval": 0, "overflow": "break", "width": 100, "height": 200}
            }

    options = {
    "tooltip": {
       "trigger": 'axis',
        "axisPointer": {"type": 'shadow'},
        "showContent": False
    },
    "legend": {
        "orient": 'horizontal',
        "left": 'left'
    },
    "grid": {
        "left": 0,
        "right": '4%',
        "containLabel": True
  },
    "dataset": {
        "source": source_data
    },
    "xAxis": xAxis_config,
    "yAxis": yAxis_config,
    "series": series,
    "label": {
        "show": True, 
        "distance": 10, 
        "fontSize": 10, 
        "position": "top", 
        "formatter": JsCode( "function(x){return x.value[x.encode.y[0]] + '%';}").js_code,
        "fontWeight": "lighter"
    },
    "emphasis": {"focus": "series"}
    }
    return options

# pie chart generation
def pie_chart_plot(demographic_factors):
    factors = demographic_factors
    source_data_set= [pie_chart_data(factors[0]), pie_chart_data(factors[1])]
    return st_echarts(options=pie_plot_config(source_data_set, factors), height= "325px", width="100%")

# demographic bar chart generation
def demo_bar_plot(topic):
    if topic == "Ethnicity":
        labels = race_labels
    else:
        labels = lgbq_labels
    source_data = metrics_percent(df_filtered, labels)
    return st_echarts(options=demo_barplot_config(source_data, topic), height= "400px", width="105%")

# bar chart generation
def bar_chart_plot(labels, answers, selected_aspect):
    height = "400px"
    if selected_aspect != "All responses" and len(aspects_bundles[selected_aspect]) > 6:
        height = "700px"
    source_data = bar_chart_source_data(labels, answers, selected_aspect)
    return st_echarts(options=bar_plot_config(source_data, selected_aspect), height= height, width="100%")

def bar_chart_plot_ctg(topic, selected_aspect):
    height = "400px"
    if selected_aspect != "All responses" and len(aspects_bundles[selected_aspect]) > 6:
        height = "700px"    
    source_data = bar_chart_source_data_ctg(topic, selected_aspect)
    return st_echarts(options=bar_plot_config(source_data, selected_aspect), height= height, width="100%")

# single bar chart widget display
def bar_chart_widget(topic):
    topic_bundle = topic_bundles[topic]
    text = topic_bundle["text"]
    labels = topic_bundle["labels"]
    answers = topic_bundle["answers"]

    st.subheader(text)
    selected_aspect = st.selectbox (label = "Choose demographic factors to compare:", options=aspects, key=topic)
    if selected_aspect == 'All responses':
        bar_chart_plot(labels, answers, selected_aspect)

    else:
        global df_grouped
        df_grouped = df_filtered.groupby(selected_aspect)[labels].sum().reindex(aspects_bundles[selected_aspect])
        bar_chart_plot(labels, answers, selected_aspect)
        # st.dataframe(df_grouped) # for temp reference
    st.markdown('##')

def bar_chart_widget_ctg(topic):
    text = topic_bundles[topic]

    st.subheader(text)
    selected_aspect = st.selectbox (label = "Choose demographic factors to compare:", options=aspects, key=topic)
    if selected_aspect == 'All responses':
        bar_chart_plot_ctg(topic, selected_aspect)

    else:
        global df_grouped
        df_grouped = df_filtered.groupby(selected_aspect)[topic].value_counts().unstack(fill_value=0).stack().sort_index(ascending=False)
        bar_chart_plot_ctg(topic, selected_aspect)
        # st.dataframe(df_grouped) # for temp reference
    st.markdown('##')

#############################
### INTERFACE - MAIN PAGE ###
#############################
st.title("The Percentage Project")
st.metric(label = "The total number of respondents you selected is:", value=respondents_num)

# test
option_test = {
  "title": {
    "text": 'World Population'
  },
  "tooltip": {
    "trigger": 'axis',
    "axisPointer": {
      "type": 'shadow'
    }
  },
  "legend": {},
  "grid": {
    "left": "left",
    "right": 0,
    "containLabel": True,
  },
  "xAxis": {
  },
  "yAxis": {
    "type": 'category',
    "axisLabel":{"interval": 0, "overflow": "break", "width": 100, "height": 100, "hideOverlap": True, "align": 'left'},
    "data": ['Brazil', 'Indonesia', 'USA', 'India', 'China', 'I would tell my professors, TAs, or another authoritative figure if a discriminatory or inappropriate comment was made']
  },
  "series": [
    {
      "name": '2011',
      "type": 'bar',
      "data": [18203, 23489, 29034, 104970, 131744, 630230]
    },
    {
      "name": '2012',
      "type": 'bar',
      "data": [19325, 23438, 31000, 121594, 134141, 681807]
    }
  ]
}


# st_echarts(options=option_test, height= "700px", width="100%")

## PIE CHART ##
st.subheader("Data At A Glance")
pie_chart_plot(["Gender", "Major"])
pie_chart_plot(["School Year", "International Students"])
pie_chart_plot(["Low-income Students", "First-Generation Students"])
pie_chart_plot(["Students with Disabilities", "Transgender Students"])

## DEMOGRAPHIC BAR CHART ##
demo_bar_plot("LGBQ")
demo_bar_plot("Ethnicity")

## QUESTION BAR CHART ##
st.header("Here are some questions we asked...")
st.markdown(":bulb: Showing all responses by default. If you want to break down the responses by certain demographic factor, please click the dropdown box and then select the one you want to compare the data.\n\n :bulb: When you choose to break down the responses, you can also select and deselect groups to display by clicking the top-left legends.\n\n :bulb: Highlight groups you are interested in by hovering over bars.")
st.markdown('###')

for topic in topic_bundles:
    if topic in ["confidence", "microaggression", "respect", "comfort", "acceptance", "job", "bias"]:
        bar_chart_widget(topic)
    else:
        bar_chart_widget_ctg(topic)


# st.dataframe(df_filtered) #for temp reference