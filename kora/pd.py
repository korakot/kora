""" What I want to add to pandas 

Initially just ability to read and write to google sheet
"""

import os
import re
from pandas import *
import gspread_dataframe


def auth_gsheet():
    from google.colab import auth
    auth.authenticate_user()
    import gspread
    from oauth2client.client import GoogleCredentials as GC
    gsheet = gspread.authorize(GC.get_application_default())
    return gsheet


def gsheet_open(source):
    """ Open existing title/id/url, or create a new one
    
    Return the first sheet (sheet1)
    """
    g = auth_gsheet()
    # a URL ?
    if source.startswith('http'):
        return g.open_by_url(source).sheet1
    # a file_id ?
    if re.match(r'1[-\w]{43}$', source):
        return g.open_by_key(source).sheet1
    # otherwise, it's a title
    try:
        return g.open(source).sheet1
    except:
        return g.create(source).sheet1


def read_sheet(source, **kw):
    """ Imitate pd.read_csv()
    
    Source can be title, fild_id, or URL
    """
    sheet = gsheet_open(source)
    return (gspread_dataframe
            .get_as_dataframe(sheet, **kw)
            .dropna(0, 'all').dropna(1, 'all')
            .fillna(''))
    

def _df_to_sheet(self, title, 
                 header=True, index=False, resize=True, 
                 public=False):
    sheet = gsheet_open(title)
    (gspread_dataframe
     .set_with_dataframe(sheet, self,
                        include_index=index,
                        include_column_header=header,
                        resize=resize)
    )
    if public:
        sheet.spreadsheet.share(None, 'anyone', 'reader')
    return 'https://docs.google.com/spreadsheets/d/' + sheet.spreadsheet.id

DataFrame.to_sheet = _df_to_sheet


# Notion.so

def get_notion_client(token=None):
    # Lazy install notion-py if not installed
    try: 
        from notion.client import NotionClient
    except:
        os.system("pip install notion")
        from notion.client import NotionClient

    # Allow access to public notion without token
    class NotionWrapper(NotionClient):
        def _update_user_info(self):
            pass
    # So, use Wrapper instead of NotionClient
    return NotionWrapper(token_v2=token)


def read_notion(url, **kwargs):
    """ Just like read_csv """
    client = get_notion_client()
    cv = client.get_collection_view(url)
    data = [row.get_all_properties() for row in cv.collection.get_rows()]
    return DataFrame(data, **kwargs)
