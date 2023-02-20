import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

blue, = sns.color_palette("muted", 1)

#read data into dataframes
# merging two csv files
df_discharge = pd.concat(map(pd.read_csv, ['Tests\\Battery\\data\\230213.csv', 'Tests\\Battery\\data\\230214-old.csv']), ignore_index=True)
df_discharge['Datetime'] = pd.to_datetime(df_discharge['Datetime'], format='%d-%m-%y %H:%M:%S')

df_charge = pd.read_csv('Tests\\Battery\\data\\230214.csv', parse_dates=['Datetime'], dayfirst=True)

# subplot with shared x 
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6))
ax00 = ax[0]
ax01 = ax[0].twinx()    #twin the axis
ax10 = ax[1]
ax11 = ax[1].twinx()

#first subplot
d_level = sns.lineplot(data=df_discharge, x='Datetime', y='Voltage', color='g', lw='2', ax=ax00, label='Voltage')
d_fix = sns.lineplot(data=df_discharge, x='Datetime', y='Fix', ax=ax01, color=blue, label='Fix')

#legend merging
h1,l1 = d_level.get_legend_handles_labels()
h2,l2 = d_fix.get_legend_handles_labels()
ax00.legend(loc=0, handles=h1+h2, labels = l1+l2)
#remove extra legend
ax01.get_legend().remove()   

#styling
ax00.set_xlim()
ax00.fill_between(df_discharge['Datetime'], 0, df_discharge['Fix'], alpha=0.3)

#second subplot
c_level = sns.lineplot(data=df_charge, x='Datetime', y='Voltage', ax=ax10, label='Voltage')
d_fix = sns.lineplot(data=df_charge, x='Datetime', y='Fix', ax=ax10, color=blue, label='Fix')
ax10.fill_between(df_charge['Datetime'], 0, df_charge['Fix'], alpha=0.3)

#graph labels
ax00.set_ylabel('Voltage (V)')
ax10.set_ylabel('Voltage (V)')
fig.suptitle('Battery charge curves')
plt.legend()

plt.show()
