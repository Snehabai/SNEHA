def balaji():
     return "this is my bank balance"
test_dict={"fname":balaji,"age":50,"address":"salem"}
print("the original dictionary is :"+ str(test_dict))
res=test_dict['fname']()
print("the required call result:"+str(res))


