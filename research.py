from xml.dom.minidom import parse
import xml.dom.minidom
 
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(".\P.xml")
collection = DOMTree.documentElement
s='string'
# 在集合中获取所有词语
items = collection.getElementsByTagName("item")

for k in range(1,10) :
    s=input("请输入词语：")
    s=s+"/n"
    print (s)
    # 打印每个词语的详细信息
    flag=1
    for item in items:
        #if item.hasAttribute("title"):
        name = item.getElementsByTagName('name')[0]
        # print ("name: %s" % name.childNodes[0].data)
        #print ("Title: %s" % movie.getAttribute("title"))
        sons = item.getElementsByTagName('son')
        for son in sons:
            son_name = son.getElementsByTagName('son_name')[0]
            #print ("name: %s" % name.childNodes[0].data)
            if(son_name.childNodes[0].data==s):
                print ("*****item*****")
                print ("name: %s" % name.childNodes[0].data)
                print ("  son name: %s" % son_name.childNodes[0].data)
                rank = son.getElementsByTagName('son_rank')[0]
                print ("  son rank: %s" % rank.childNodes[0].data)
                score = son.getElementsByTagName('son_score')[0]
                print ("  son score: %s \n" % score.childNodes[0].data)
                flag=0
    if flag ==1 :
        print ("无匹配项！")
    
