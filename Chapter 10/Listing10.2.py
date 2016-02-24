# Listing 10.2

import seaborn as sns	# Seaborn is a statistical visualization library

nClicks = df.click.value_counts()[True]
print('nClicks={} ({}%)'
.format(nClicks, round(float(nClicks) * 100 / nImps, 2)))

nViews = df.viewed.value_counts()[True]
print('nViews={} ({}%)'.format(nViews, 
round(float(nViews) * 100 / nImps, 2)))

# group by domain and look at number of impressions per domain
df.groupby('pub_domain').size()

f = df.groupby('pub_domain').size()
f.describe()

sns.distplot(np.log10(f));
