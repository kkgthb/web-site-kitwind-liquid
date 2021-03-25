import os
[print("{%- include 'components/kitwind_all/contents/" + x.split('.')[0] + "' section:section_comprehensive -%}\r\n") for x in os.listdir('./src/_includes/components/kitwind_all/contents')]