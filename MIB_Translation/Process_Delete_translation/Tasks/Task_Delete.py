import os

from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()

context = Variables.task_call(dev_var)

gen_file = context['translated_oid_file_name']
if os.path.isfile(gen_file):
    os.unlink(gen_file)

ret = MSA_API.process_content('ENDED', f'File {gen_file} deleted', context, True)
print(ret)

