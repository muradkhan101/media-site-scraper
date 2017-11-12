from selenium.webdriver.common.by import By
from ..Field import Field
from ..FieldStructure import FieldStructure

def ytSearchStruct(driver):
    fieldStruct = FieldStructure()

    fieldStruct.addQuery(
        Field(
          driver,
          By.CLASS_NAME, 
          'yt-lockup-title',
          list(map( lambda x: x.find_element(By.ID, 'video-title')))
          ),
          'video-titles', True
    )
