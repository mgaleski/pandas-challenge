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
function gathering most popular items
'''

top_items = purchase_df['Item Name'].value_counts()[:3].index.tolist()


for i in (0,6):
    top_items_df.append(purchase_df['Item Name' == top_items[i]

        


with open('summary_report.txt','w') as file:
    file.write('Summary Report:\n')
    file.write('------------------------------\n')
    file.write(f'Unique Player Count: {playercnt}\n')
    file.write('------------------------------\n')
    file.write('Purchase Analysis:\n')
    file.write(f'Unique Items: {itemcnt}\n')
    file.write(f'Average Purchase Price: ${avg_purchase}\n')
    file.write(f'Number of Purchases: {purchase_count}\n')
    file.write(f'Total Revenue: ${total_revenue}\n')
    file.write('------------------------------\n')
    file.write('Gender Demographics:\n')
    file.write(f'Male Players: {male_pct}% ({male_playercnt})\n')
    file.write(f'Female Players: {female_pct}% ({female_playercnt})\n')
    file.write(f'Other Players: {other_pct}% ({other_playercnt})\n')
    file.write('------------------------------\n')
    file.write('Purchasing Analysis (Gender):\n')
    file.write(f'Male Purchases: {male_purchase_count}\n')
    file.write(f'Female Purchases: {female_purchase_count}\n')
    file.write(f'\n')
    file.write(f'Male Average Purchase: ${male_purchase_avg}\n')
    file.write(f'Female Average Purchase: ${female_purchase_avg}\n')
    file.write('\n')
    file.write(f'Male Purchase Total: ${male_purchase_total}\n')
    file.write(f'Female Purchase Total: ${female_purchase_total}\n')
    file.write('------------------------------\n')
    file.write('Age Demographics:\n')
    file.write('------------------------------\n')
    file.write('Top Spenders:\n')
    file.write('------------------------------\n')
    file.write('Most Popular Items:\n')
    file.write('------------------------------\n')
    file.write('Most Profitable Items:\n')
    file.write('------------------------------\n')
    
    
    