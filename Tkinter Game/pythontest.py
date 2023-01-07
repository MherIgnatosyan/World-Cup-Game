import os
def leaderboard_sort():
    lead_wind = open("leaderboard.txt" , "r")
    leaderb = lead_wind.read()
    leader_list = leaderb.split("\n")
    userreg = {}
    
    for i in range(len(leader_list)):
        leadersplit = leader_list[i].split(":")
        userreg[leadersplit[0]] = int(leadersplit[1])

    sortedusers = dict(sorted(userreg.items(), key=lambda x:x[1], reverse=True))
    list_values  =  list(sortedusers.keys())
    print(list_values[0])
 
leaderboard_sort()