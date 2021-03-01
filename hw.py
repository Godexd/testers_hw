import docdir


class Tester:

    def test_add_doc_to_shelf(self):
        shelf_before = len(docdir.directories['3'])
        docdir.append_doc_to_shelf('123', '3')
        assert shelf_before + 1 == len(docdir.directories['3'])

    def test_remove_doc_from_shelf(self):
        docs_before = sum([len(value) for value in docdir.directories.values()])
        docdir.remove_doc_from_shelf('11-2')
        assert docs_before - 1 == sum([len(value) for value in docdir.directories.values()])

    def test_documents_existance(self):
        doc_exist = '2207 876234'
        doc_not_exist = '123'
        assert docdir.check_document_existance(doc_exist)
        assert not docdir.check_document_existance(doc_not_exist)