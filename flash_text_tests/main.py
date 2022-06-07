from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor(case_sensitive=False)
#case_sensitive determina se o FlashText avaliará se a palavra possui caracteres maiúsculos ou minúsculos

keyword_dictionary = {
    'Programador': ['Desenvolvedor', 'Trabalhador', 'Developer', 'Engenheiro']
}
#a key do dicionário é a replacementWord; os values são as keywords e serão substituídos por ela.

keyword_processor.add_keywords_from_dict(keyword_dictionary)
#basta isso para adicionar o dicionário ao processador

keywords_found2 = keyword_processor.extract_keywords(
    'Desenvolvedor Programador Engenheiro Trabalhador Developer Dentista Maratonista'
)
#O FlashText encontra as unclean words e as substitui.
#Observe que ela não identifica a palavra Programador na string, mesmo sendo a keyword.
print(keywords_found2)
# ['Programador', 'Programador', 'Programador', 'Programador']

keyword_processor.add_keyword('Python', 'Back-End') #Python é a Keyword e 'BE LANGUAGE' é a replacementWord
keyword_processor.add_keyword('Django', 'API') #Idem acima
keywords_found = keyword_processor.extract_keywords('I love PyThOn and DJaNgO.') #observe o case sem fazer efeito
print(keywords_found)
# ['BE LANGUAGE', 'API']

keyword_processor.add_keyword('HTML', 'Front-End')
new_sentence = keyword_processor.replace_keywords('I love Python, HTML and DJANGO.')
print(new_sentence)
# 'I love Back-End, Front-End and API.'

kp = KeywordProcessor()
kp.add_keyword('Python', ('Linguagem Back-End', 'Python')) #você pode adicionar uma informação na sua consulta
kp.add_keyword('HTML', ('Linguagem Front-End', 'HTML'))
print(kp.extract_keywords('Se você quiser aprender Python, conte comigo. Se prefere HTML, consulte o Youtube.'))
# [('Linguagem Back-End', 'Python'), ('Linguagem Front-End', 'HTML')]
# A função replace_word não funciona com isso.

kc = KeywordProcessor(case_sensitive=False)
kc.add_keyword_from_file('constituicao_federal.txt')
print(len(kc))
# adicionei os termos da constituição federal como keywords
# '3755'