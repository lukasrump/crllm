from crllm.code.loaders.file import file


def test_file_loader():
    assert file("./src/crllm/test/functional/code/loaders/file/foo.txt") == "bar"
