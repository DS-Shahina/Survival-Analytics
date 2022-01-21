# pip install lifelines
# import lifelines

import pandas as pd
# Loading the the survival un-employment data
ECG = pd.read_csv('D:/C DRIVE-SSD DATA backup 15-12-2020/Desktop/360DigiTmg Assignment/Survival Analytics/ECG_Surv.csv')
ECG.head()
ECG.describe()
ECG.info()

ECG["survival_time_hr"].describe()

#Time <- survival_time_hr
#event <- alive 
#group <- group


ECG.columns
#drop all rows that have any NaN values
ECG = ECG.dropna(how='all')
ECG.survival_time_hr.isnull

# survival_time_hr is referring to time 
T = ECG.survival_time_hr

# pip install lifelines
# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Events  
kmf.fit(T, event_observed=ECG.alive)

# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is ui
ECG.group.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[ECG.group==1], ECG.alive[ECG.group==1], label='1')
ax = kmf.plot()

# Applying KaplanMeierFitter model on Time and Events for the group "2"
kmf.fit(T[ECG.group==2], ECG.alive[ECG.group==2], label='2')
kmf.plot(ax=ax)

# Applying KaplanMeierFitter model on Time and Events for the group "3"
kmf.fit(T[ECG.group==3], ECG.alive[ECG.group==3], label='3')
kmf.plot(ax=ax)
