from xml.dom.minidom import parse
import xml.dom.minidom
 
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(".\master_mission\eg.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element :") 
   print (collection.getAttribute("shelf"))
 
# 在集合中获取所有子节点
contents = collection.getElementsByTagName("content")
 
# 打印详细信息
for content in contents:
   print ("*****content*****")
   if content.hasAttribute("title"):
      print ("Title: %s" % content.getAttribute("title"))
 
   rank = content.getElementsByTagName('rank')[0]
   print ("rank: %s" % rank.childNodes[0].data)
   score = content.getElementsByTagName('score')[0]
   print ("Fscore: %s" % score.childNodes[0].data)
