import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

# load
path = "/2022 Masters Stats.xlsx"
df = pd.read_excel(path, sheet_name='2022 Masters Data Main Sheet')

# create groups by bs_aggr quartiles
df['vol_q'] = pd.qcut(df['bs_aggr'], 4, labels=['Q1','Q2','Q3','Q4'])
q25 = df['bs_aggr'].quantile(0.25)
q75 = df['bs_aggr'].quantile(0.75)
def vol_label(x):
    if x <= q25: return 'Low'
    if x >= q75: return 'High'
    return 'Mid'
df['aggr_group'] = df['bs_aggr'].apply(vol_label)

# group summary
group_stats = df.groupby('aggr_group').agg(
    n=('player','count'),
    mean_sg_total=('sg_total','mean'),
    median_sg_total=('sg_total','median'),
    mean_score_par=('score_par_diff','mean')
).reset_index()
print(group_stats)

# t-test high vs low for sg_total
high = df[df['aggr_group']=='High']['sg_total']
low = df[df['aggr_group']=='Low']['sg_total']
tstat, pval = stats.ttest_ind(high, low, equal_var=False, nan_policy='omit')
print("t-stat:", tstat, "p-value:", pval)

# correlations
print(df[['sg_total','bs_aggr','aggr_split','sg_t2g','sg_putt','sg_app','sg_ott']].corr())

# regression
X = df[['bs_aggr','sg_putt']]
X = sm.add_constant(X)
y = df['sg_total']
model = sm.OLS(y, X).fit()
print(model.summary())

# robustness on made_cut
made = df[df['made_cut']==1]
X2 = sm.add_constant(made[['bs_aggr','sg_putt']])
model2 = sm.OLS(made['sg_total'], X2).fit()
print(model2.summary())

  aggr_group   n  mean_sg_total  median_sg_total  mean_score_par
0       High  20       1.387500            1.350        1.350000
1        Low  20      -2.316500           -1.840       10.450000
2        Mid  38       0.058947            0.225        5.447368
t-stat: 7.953803329886411 p-value: 1.6988304458563733e-09
            sg_total   bs_aggr  aggr_split    sg_t2g   sg_putt    sg_app  \
sg_total    1.000000  0.772788   -0.161483  0.830733  0.389876  0.668766   
bs_aggr     0.772788  1.000000   -0.162466  0.902437 -0.129461  0.831024   
aggr_split -0.161483 -0.162466    1.000000 -0.215405  0.070180 -0.058442   
sg_t2g      0.830733  0.902437   -0.215405  1.000000 -0.188731  0.736743   
sg_putt     0.389876 -0.129461    0.070180 -0.188731  1.000000 -0.039055   
sg_app      0.668766  0.831024   -0.058442  0.736743 -0.039055  1.000000   
sg_ott      0.509321  0.703014   -0.212115  0.651307 -0.178631  0.188639   

              sg_ott  
sg_total    0.509321  
bs_aggr     0.703014  
aggr_split -0.212115  
sg_t2g      0.651307  
sg_putt    -0.178631  
sg_app      0.188639  
sg_ott      1.000000  
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               sg_total   R-squared:                       0.841
Model:                            OLS   Adj. R-squared:                  0.837
Method:                 Least Squares   F-statistic:                     198.8
Date:                Wed, 10 Dec 2025   Prob (F-statistic):           1.05e-30
Time:                        02:02:29   Log-Likelihood:                -90.441
No. Observations:                  78   AIC:                             186.9
Df Residuals:                      75   BIC:                             194.0
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0398      0.089     -0.445      0.658      -0.218       0.138
bs_aggr        1.1146      0.062     18.050      0.000       0.992       1.238
sg_putt        0.8785      0.082     10.741      0.000       0.716       1.041
==============================================================================
Omnibus:                        0.545   Durbin-Watson:                   1.588
Prob(Omnibus):                  0.761   Jarque-Bera (JB):                0.209
Skew:                          -0.107   Prob(JB):                        0.901
Kurtosis:                       3.136   Cond. No.                         1.50
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               sg_total   R-squared:                       0.799
Model:                            OLS   Adj. R-squared:                  0.790
Method:                 Least Squares   F-statistic:                     91.23
Date:                Wed, 10 Dec 2025   Prob (F-statistic):           9.79e-17
Time:                        02:02:29   Log-Likelihood:                -46.656
No. Observations:                  49   AIC:                             99.31
Df Residuals:                      46   BIC:                             105.0
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0395      0.110      0.359      0.721      -0.182       0.261
bs_aggr        1.1565      0.106     10.925      0.000       0.943       1.370
sg_putt        0.9854      0.114      8.661      0.000       0.756       1.214
==============================================================================
Omnibus:                        0.441   Durbin-Watson:                   2.120
Prob(Omnibus):                  0.802   Jarque-Bera (JB):                0.598
Skew:                           0.156   Prob(JB):                        0.741
Kurtosis:                       2.558   Cond. No.                         1.85
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
