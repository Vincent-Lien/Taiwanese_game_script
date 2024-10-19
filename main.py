import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def play_game(stg, wait_time):
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Open browser
    driver.get("http://203.66.45.207:8000/play/mzb")

    # close-btn
    try:
        close_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "close-btn"))
        )
        close_btn.click()
    except Exception as e:
        print(f"Could not find the close-btn: {e}")

    time.sleep(3)

    # Go to the next page if the stage is not in the page (15 stages in a page)
    for _ in range((stg - 1) // 15):
        # right-btn
        try:
            right_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="right-btn"]'))
            )
            right_btn.click()
        except Exception as e:
            print(f"Could not find the right-btn: {e}")
        time.sleep(1)

    # Enter the stage
    try:
        ep_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//button[contains(@class, 'stage') and text()='EP{stg}']",
                )
            )
        )
        ep_btn.click()
    except Exception as e:
        print(f"Could not find the EP{stg}: {e}")

    # audio-btn
    try:
        audio_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "audio-btn"))
        )
        audio_btn.click()
    except Exception as e:
        print(f"Could not find the audio-btn: {e}")

    time.sleep(5)

    # start-btn
    try:
        start_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-btn"))
        )
        start_btn.click()
    except Exception as e:
        print(f"Could not find the start-btn: {e}")

    time.sleep(3)

    # Check and click all button with the feature of is-correct="true"
    try:
        for stage in range(1, 13):
            time.sleep(wait_time)  # Use the specified wait time
            card = driver.find_element(By.ID, f"card{stage}")
            if card.get_attribute("is-correct") == "true":
                card.click()
                print(f"Clicked: card{stage}")
    except Exception as e:
        print(f"Error while clicking answers: {e}")

    time.sleep(5)

    # Agree
    try:
        agree_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tos2"]/button[2]'))
        )
        agree_btn.click()
    except Exception as e:
        print(f"Could not find the agree button: {e}")

    time.sleep(3)

    # Name
    try:
        name_block = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))
        )
        name_block.send_keys("YOUR_NAME")  # Change your name here
    except Exception as e:
        print(f"Could not find the name: {e}")

    # send button
    try:
        name_block = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="leaderboard"]/div[3]/button[2]')
            )
        )
        name_block.click()
    except Exception as e:
        print(f"Could not find the send button: {e}")

    time.sleep(3)

    # turn off the browser
    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game automation script")
    parser.add_argument(
        "--stages", nargs="+", type=int, required=True, help="List of stages to play"
    )
    parser.add_argument(
        "--wait-time",
        type=float,
        default=0.4,
        help="Wait time between answers (default: 0.4)",
    )

    args = parser.parse_args()

    for stage in args.stages:
        print(f"Playing stage {stage}")
        play_game(stage, args.wait_time)
