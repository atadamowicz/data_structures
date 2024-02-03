class BSTNode:
    def exists(self, val):
        if not self.val:
            return False
        if val == self.val:
            return True
        elif val < self.val:
            if self.left:
                return self.left.exists(val)
            else:
                return False
        else:
            if self.right:
                return self.right.exists(val)
            else:
                return False


    def __init__(self, val=None):
        self.left = None
        self.right = None
        if val is not None:
            self.val = val

    def insert(self, val):
        if self.val is None and val is not None:
            self.val = val
        elif val is not None:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = BSTNode(val)
            elif val > self.val:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = BSTNode(val)

    def delete(self, val):
        if self.val is None:
            return self

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:  
            if not self.left:
                return self.right
            elif not self.right:
                return self.left

            min_val = self.right.find_min()
            self.val = min_val
            self.right = self.right.delete(min_val)

        return self



    def find_min(self):
        if not self.left:
            return self.val
        return self.left.find_min()
