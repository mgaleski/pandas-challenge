import pandas as pd

csv_file = './Resources/purchase_data.csv'

purchase_df = pd.read_csv(csv_file)

for col in purchase_df.columns:
    print(col)
    
avg_purchase = round(purchase_df['Price'].mean(),2)
purchase_count = purchase_df['Purchase ID'].count()
total_revenue = purchase_df['Price'].sum()

playerlist = []
itemlist = []



'''
For loops creating lists of unique players and items
'''
for player in purchase_df['SN']:
    if player not in playerlist:
        playerlist.append(player)

for item in purchase_df['Item Name']:
    if item not in itemlist:
        itemlist.append(player)


'''
creates dataframes of male and female purchases
'''
male_purchases = purchase_df[purchase_df.Gender == 'Male']
female_purchases = purchase_df[purchase_df.Gender == 'Female']


male_playerlist = []
female_playerlist = []
other_playerlist = []

for player in male_purchases['SN']:
    if player not in male_playerlist:
        male_playerlist.append(player)

for player in female_purchases['SN']:
    if player not in female_playerlist:
        female_playerlist.append(player)


'''
counts of players and items
'''

playercnt = len(playerlist)
itemcnt = len(itemlist)

male_playercnt = len(male_playerlist)
female_playercnt = len(female_playerlist)
other_playercnt = playercnt - male_playercnt - female_playercnt

male_pct = round(male_playercnt*100/playercnt,2)
female_pct = round(female_playercnt*100/playercnt,2)
other_pct = round(other_playercnt*100/playercnt,2)




'''
analysis variables
'''
male_purchase_count = male_purchases['Purchase ID'].count()
female_purchase_count = female_purchases['Purchase ID'].count()

male_purchase_total = male_purchases['Price'].sum()
female_purchase_total = female_purchases['Price'].sum()
male_purchase_avg = round(male_purchases['Price'].mean(),2)
female_purchase_avg = round(female_purchases['Price'].mean(),2)

'''
creates dfs for age bins
'''

bin1_df = purchase_df[purchase_df.Age < 10]

bin1_count = bin1_df['Purchase ID'].count()
bin1_mean = round(bin1_df['Price'].mean(),2)
bin1_sum = bin1_df['Price'].sum()


bin2_df = purchase_df[purchase_df.Age > 9]
bin2_df = bin2_df[bin2_df.Age < 15]

bin2_count = bin2_df['Purchase ID'].count()
bin2_mean = round(bin2_df['Price'].mean(),2)
bin2_sum = bin2_df['Price'].sum()


bin3_df = purchase_df[purchase_df.Age > 14]
bin3_df = bin3_df[bin3_df.Age < 20]

bin3_count = bin3_df['Purchase ID'].count()
bin3_mean = round(bin3_df['Price'].mean(),2)
bin3_sum = bin3_df['Price'].sum()


bin4_df = purchase_df[purchase_df.Age > 19]
bin4_df = bin4_df[bin4_df.Age < 25]

bin4_count = bin4_df['Purchase ID'].count()
bin4_mean = round(bin4_df['Price'].mean(),2)
bin4_sum = bin4_df['Price'].sum()



'''
function gathering most popular items
'''


top_items_df = purchase_df['Item Name'].value_counts()[:5].index.tolist()

   
with open('summary_report.txt','w') as fileh:
    fileh.write('test')
    fileh.write('------------------------------\n')
    fileh.write(f'Unique Player Count: {playercnt}\n')
    fileh.write('------------------------------\n')
    fileh.write('Purchase Analysis:\n')
    fileh.write(f'Unique Items: {itemcnt}\n')
    fileh.write(f'Average Purchase Price: ${avg_purchase}\n')
    fileh.write(f'Number of Purchases: {purchase_count}\n')
    fileh.write(f'Total Revenue: ${total_revenue}\n')
    fileh.write('------------------------------\n')
    fileh.write('Gender Demographics:\n')
    fileh.write(f'Male Players: {male_pct}% ({male_playercnt})\n')
    fileh.write(f'Female Players: {female_pct}% ({female_playercnt})\n')
    fileh.write(f'Other Players: {other_pct}% ({other_playercnt})\n')
    fileh.write('------------------------------\n')
    fileh.write('Purchasing Analysis (Gender):\n')
    fileh.write(f'Male Purchases: {male_purchase_count}\n')
    fileh.write(f'Female Purchases: {female_purchase_count}\n')
    fileh.write(f'\n')
    fileh.write(f'Male Average Purchase: ${male_purchase_avg}\n')
    fileh.write(f'Female Average Purchase: ${female_purchase_avg}\n')
    fileh.write('\n')
    fileh.write(f'Male Purchase Total: ${male_purchase_total}\n')
    fileh.write(f'Female Purchase Total: ${female_purchase_total}\n')
    fileh.write('------------------------------\n')
    fileh.write('Age Demographic:\n')
    fileh.write('\n')
    fileh.write('Purchase Count:\n')
    fileh.write(f'Bin 1: {bin1_count}\n')
    fileh.write(f'Bin 2: {bin2_count}\n')
    fileh.write(f'Bin 3: {bin3_count}\n')
    fileh.write(f'Bin 4: {bin4_count}\n')
    fileh.write('\n')
    fileh.write('Avg Purchase:\n')
    fileh.write(f'Bin 1: ${bin1_mean}\n')
    fileh.write(f'Bin 2: ${bin2_mean}\n')
    fileh.write(f'Bin 3: ${bin3_mean}\n')
    fileh.write(f'Bin 4: ${bin4_mean}\n')
    fileh.write('\n')
    fileh.write('Total Purchases:\n')
    fileh.write(f'Bin 1: ${bin1_sum}\n')
    fileh.write(f'Bin 2: ${bin2_sum}\n')
    fileh.write(f'Bin 3: ${bin3_sum}\n')
    fileh.write(f'Bin 4: ${bin4_sum}\n')
    fileh.write('------------------------------\n')
    fileh.write('Top Spenders:\n')
    fileh.write('------------------------------\n')
    fileh.write('Most Popular Items:\n')
    fileh.write(f'1. {top_items_df[0]}\n')
    fileh.write(f'2. {top_items_df[1]} (tie)\n')
    fileh.write(f'3. {top_items_df[2]}\n')
    fileh.write(f'4. {top_items_df[3]}\n')
    fileh.write(f'5. {top_items_df[4]}\n')
    fileh.write('------------------------------\n')
    fileh.write('Most Profitable Items:\n')
    fileh.write('------------------------------\n')


