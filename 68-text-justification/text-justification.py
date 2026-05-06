class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0 # with no space

        for word in words:
            # already add + curr word + space
            '''
            ["This", "is", "an"]
            需要 2 个空格 = len(line) - 1
            但在“尝试加入新词”时，相当于已经多一个间隙，所以用 len(line)
            '''
            # can't add one more word
            if line_len + len(word) + len(line) > maxWidth:
                # how many spaces need to be added
                spaces = maxWidth - line_len
                gaps = len(line) - 1

                # case 1: if one word line
                if gaps == 0:
                    # add spaces in the end
                    res.append(line[0] + ' ' * spaces)

                # case 2: multi words
                else:
                    space_each = spaces // gaps
                    extra = spaces % gaps
                    
                    # distribute extra space from left to right
                    for i in range(extra):
                        line[i] += ' '
                    
                    # Concatenate
                    # word + "    " + word + "    " + word
                    res.append((' ' * space_each).join(line))
                
                # reset, next line
                line = []
                line_len = 0
            
            # add current word
            line.append(word)
            line_len += len(word)
        
        # last line（left-justified）
        last_line = ' '.join(line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return res
