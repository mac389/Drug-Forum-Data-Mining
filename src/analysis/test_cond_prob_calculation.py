import pandas as pd

df = pd.DataFrame([[1,2,3],[2,3,4],[3,4,5],[1,2,4]], 
		columns = ['a','b','c'],index=['d','e','f','g'])

def from_occurences_to_conditional_probs(df):
	baseline_probabilities = df.sum(axis=1)/(df.sum(axis=1).sum())
	#rows contain variable conditioning on p(col | row)
	overall_sum = df.sum().sum()
	print baseline_probabilities

	conditional_prob_df = df.copy(deep=True)
	conditional_prob_df /= overall_sum
	conditional_prob_df = conditional_prob_df.divide(baseline_probabilities, axis=0)

	return conditional_prob_df

#print df
x = from_occurences_to_conditional_probs(df)
df1 = x.stack().rename_axis(('conditioning event','event')).reset_index(name='probabilitiy')

print df1