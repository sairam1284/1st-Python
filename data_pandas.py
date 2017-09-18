import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import code

data_raw = pd.read_csv('data_with_headers.csv')
print(data_raw.head())

time = data_raw['time']
time = time - time[0] #Want time to start at Zero

# Can see that sensors s5-s8 are blank. So need to focus on others
sensors = data_raw.ix[:, 's1':'s4']
avg_row = np.mean(sensors, 1)
avg_col = np.mean(sensors, 0)

col_final = [time, sensors, avg_row]
data_final = pd.concat(col_final, axis=1)

# Export the final table:
# data_final.to_csv('result.csv')
# data_final.to_html('result.htm')
# data_final.to_clipboard() #Ctrl-V will paste to whatever

plt.figure(1)
plt.plot(time, sensors['s1'], 'r-')
plt.plot(time, avg_row, 'b.')
plt.legend(['Sensor 1', 'Average'])
plt.xlabel('Time')
plt.ylabel('Sensor Values')
plt.savefig('Plot 1')
plt.show()

# code.interact(local=dict(globals(), **locals()))
