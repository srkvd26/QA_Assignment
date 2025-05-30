import pytest
from pages.dashboard import Dashboard
from pages.new_repo import NewRepo
import time


@pytest.mark.parametrize("login", [("srkvd26", "Vasu@265")], indirect=True)
def test_TC_repocre_001(login, logger):
    try:
        logger.info("********* test_TC_repocre_001 ********")
        dashboard = Dashboard(login)
        newrepo = NewRepo(login)
        dashboard.click_add_icon()
        dashboard.select_newrepository()
        newrepo.enter_reponame("my-new-repo")
        newrepo.click_private_chkbx()
        newrepo.scroll_to_create_and_click()
        time.sleep(2)
        
        assert "my-new-repo" in login.current_url

    except Exception as e:
        logger.info("[Exception Occured] " + str(e))
        assert False, "Exception occured, hence test case is failed"