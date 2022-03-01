class Storage:
    def __init__(self):
        self.__is_appendable = False
        self.__data = []

    def show(self):
        return self.__data

    def append(self, odj):
        if self.__is_appendable:
            self.__data.append(odj)
        else:
            print('storage close')

    def lock(self):
        self.__is_appendable = False

    def unlock_(self):
        self.__is_appendable = True

    def __enter__(self):
        assert not self.__is_appendable, 'object is already open for recording'
        self.unlock_()
        print('open')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lock()
        print('close')


if __name__ == "__main__":
    storage = Storage()
    storage.append(12345)

    with Storage() as st:
        st.append('abc')
        print(st.show())
        st.append({3: 5, 6: 8})
        print(st.show())

    storage.unlock_()
    with storage:
        st.append('qwer')