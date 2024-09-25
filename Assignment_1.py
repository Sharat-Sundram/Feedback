#Highest attendence student in first five row


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("attendence")

df=pd.read_csv("physics.csv")

x=df.head().iloc()[:,1]
y=df.head().iloc[:,2]

plt.bar(x,y)
plt.show()





#######################################
#######################################





#Highest attendence student in last five row


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("physics.csv")

x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]

plt.bar(x,y)
plt.show()




#######################################
#######################################

#Attendence of student from rows 10-20



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("physics.csv")

x=df.iloc[9:19:,1]
y=df.iloc[9:19:,2]

plt.bar(x,y)
plt.show()




#######################################
#######################################



#Overall attendence


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("physics.csv")

x=df.iloc[:,1]
y=df.iloc[:,2]

plt.bar(x,y)
plt.show()

























































































