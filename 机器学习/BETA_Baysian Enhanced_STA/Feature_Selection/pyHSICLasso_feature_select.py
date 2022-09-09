# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 15:23
# @Author  : Ronchy_LU
# @Email   : rongqi1949@gmail.com
# @File    : pyHSICLasso_feature_select.py
# @Software: PyCharm
# @Github_link: https://github.com/riken-aip/pyHSICLasso

from pyHSICLasso import HSICLasso
hsic_lasso = HSICLasso()

# hsic_lasso.input("timing1500x14_del_first_col.csv",output_list=['Corner7','Corner8','Corner9','Corner10','Corner11','Corner12','Corner13','Corner14'])
hsic_lasso.input("timing1500x14_del_first_col.csv",output_list=['Corner11'])
# hsic_lasso.regression(num_feat=6, B=0, M=1)
hsic_lasso.regression(num_feat=5)
# hsic_lasso.plot()
hsic_lasso.dump()

hsic_lasso.get_index()
hsic_lasso.get_index_score()
hsic_lasso.get_index_score()
hsic_lasso.get_features()




