# Apriori-Algorithm Implementation In Python
Describing in details the importance of Apriori algorithm along with technical implementation of the algorithm itself

# In project implementation, we divide code over 3 files:

	1. Config.py
It consists of three sections:

•	Data Config: To select data directory and name of data file, number of your first attribute as it in the data file and name of the output csv file containing our attributes columns only.
•	Sorting of rules: To select sorting according to Lift or Leverage.
•	HTML style for rules: Css style code for styling output HTML file

	2. Utils.py
It consists of definition of all used functions in the project:

•	Data_extract: To extract specific attributes from a data file based on configuration done in config.py and return dataframe containing the attributes.

•	Support_lvl: Get support of each level by giving the dataframe and return list of dictionaries that contain support of each sub attribute.

•	Elimination_of_values: Elimination of values less than minimum support from list of dictionaries and return filtered list of dictionaries.

•	Elimination_of_columns: Elimination of empty columns in dataframe after elimination of values that less than minimum support as may some attributes that have no values exceeds the minimum support.

•	Make_combination: To make combinations between attributes to higher the level as it takes current level itemsets (K) and return next level (K+1).

•	Collective_fun: It takes Make_combination, Support_lvl, Elimination_of_values, Elimination_of_columns and returns lvl dataframe with only columns that exceeds minimum support.


•	Return_last_lvl_values: Return only last lvl all values with support greater than minimum support.

•	Return_support: Return support of specific combinations.

•	Confidence_of_rule: Calculate confidence of rule.

•	Lift_of_rule: Calculate lift of rule.

•	Leverage_of_rule: Calculate leverage of rule.

•	Make_rules_and_prioritize: Return all rules that have more than minimum confidence and prioritize them by lift or leverage descendingly.

•	DataFrame_to_HTML: Converting output rules in dataframe into an HTML.

	3. Main.py
To take User inputs and combine functions together:

•	User inputs: Take minimum support in fraction (as 0.4) or number of appearance (as 322) and minimum confidence in fraction (as 0.6) or percentages (as 70%).

•	Then calling four functions (data_extract, return_last_lvl_values, make_rules_and_prioritize, DataFrame_to_HTML) respectively.

# Demo video
https://youtu.be/8zoyAgUuWfo
