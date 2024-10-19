# Taiwanese_game_script

魔字壁 game link: http://203.66.45.207:8000/play/mzb

This is a script for playing a game called "魔字壁" automatically. You can run multiple stages at once and make your name on the leaderboard.

## Setput
### 1. Code
```
git clone https://github.com/Vincent-Lien/Taiwanese_game_script.git
```
### 2. Environment
Download the chormewebdriver, for the latest version please check: https://googlechromelabs.github.io/chrome-for-testing/#stable  

After downloading the chormewebdriver, please place it in the root folder.

Then
```
pip install selenium
```
### 3. Run
```
python main.py --stages [NUMBER_OF_STAGES] --wait-time [WAITING_TIME_BETWEEN_ANSWERING] --name [YOUR_NAME]
```
For example, to run stage 8, stage 9 and wait 0.5 seconds between answers:
```
python main.py --stages 8 9 --wait-time 0.5
```