from xml.dom.minidom import parse
import xml.dom.minidom
 
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(".\P.xml")
collection = DOMTree.documentElement
s='string'
# 在集合中获取所有词语
items = collection.getElementsByTagName("item")
 
# 打印每个词语的详细信息
for item in items:
    print ("*****item*****")
    #if item.hasAttribute("title"):
    name = item.getElementsByTagName('name')[0]
    print ("name: %s" % name.childNodes[0].data)
    #print ("Title: %s" % movie.getAttribute("title"))
    sons = item.getElementsByTagName('son')
    for son in sons:
        name = son.getElementsByTagName('son_name')[0]
        print ("  son name: %s" % name.childNodes[0].data)
        rank = son.getElementsByTagName('son_rank')[0]
        print ("  son rank: %s" % rank.childNodes[0].data)
        score = son.getElementsByTagName('son_score')[0]
        print ("  son score: %s \n" % score.childNodes[0].data)
