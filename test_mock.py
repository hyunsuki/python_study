from unittest.mock import Mock
from icecream import ic


class MockManager:

    def __init__(self): pass

    def returnValueMock(self, value):
        return Mock(return_value=value)()

    def returnExceptionMock(self, exception_message):
        return Mock(side_effect=Exception(exception_message))()

    def returnKeyErrorMock(self, error_message):
        return Mock(side_effect=KeyError(error_message))()

    def returnIterMock(self, iter_):
        return Mock(side_effect=iter_)

    def returnMultiplyTenMock(self, x):
        return Mock(side_effect=lambda x:x * 10)(x)

    def createMock(self):
        return Mock()

def main():
    mm = MockManager()
    ic(mm.returnValueMock('Hello, Mock!'))
    mock_iter = mm.returnIterMock([1, 2, 3])
    ic(mock_iter())
    ic(mock_iter())
    ic(mock_iter())
    ic(mm.returnMultiplyTenMock(1))
    mock_vo = mm.createMock()
    mock_vo.return_value = 1
    ic(mock_vo())
    mock = Mock()
    mock.attribute = 'ATTRIBUTE'
    ic(mock.attribute)
    mock.method.return_value = 'METHOD RETURN VALUE'
    ic(mock.method())
    ic(mm.returnExceptionMock('Oops!'))
    ic(mm.returnKeyErrorMock('foo'))

if __name__ == '__main__':
    main()


