string_1=input('輸入一串密文:') #輸入一串加密過的字串，該字串由英文大寫組成
A=[] #設定一個空字列
A.append(string_1) #把輸入的字串加進空字列裡
section_1={chr(ord('D')+i):chr(ord('A')+i)for i in range(23)} #設定一個字典從D~Z，解釋為A~W
section_2={chr(ord('A')+i):chr(ord('X')+i)for i in range(3)} #設定另一個字典從A~C，解釋為X~Z

section_1.update(section_2) #把secion_2字典加入到secion_2字典裡

ee="" #設定一個空字串
for c in string_1: 
    if c!=' ': 
        ee+=section_1[c] #ee空字串加上藉由seecion_1解密的文本
    else:
        ee+=' ' #ee還是原來的空字串
print(ee) #輸出解密的文本