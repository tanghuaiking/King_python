# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:13:09 2019

@author: king
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# see the pre-defined styles provided.
plt.style.available
# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')
#######DataFrame.plot###########

np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))
df.head()
df.plot(); # add a semi-colon to the end of the plotting call to suppress unwanted output
df.plot('A','B', kind = 'scatter');
# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
######################
ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
##############
df.plot.box();
df.plot.hist(alpha=0.7);
df.plot.kde();
##########pandas.tools.plotting##########################


iris = pd.read_csv('iris.csv')
iris.head()
pd.tools.plotting.scatter_matrix(iris);

plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');
####Seaborn##########################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(1234)

v1 = pd.Series(np.random.normal(0,10,1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60,15,1000), name='v2')
plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50,150,5), label='v1');
plt.hist(v2, alpha=0.7, bins=np.arange(-50,150,5), label='v2');
plt.legend();
############################
# plot a kernel density estimation over a stacked barchart
plt.figure()
plt.hist([v1, v2], histtype='barstacked', normed=True);
v3 = np.concatenate((v1,v2))
sns.kdeplot(v3);

#######################
plt.figure()
# we can pass keyword arguments for each individual component of the plot
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'});
#################
sns.jointplot(v1, v2, alpha=0.4);
############################3
grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')
###########################
sns.jointplot(v1, v2, kind='hex');

########################33
# set the seaborn style for all the following plots
sns.set_style('white')

sns.jointplot(v1, v2, kind='kde', space=0);
###########################
iris = pd.read_csv('iris.csv')
iris.head()
#################
sns.pairplot(iris, hue='Name', diag_kind='kde', size=2);
##########
plt.figure(figsize=(8,6))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris);
























