import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    wait = WebDriverWait(driver, 20)

    driver.get(base_url + "simple-form-demo")

    wait.until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    message_box = wait.until(
        EC.visibility_of_element_located((By.ID, "user-message"))
    )

    message_box.clear()
    message_box.send_keys(message)

    button = wait.until(
        EC.element_to_be_clickable((By.ID, "showInput"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    driver.execute_script("arguments[0].click();", button)

    output = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    wait.until(lambda d: output.text.strip() != "")

    assert output.text.strip() == message


def test_checkbox_demo(driver, base_url):

    wait = WebDriverWait(driver, 20)

    driver.get(base_url + "checkbox-demo")

    checkbox = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='checkbox']")
        )
    )

    driver.execute_script("arguments[0].click();", checkbox)

    assert checkbox.is_selected()

    driver.execute_script("arguments[0].click();", checkbox)

    assert not checkbox.is_selected()


def test_dropdown_selection(driver, base_url):

    wait = WebDriverWait(driver, 20)

    driver.get(base_url + "select-dropdown-demo")

    dropdown = Select(
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "select-demo")
            )
        )
    )

    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"