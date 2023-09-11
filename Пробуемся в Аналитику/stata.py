import pandas as pd
click_index = ['id', 'offerId', 'advertiserId', 'webmasterId', 'createDate',
       'isUniqueCookie', 'isUniqueHost', 'clientId', 'trafficBackId', 'sub1',
       'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10',
       'clientUuid', 'phoneNumber', 'sourceOfferId', 'sharedWebmasterId',
       'offerLinkId', 'redirectUrl', 'parentId', 'sharingMixProbability']

conversion_index = ['id', 'clickId', 'webmasterId', 'offerConversionId', 'goalId',
       'goalType', 'sumIncome', 'sumWebmaster', 'currency', 'status',
       'comment', 'createDate', 'updateDate', 'holdoutDate', 'attributionDate',
       'updateSource', 'statusChangeDate', 'sub1', 'sub2', 'sub3', 'sub4',
       'sub5', 'sub6', 'sub7', 'sub8', 'sub9', 'sub10', 'offerId',
       'advertiserId', 'offerName', 'clickDate', 'phoneNumber',
       'sourceOfferId', 'isRevise', 'sumRefBack', 'sharedWebmasterId',
       'offerLinkId', 'clientId', 'clientUuid', 'parentId',
       'sharingMixProbability']



df_click = pd.read_csv("/Users/kuzin/Downloads/04_click.csv", low_memory=False)
df_conversion = pd.read_csv("/Users/kuzin/Downloads/04_05_conversion.csv", low_memory=False)


df_merge = df_click.merge(df_conversion, left_on='id', right_on='clickId', how='left', suffixes=('_click', '_conv'))

# result_df = df_merge.agg(
#     count_click=("id_click", lambda x: x.nunique()),
#     count_unique_lick=("isUniqueCookie_click", lambda x: x[x].count()),
#     count_unique_host=("isUniqueHost_click", lambda x: x[x].count()),
#     count_conversions=("id_click_conv", "count"),
#     approve=("status_conv", lambda x: x[x == 1].count()),
#     pending=("status_conv", lambda x: x[x == 0].count()),
#     rejected=("status_conv", lambda x: x[x == 2].count()),
#     AR=("id", lambda x: (x[x == 1].count() / x.count()) * 100),
#     CR=("id", lambda x: x.count() / x[x].nunique() * 100),
#     total_Webu=("sumWebmaster_conv", lambda x: x[x.status == 1].sum()),
#     EPL_Webs=("sumWebmaster_conv", lambda x: x[x.status == 1].sum() / x[x == 1].count()),
#     EPC_Webs=("sumWebmaster_conv", lambda x: x[x.status == 1].sum() / x[x.isUniqueCookie].nunique()),
#     EPC_Webs_host=("sumWebmaster_conv", lambda x: x[x.status == 1].sum() / x[x.isUniqueHost].nunique())
# )

result_df = df_merge.groupby('offerId_click').agg({'id_click': 'count', 'id_conv': 'count'})
result_df.rename(columns={'id_click': 'count_click', 'id_conv': 'count_conversion'}, inplace=True)
result_df['AR'] = result_df['count_click'] / result_df['count_conversion']
print(result_df.reset_index())



