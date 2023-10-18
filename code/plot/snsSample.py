# %% importing packages 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt
# %% creating data 
df = pd.DataFrame({'Date': ['2019-10-01', '2019-11-01', 
							'2019-12-01','2020-01-01', 
							'2020-02-01', '2020-03-01', 
							'2020-04-01', '2020-05-01', 
							'2020-06-01'], 
					
				'Col_1': [34, 43, 14, 15, 15, 
							14, 31, 25, 62], 
					
				'Col_2': [52, 66, 78, 15, 15, 
							5, 25, 25, 86], 
					
				'Col_3': [13, 73, 82, 58, 52, 
							87, 26, 5, 56], 
				'Col_4': [44, 75, 26, 15, 15, 
							14, 54, 25, 24]}) 

# %% create the time series plot 
sns.lineplot(x = "Date", y = "Col_1", 
			data = df) 

plt.xticks(rotation = 25)
