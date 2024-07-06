import streamlit as st
import pandas as pd
from matplotlib_venn import venn2, venn3
from matplotlib import pyplot as plt

st.title("US Credit Card Travel Partners")

### LOGIC UI INTERFACE ###
comparison = st.selectbox(
    'Select how many credit cards you are comparing:', 
    (2, 3))
cc = []
for x in range(comparison):
    option = st.selectbox(
        'Select your credit card company', 
        ('American Express', 'BILT', 'Chase', 'Capital One'),
        key = x)
    cc.append(option)
    del option

### VENN CODE ###
# Load CSV file
df = pd.read_csv('credit_card_data.csv')

# Create sets of travel partners for each credit card
partner_sets = []
for card in cc:
    card_partners = set(df[df['Credit Card'] == card]['Travel Partner'])
    if len(card_partners) > 0:
        partner_sets.append(card_partners)

# Create Venn diagram
if len(partner_sets) == 3:
    # Assign unique colors to intersection areas
    c = ('red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'gray')
    v = venn3(subsets=partner_sets, set_labels=cc, set_colors=c, normalize_to=100)

    # Add travel partner names to intersection areas
    v.get_label_by_id('100').set_text('\n'.join(partner_sets[0] - partner_sets[1] - partner_sets[2]))
    v.get_label_by_id('010').set_text('\n'.join(partner_sets[1] - partner_sets[0] - partner_sets[2]))
    v.get_label_by_id('001').set_text('\n'.join(partner_sets[2] - partner_sets[0] - partner_sets[1]))
    v.get_label_by_id('110').set_text('\n'.join(partner_sets[0] & partner_sets[1] - partner_sets[2]))
    v.get_label_by_id('101').set_text('\n'.join(partner_sets[0] & partner_sets[2] - partner_sets[1]))
    v.get_label_by_id('011').set_text('\n'.join(partner_sets[1] & partner_sets[2] - partner_sets[0]))
    v.get_label_by_id('111').set_text('\n'.join(partner_sets[0] & partner_sets[1] & partner_sets[2]))
    
    # Adjust text size
    for t in v.set_labels: t.set_fontsize(12)
    for t in v.subset_labels: t.set_fontsize(8)
elif len(partner_sets) == 2:
    c = ('red', 'green', 'blue')
    v = venn2(subsets=partner_sets, set_labels=cc, set_colors=c, normalize_to=100)

    # Add travel partner names to intersection areas
    v.get_label_by_id('10').set_text('\n'.join(partner_sets[0] - partner_sets[1]))
    v.get_label_by_id('01').set_text('\n'.join(partner_sets[1] - partner_sets[0]))
    v.get_label_by_id('11').set_text('\n'.join(partner_sets[0] & partner_sets[1]))
    
    # Adjust text size
    for t in v.set_labels: t.set_fontsize(12)
    for t in v.subset_labels: t.set_fontsize(8)
else:
    print("Error: Number of credit cards must be 2 or 3")

### PLOTTING ###
plt.title("Credit Card Partners", fontsize = 14)
plt.savefig('test.png')
fig = plt.show
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(plt.show())
