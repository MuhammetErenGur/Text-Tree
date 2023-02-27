

text="""Gestures, like panning or scrolling, and other events can map directly to animated values using Animated.event(). This is done with a structured map syntax so that values can be extracted from complex event objects. The first level is an array to allow mapping across multiple args, and that array contains nested objects.

Animated.event()

For example, when working with horizontal scrolling gestures, you would do the following in order to map event.nativeEvent.contentOffset.x to scrollX (an Animated.Value):"""


class StringTree:
    def __init__(self,text):
        self.text=text
        self.children=[]
        self.parent=None

    def addChild(self,child):
        child.parent=self
        self.children.append(child)




def buildTree(text):
    root=StringTree(text)
    paragraphs=text.split("\n\n")
    for i in range(len(paragraphs)):
        root.addChild(StringTree(paragraphs[i]))
        sentences=paragraphs[i].split(".")
        for  j in range(len(sentences)):
            root.children[i].addChild(StringTree(sentences[j]))
            words=sentences[j].split(" ")
            for k in range(len(words)):
                root.children[i].children[j].addChild(StringTree(words[k]))
    return root



root=buildTree(text)



