import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if response.status_code == 200 :
    pullrequests = response.json()

    pr_creators = {}

    for pull in pullrequests:
    
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] +=1
        else:
            pr_creators[creator] =1

    for creator,count in pr_creators.items():
        print(f" {creator}:{count}")

else:
    print(f"Error: {response.status_code}")
