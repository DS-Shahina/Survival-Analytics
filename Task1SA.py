# pip install lifelines
# import lifelines

import pandas as pd
# Loading the the survival un-employment data
Patient = pd.read_csv("D:/C DRIVE-SSD DATA backup 15-12-2020/Desktop/360DigiTmg Assignment/Survival Analytics/Patient.csv")
Patient.head()
Patient.describe()

Patient["Followup"].describe()

#Time <- Followup
#event <- Eventtype
#group <- Scenario

# Followup is referring to time 
T = Patient.Followup

# pip install lifelines
# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter

# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()

# Fitting KaplanMeierFitter model on Time and Eventtype
kmf.fit(T, event_observed=Patient.Eventtype)

# Time-line estimations plot 
kmf.plot()

Patient.Scenario.value_counts()

# Applying KaplanMeierFitter model on Time and Events for the group "A"
kmf.fit(T[Patient.Scenario=="A"], Patient.Eventtype[Patient.Scenario=="A"], label='A')
ax = kmf.plot()
