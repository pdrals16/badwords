# %%
import os
import pandas as pd

os.chdir('..')

from src.core.badwords_filter import BadwordsFilter
# %%
badwords = pd.read_csv('reference/badwords.csv')
list_badwords = badwords['Word'].to_list()

badwords_filter = BadwordsFilter(language='pt',
                                list_badwords=list_badwords)
# %%
badwords_filter.censor('Voce é uma v4c4')