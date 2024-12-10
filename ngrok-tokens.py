import yaml
import getpass


try:
    with open("tokens.yml","r") as tokens_yaml:
        yaml_decode_tokens=yaml.safe_load(tokens_yaml)
        
        tokens=yaml_decode_tokens["tokens"]
        index=0

        print("tokens available: ")
        for token_item in tokens:
            index = index + 1
            print(str(index) + " - " + str(token_item))

        
        index_token = int(input("which token do you want to load? "))

        if index_token < 1 or index_token > index:
            print("Operation aborted due to wrong value used for retrieving token from the menu")
        else:    
            token_defenitive = tokens[int(index_token)-1]

            user=getpass.getuser()
            
            with open("/home/{}/.config/ngrok/ngrok.yml".format(user),"w") as ngrok_yaml_hacked:
                ngrok_object = {"version":"3","agent":{"authtoken":"{}".format(token_defenitive)}}
                yaml.safe_dump(ngrok_object,ngrok_yaml_hacked)
                
                

except Exception as e:
    print("An Exception happened")
    print(e)
