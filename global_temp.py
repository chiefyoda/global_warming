import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class GlobalTempAnalysis:
    def __init__(self, baseline_temps, data):
        self.base_temps = baseline_temps
        self.data = data

    def load_and_process_data(self):
        data = []
        with open(self.data, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('%') or '':
                    continue
                else:
                    parts = line.split()
                    if len(parts) == 12:
                        year = int(parts[0])
                        month = int(parts[1])
                        values = []
                        for v in parts[2:]:
                            if v == 'NaN':
                                values.append(None)
                            else:
                                values.append(float(v))
                        data.append({
                            'year': year,
                            'month':month,
                            'monthly_anomaly':values[0]
                            })

        self.df = pd.DataFrame(data)
        self.df['baseline_temp'] = self.df['month'].map(baseline_monthly_temps)
        self.df['absolute_temp'] = self.df['baseline_temp']+self.df['monthly_anomaly'].fillna(np.nan)


    def plot(self):
        sns.lineplot(data=self.df, x="year", y="absolute_temp")
        plt.savefig('global_temp.png')


baseline_monthly_temps = {
    1: 12.23, 2: 12.44, 3: 13.06, 4: 13.97, 5: 14.95, 6: 15.67,
    7: 15.95, 8: 15.79, 9: 15.19, 10: 14.26, 11: 13.24, 12: 12.49
}

global_temp = GlobalTempAnalysis(baseline_monthly_temps, 'Land_and_Ocean_complete.txt')
global_temp.load_and_process_data()
global_temp.plot()



