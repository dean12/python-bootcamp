# 1. Import the required libraries
import numpy as np
import pandas as pd
from urllib2 import urlopen 

# Specify the URL to extract the data from
url_info = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.names"

# Download the file
raw_data = urlopen(url_info)
print(raw_data.read())

# Note that if you are interested in scraping web pages, you can use the Beautiful Soup library from 
# https://www.crummy.com/software/BeautifulSoup/


# Specify the URL for the Housing dataset (UCI Machine Learning Repository)
url_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"

# 3. Download the file
raw_data = urlopen(url_data)

# 4. Load the data file as pandas dataframe
housing_dataset = pd.read_csv(raw_data, delim_whitespace=True, 
                              names=('crime_per_capita', 'zoned_land', 'industry_land',
                              'bounds_river', 'nox_concentrate', 'ave_rooms', 'age', 
                               'dist_emp', 'access_highway', 'tax_rate', 'std_teach_ratio', 
                               'black_prop', 'lstat', 'med_price'))
