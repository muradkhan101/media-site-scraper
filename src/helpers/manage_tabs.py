from selenium.webdriver.common.keys import Keys

def get_tab_index(driver, handle):
    for i in range(len(driver.window_handles)):
        if driver.window_handles[i] == handle:
            return i
    return None

def open_tab(driver, link):
    """
    Opens a given link in a new tab, switches to it, and returns the new tab handle
    @params(driver, link)
    driver is a Selenium driver instance
    link is an <a> tag

    returns the old tab handle and new tab handle
    """
    tab_handle = driver.current_window_handle
    current_tab = get_tab_index(driver, tab_handle)
    link.send_keys(Keys.COMMAND + Keys.RETURN)
    driver.switch_to.window(driver.window_handles[current_tab + 1])
    return ( tab_handle, driver.current_window_handle )

def close_tab(driver, old):
    driver.close()
    driver.switch_to.window(old)
