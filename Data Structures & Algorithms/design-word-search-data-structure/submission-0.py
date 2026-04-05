class TrieNode:
    def __init__(self):
        self.children={}
        self.wordEnd=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for s in word:
            if s not in cur.children:
                cur.children[s]=TrieNode()
            cur=cur.children[s]
        cur.wordEnd=True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                s=word[i]

                if s == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if s not in cur.children:
                        return False
                    cur=cur.children[s]
            return cur.wordEnd

        return dfs(0, self.root)



