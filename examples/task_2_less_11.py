import pandas as pd

# file = '../files/NISPUF17.csv'
# df = pd.read_csv(file, sep=',')
# # df['CBF_01'] = df['CBF_01'].replace(1, 'yes', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(2, 'no', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(77, 'dk', regex=True)
# # df['CBF_01'] = df['CBF_01'].replace(99, 'miss', regex=True)

# bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
# bm_tuple = (round(float(bm[1]), 1), round(float(bm[2]), 1))
# print(bm_tuple)



df = pd.read_csv('../files/NISPUF17.csv', sep=',')
bm = df.groupby('CBF_01')['P_NUMFLU'].mean()
print(round(float(bm[1]), 1), round(float(bm[2]), 1))