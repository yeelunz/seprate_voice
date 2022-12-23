# 人聲切割

## 前置

1. 運行 `setup.bat` 安裝需要的函式庫
2. 下載 [ffmpeg](https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-5.0.1-full_build.7z)
3. 解壓縮 `ffmpeg-5.1.2-full_build.7z` 到資料夾中
4. 根據自己的路徑，把 `ffmpeg-5.1.2-full_build\bin` 加進Path的環境變數

![Untitled](%E4%BA%BA%E8%81%B2%E5%88%87%E5%89%B2%20bbb351c58805422d9d4ee2115f907977/Untitled.png)

![Untitled](%E4%BA%BA%E8%81%B2%E5%88%87%E5%89%B2%20bbb351c58805422d9d4ee2115f907977/Untitled%201.png)

![Untitled](%E4%BA%BA%E8%81%B2%E5%88%87%E5%89%B2%20bbb351c58805422d9d4ee2115f907977/Untitled%202.png)

![Untitled](%E4%BA%BA%E8%81%B2%E5%88%87%E5%89%B2%20bbb351c58805422d9d4ee2115f907977/Untitled%203.png)

## 執行

1. 在 `yt_download.py` code裡的32行修改要下載的播放清單，接著在運行 `yt_download.py` ，程式會自動略過已經下載到 `downloads` 的音樂。

![Untitled](%E4%BA%BA%E8%81%B2%E5%88%87%E5%89%B2%20bbb351c58805422d9d4ee2115f907977/Untitled%204.png)

2.運行 `seperate.py` 去除人聲，程式會將 `input` 資料夾內的音樂去除人聲，並自動略過已經完成去除或副檔名不符合的文件，會將去除完成的音樂放置在 `output` 資料夾。

3.運行 `extract.py`會將 `output` 內的文件重新更名並移動到 `database` 資料夾。(檔案路徑長度如果超過255的話不會移動)