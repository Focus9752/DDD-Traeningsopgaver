           #           
          ###          
         #####         
        #######        
       #########       
      ###########      
     #############     
    ###############    
   #################   
  ###################  
 ##################### 
#######################

def main():
    christmastree = [
    "#", 
    "###", 
    "#####", 
    "#######", 
    "#########", 
    "###########", 
    "#############", 
    "###############", 
    "#################", 
    "###################",
    "#####################",
    "#######################"
    ]

    D = int(input())

    tempString = ""
    offSet = 0
    for i in range(1, int((D + 1) / 2) + 1):
        tempString += " " * int((((D + 1) / 2) - i))
        tempString += "#" * (1 + (i - 1) * 2)
        print(tempString)
        tempString = ""
        

main()