from telethon.sync import TelegramClient
import datetime
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

chats = ['zerodhain','cryptodubai7','AlgoBullsOfficial','RajnishTrade']

df = pd.DataFrame()


for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        for message in client.iter_messages(chat, offset_date=datetime.date.today() , reverse=True):
        # for message in client.iter_messages(chat, offset_date=datetime.date(2020, 1, 1) , reverse=True):
            print(message)
            data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}
            temp_df = pd.DataFrame(data, index=[1])
            df = pd.concat([df, temp_df], ignore_index=True)
print(df.head())

if(df.empty):
    print('No New Message Found!')
else:
    
    df['date'] = df['date'].dt.tz_localize(None)

    df.to_excel("data/data_{}.xlsx".format(datetime.date.today()), index=False)
