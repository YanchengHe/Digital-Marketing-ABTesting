import math

import pandas as pd
import numpy as np
from scipy.stats import norm
import datetime

print((1-norm.cdf(1.64))*2)
print(norm.ppf(1-(0.05/2)))