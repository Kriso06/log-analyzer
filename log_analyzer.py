import re #parsing messy text patterns
import pandas as pd #store analyze data in tables
import matplotlib.pyplot as plt 

#build a regex pattern that matches each part
log_pattern=re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+)\s(?P<url>\S+)\s*(?P<protocol>\S+)?" (?P<status>\d{3}) (?P<size>\S+)'
)

#(?P<>) creates a group 
#\S+ one or more non-space char
#.*? grab everything lazily until next bracket closes
#\s* zero or more spaces

logs=[]
with open("access.log", encoding="utf-8", errors="ignore") as f:
    for line in f:
        match=log_pattern.match(line) #returns a match object if pattern fits else None
        if match:
            logs.append(match.groupdict()) #match.groupdict() converts data into a dict, groupname:value

df=pd.DataFrame(logs) #convert list of dict into panda data frame like an excel table
df["status"]=df["status"].astype(int) #convert status col from string to int
df["size"]=df["size"].replace("-",0).astype(int) 

#verify
print("Number of Parsed Entries: ", len(df))
print(df.head())

stat_count=df["status"].value_counts()
top_stat_count=stat_count.head(10)
top_stat_count.plot(kind="bar")
plt.title("Top HTTP Status Codes")
plt.xlabel("Status Code")
plt.ylabel("Count")
plt.show()