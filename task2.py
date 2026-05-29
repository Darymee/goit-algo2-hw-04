from trie import Trie


class Homework(Trie):

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("pattern must be a string")

        count = 0

        def dfs(node, word):
            nonlocal count

            if node.value is not None and word.endswith(pattern):
                count += 1

            for ch, child in node.children.items():
                dfs(child, word + ch)

        dfs(self.root, "")
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
