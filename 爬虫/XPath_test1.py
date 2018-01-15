#encoding=utf-8
#__author__:Chen bolin

from lxml import etree

# # 方法一：验证lxml可以直接修正字符串类型
# text = """
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
# </div>
#        """

# html = etree.HTML(text)
# result = etree.tostring(html)
# print(type(text))
# print(result)
# print(type(result))


#方法二：文件读取
html = etree.parse("./test_XPath.html")
# html = etree.parse("../html文件/test_XPath.html")
result = etree.tostring(html,pretty_print=True)
print(result)
