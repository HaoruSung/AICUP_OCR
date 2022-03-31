import re
def text_classify(texts):
    class_dic = {"None":0,"zh_char":1,"zh_str":2,"en":3,"zh_en":4}
    #None case
    if len(texts)== 0 or texts =="###":
        return class_dic["None"]
    #char case 
    if len(texts)== 1 :
        #zh
        if re.findall("[\u4e00-\u9FFF]",texts):
            return class_dic["zh_char"]
        else:
        #en
            return class_dic["en"]
    #zh_str case 
    if len(texts) == len(re.findall("[\u4e00-\u9FFF]",texts)):
        return class_dic["zh_str"]
    else:
        if(len(re.findall("[\u4e00-\u9FFF]",texts))!=0):
            return class_dic["zh_en"]
    #en case
    if len(texts)!= 0 and len(re.findall("[\u4e00-\u9FFF]",texts)) == 0:
        return class_dic["en"]
    print("Unexpected class",texts)
    
def sep_pts(points):
    pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8 = ([] for i in range(8))
    for elem in points:
        pt1.append(elem[0][0])
        pt2.append(elem[0][1])
        pt3.append(elem[1][0])
        pt4.append(elem[1][1])
        pt5.append(elem[2][0])
        pt6.append(elem[2][1])
        pt7.append(elem[3][0])
        pt8.append(elem[3][1])
    return  pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8 

#def box_includes(point1,point2):
	

if __name__ == "__main__":
	print("call as main")

