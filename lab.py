import pandas as pd

df = pd.read_csv('dining.csv')


#task_1
print('Part 1')
print(df.shape)
print((df.info)) 

#Task_2
print('part 2')
average_df = df[df['dining_hall'] == 'Brooks']
print(average_df.head())


#Task 3
print('part 3')
average_df ['average_coffee'] = average_df['coffee_consumed'] / average_df['swipes']
print(average_df.head())


#task 4
print('part 4')
sorted_df = average_df.sort_values(by='average_coffee', ascending=False)
print(sorted_df.head())


#saving part
sorted_df.to_csv("modified_dining.csv", index=False)
