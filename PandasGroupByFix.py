df=pd.DataFrame({
    'a': ['aa', 'a2', 'a3'],
    'b': [1, 2, 3],
}, index=pd.Index([1., 2., 3.]))

def groupByEval(df,groupByColumn,targetColumn):
    dataList = []
    indexList = [groupByColumn]
    for i in set(df[groupByColumn]):
        dataList.append(df[df[groupByColumn] == i][targetColumn].mean())
        indexList.append(i)
    df = pd.DataFrame({'{}_mean'.format(targetColumn):dataList},index=indexList[1:])
    df.index.name = indexList[0]
    
    return df
	
	
print(groupByEval(df,'a','b'))
