import jupyter_to_medium as jtm
import os

jtm.publish('october_2020/cleaning_categorical_data/cleaning_categorical_data.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title=None,
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
