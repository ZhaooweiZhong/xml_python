from __future__ import print_function, unicode_literals
from lxml import etree, objectify
from xml.etree import ElementTree as ET
from bosonnlp import BosonNLP
from xml.dom.minidom import parse
import xml.dom.minidom
E = objectify.ElementMaker(annotate=False)
E2 = objectify.ElementMaker(annotate=False)
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(".\master_mission\cmd.xml")
collection = DOMTree.documentElement
# 注意：在测试时请更换为您的API Token
nlp = BosonNLP('API Token')
s=['hello']
rules = collection.getElementsByTagName("RULE")
anno_tree = E.collection()
for rule in rules :
    ps = rule.getElementsByTagName("P")    
    for p in ps:
        s=p.childNodes[0].data
        result = nlp.suggest(s,15)
        i=1
        anno_tree2=E.item(
        E.name(s)
        )
        #anno_tree.append(anno_tree2)
        for score, word in result: 
            anno_tree3 = E.son(
                    E.son_item(
                        E.son_name(word),
                        E.son_rank(i),
                        E.son_score(score)
                    )
            )
            anno_tree2.append(anno_tree3)
            i = i + 1
        if i==1:
            anno_tree3 = E.son(
                    E.son_item(
                        E.son_name(s),
                        E.son_rank(i),
                        E.son_score(1)
                    )
            )
            anno_tree2.append(anno_tree3)
        anno_tree.append(anno_tree2)
etree.ElementTree(anno_tree).write("p1.xml", pretty_print=True)
