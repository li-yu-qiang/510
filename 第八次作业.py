# 车牌价格
# 2018.5.12
#

import numpy as np
from sklearn.linear_model.coordinate_descent import ConvergenceWarning
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

X_train = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
X_test = [[12]]
y_train1 = [[15900], [17300], [18900], [21500], [23900], [25000], [26800], [28800], [30000], [30700], [32100]]
y_train2 = [[17419], [18358], [20127], [22996], [25498], [26668], [28561], [30535], [32449], [34046], [34455]]


# y_test1 = []

# 建立线性回归，并用训练的模型绘图
def reg(X_train, y_train):
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    xx = np.linspace(0, 15, 100)
    yy = regressor.predict(xx.reshape(xx.shape[0], 1))
    plt.plot(X_train, y_train, 'k.')
    cubic_featurizer = PolynomialFeatures(degree=3)
    X_train_cubic = cubic_featurizer.fit_transform(X_train)
    regressor_cubic = LinearRegression()
    regressor_cubic.fit(X_train_cubic, y_train)
    xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0], 1))
    plt.plot(xx, regressor_cubic.predict(xx_cubic))
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("车牌价格")
    plt.show()
    return regressor.predict(X_test)


a = reg(X_train, y_train1)
b = reg(X_train, y_train2)
print("5月个人最低成交价格:%f" % a)
print("5月个人平均成交价格:%f" % b)

warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

plt.figure(figsize=(8, 4))
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("车牌价格")

data = np.loadtxt('price_date2.csv', str, delimiter=",", skiprows=1)

Individual_minimum_transaction = data[:, 1]
Personal_average_price = data[:, 2]
Unit_minimum_transaction_price = data[:, 3]
Unit_average_transaction_price = data[:, 4]
Individual_minimum_transaction = Individual_minimum_transaction.astype(float)
Personal_average_price = Personal_average_price.astype(float)
Unit_minimum_transaction_price = Unit_minimum_transaction_price.astype(float)
Unit_average_transaction_price = Unit_average_transaction_price.astype(float)

x = np.linspace(1, 69, 69)
X = np.array(x).reshape(-1, 1)
y1 = Individual_minimum_transaction
y2 = Personal_average_price
y3 = Unit_minimum_transaction_price
y4 = Unit_average_transaction_price

plt.plot(x, y1, label="个人最低成交价", color="r", linewidth=0.5)
plt.plot(x, y2, label="个人平均成交价", color="y", linewidth=0.5)
plt.plot(x, y3, label="单位最低成交价", color="b", linewidth=0.5)
plt.plot(x, y4, label="单位平均成交价", color="g", linewidth=0.5)
plt.scatter(x, y1, color="r", marker='.')
plt.scatter(x, y2, color="y", marker='.')
plt.scatter(x, y3, color="b", marker='.')
plt.scatter(x, y4, color="g", marker='.')

plt.legend()
plt.grid(True)
# plt.savefig("车牌价格.pdf")
plt.show()

# 数据
# date,Individual_minimum_transaction_price,Personal_average_price,Unit_minimum_transaction_price,Unit_average_transaction_price
# 2012/8/28,10000,22822,10000,25515
# 2012/9/25,10000,14138,10000,15978
# 2012/10/25,10000,11067,10000,12674
# 2012/11/26,10000,10779,10000,12575
# 2012/12/25,10000,10955,10000,12303
# 2013/1/25,10000,10854,10000,12583
# 2013/2/25,10000,10573,10000,11762
# 2013/3/25,10000,10585,10000,11688
# 2013/4/25,10000,10998,10000,12017
# 2013/5/27,11600,12627,10000,12548
# 2013/6/25,14000,15743,10000,13117
# 2013/7/25,18700,20631,12500,14789
# 2013/8/26,23900,26599,15100,17385
# 2013/9/25,10000,30802,18000,20643
# 2013/10/25,10000,16384,10000,19510
# 2013/11/25,10000,11813,10000,14304
# 2013/12/25,10700,11959,10000,12958
# 2014/1/26,11500,12541,10000,12601
# 2014/2/25,11600,12777,10000,12494
# 2014/3/27,12300,13085,10300,12203
# 2014/4/26,13100,14074,10800,12452
# 2014/5/27,14500,15391,11000,12902
# 2014/6/26,16000,17024,10000,13134
# 2014/7/25,14800,18310,10000,12845
# 2014/8/26,10000,16654,10000,12375
# 2014/9/25,10000,12382,10000,11997
# 2014/10/25,10000,11442,10000,11836
# 2014/11/25,10000,11207,10000,11614
# 2014/12/25,10300,11421,10000,11604
# 2015/1/25,12000,13137,10000,11882
# 2015/2/25,13200,14331,10000,12391
# 2015/3/25,14500,15436,10000,11883
# 2015/4/27,16800,17798,10000,11593
# 2015/5/25,20200,21506,10000,11604
# 2015/6/25,26000,27672,10000,11822
# 2015/7/27,35000,37805,10000,12152
# 2015/8/25,10000,36231,10000,11878
# 2015/9/25,13500,16886,10000,11590
# 2015/10/26,16000,17487,10000,11254
# 2015/11/25,19000,20609,10000,11811
# 2015/12/25,24600,27077,10000,12009
# 2016/1/25,21000,25727,10000,12106
# 2016/2/25,19500,21884,10000,11560
# 2016/3/25,21100,23315,10000,11513
# 2016/4/25,23800,25701,10000,11496
# 2016/5/25,25000,27127,10000,11186
# 2016/6/27,23400,28541,10000,11420
# 2016/7/25,10100,24324,10000,11355
# 2016/8/25,15100,17330,10000,11114
# 2016/9/26,18100,19614,10000,11277
# 2016/10/25,19500,21551,10000,11269
# 2016/11/25,18600,22300,10000,11427
# 2016/12/26,15300,20591,10000,10905
# 2017/1/25,15100,17508,10000,11093
# 2017/2/28,15900,17419,10000,11114
# 2017/3/27,17300,18358,10000,10945
# 2017/4/25,18900,20127,10000,11061
# 2017/5/25,21500,22996,10000,11063
# 2017/6/26,23900,25498,10000,11136
# 2017/7/25,25000,26668,10100,11170
# 2017/8/25,26800,28561,10800,11663
# 2017/9/25,28800,30535,11800,15659
# 2017/10/25,30000,32449,13800,18038
# 2017/11/27,30700,34046,16800,18982
# 2017/12/25,18000,32312,24000,26123
# 2018/1/25,21000,25213,28000,30832
# 2018/2/26,22800,24560,32200,34718
# 2018/3/26,25300,26939,39100,41653
# 2018/4/25,32100,34455,51000,56158
