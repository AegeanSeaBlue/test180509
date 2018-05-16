import pandas as pd

city_code = pd.read_csv('city_codes_lat_long.csv')
# city_code = city_code.sort_values(by=['COUNTRY', 'LATITUDE'], ascending=[False, False]).head(n=20)
# print(city_code)
# city_code.to_csv('city_code.csv', index=False, header=True, encoding='utf-8')
# city_code = city_code.groupby(['COUNTRY'])
