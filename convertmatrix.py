import pandas as pd

def convert_matrix(file_name, xcolname, ycolname, valcolname):
    df = pd.read_csv(file_name, index_col = 0)

    rows_list = []
    for i in df.columns:
        for j in df.index:
            rows_list.append([i, j, df.loc[j, i]])
    
    output_df = pd.DataFrame(rows_list, columns = [xcolname, ycolname, valcolname])

    return output_df

def main():
    df = convert_matrix('HICPMatrix.csv', 'year', 'Country', 'HICP')
    df = df.astype({'year': int})

    countries = df['Country'].unique()
    years = df['year'].unique()
    for country in countries:
        for year in years:
            cpi_2015 = df.loc[(df['Country'] == country) & (df['year'] == 2015), 'HICP'].values[0]
            cpi_current = df.loc[(df['Country'] == country) & (df['year'] == year), 'HICP'].values[0]
            df.loc[(df['Country'] == country) & (df['year'] == year), 'InflationAdjFactor'] = cpi_2015 / cpi_current

    df.to_csv('InflationAdjFactors.csv')

if __name__ == '__main__':
    main()