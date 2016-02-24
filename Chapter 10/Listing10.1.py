# Listing 10.1 

%matplotlib inline
import pandas as pd
import seaborn as sns		# Seaborn is a statistical visualization library
import numpy as np
import matplotlib.pyplot as plt

# load data from a compressed archive
df = pd.read_pickle('combined.pickle')

nImps = len(df)
nPubs = len(df.pub_domain.unique())
nUsers = len(df.user_id.unique())

print('nImps={}\nnPubs={}\nnUsers={}'.format(nImps, nPubs, nUsers))

(nPubs * nUsers) / 1000000	# size of the “user/item matrix”
