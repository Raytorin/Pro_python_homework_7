class Stack:
    items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print('stack empty')
            raise IndexError

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            print('stack empty')
            raise IndexError

    def size(self):
        return len(self.items)


def check(input_data):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    zip_tup = dict(zip(open_tup, close_tup))

    for data in input_data:
        if data in open_tup:
            new_stack.push(zip_tup[data])
        elif data in close_tup:
            if new_stack.is_empty() or data != new_stack.pop():
                return 'Unbalanced'
    if new_stack.is_empty():
        return 'Balanced'
    else:
        return 'Unbalanced'


if __name__ == "__main__":
    new_stack = Stack()

    pack = ''
    print(check(pack))
