import pytest
from pages.dashboard import Dashboard
from pages.new_repo import NewRepo
import time


@pytest.mark.parametrize("login", [("srkvd26", "Vasu@265")], indirect=True)
def test_TC_repocre_001(login):
    dashboard = Dashboard(login)
    newrepo = NewRepo(login)
    dashboard.click_add_icon()
    dashboard.select_newrepository()
    #time.sleep(2)
    newrepo.enter_reponame("my-new-repo1")
    newrepo.click_private_chkbx()
    newrepo.scroll_to_create_and_click()
    time.sleep(2)
    
    assert "my-new-repo1" in login.current_url