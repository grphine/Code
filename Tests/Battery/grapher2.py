import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

blue, = sns.color_palette("muted", 1)

def legend_merge(plot1, plot2, loc, axis1, axis2):
    handle1, label1 = plot1.get_legend_handles_labels()
    handle2, label2 = plot2.get_legend_handles_labels()
    axis1.legend(loc=loc, handles=handle1+handle2, labels = label1 + label2)
    axis2.get_legend().remove()

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

#styling
legend_merge(d_level, d_fix, 0, ax00, ax01)
ax01.fill_between(df_discharge['Datetime'], 0, df_discharge['Fix'], alpha=0.3)
#limits
ax00.set_ylim(2,4.25)
ax01.set_ylim(0,2)
ax01.set_yticks([0,1,2])
ax00.set_title('Discharge curve')

#second subplot
c_level = sns.lineplot(data=df_charge, x='Datetime', y='Voltage', color='g', lw='2', ax=ax10, label='Voltage')
c_fix = sns.lineplot(data=df_charge, x='Datetime', y='Fix', ax=ax11, color=blue, label='Fix')

#styling
legend_merge(c_level, c_fix, 1, ax10, ax11)
ax11.fill_between(df_charge['Datetime'], 0, df_charge['Fix'], alpha=0.3)
#limits
ax10.set_ylim(1,4.25)
ax11.set_ylim(0,2)
ax11.set_yticks([0,1,2])
ax10.set_title('Charge curve')

#graph labels
ax00.set_ylabel('Voltage (V)')
ax10.set_ylabel('Voltage (V)')
fig.suptitle('Battery charge curves')
# plt.legend()

plt.show()
