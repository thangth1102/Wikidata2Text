from mapping_estimation import *

input_file_name = 'output_common2.csv'
df = pd.read_csv(input_file_name, delimiter='#', dtype=dtypes, usecols=list(dtypes))

evaluate_qualifier_matching_type(df, 'wikidata')
evaluate_qualifier_matching_type(df, 'wikidata', 1)
evaluate_qualifier_matching_type(df, 'wikidata', 2)

