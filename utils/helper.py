def run_helper(config):
    print("Helping",config["Settings"]["user"])

def show_gamemodes(config):
    print("Avalable Game modes:")
    for gamemode in config["gamemodes"]:
        print("   ",gamemode,":",config["gamemodes"][gamemode]["help"])
    
