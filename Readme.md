



1. 跑整体流程：python main.go  （可选 --）
2. 跑获取热词并拉取图片： python i_get_image.py --word xxx   (xxx 是想获取的词)
3. 改变图片大小： python i_resize_image.py --input xxx --output xxx --width xx --height xx (xxx是文件路径， xx是长宽的数字)
4. ps套图： python i_replace_image.py --input xxx --psd xx --name x (xxx是文件夹的路径， xx是psd的文件路径， x是p图后的命名)
例子：python .\i_replace_image.py --input C:\Users\qinwe\code\final_work\process_image\resized_photos\Shohei-Ohtani-wife --psd C:\Users\qinwe\code\final_work\files\template.psd --name Shohei-Ohtani-wife
5. 图片高清化： python i_upscale_image.py --input=xxx --output=xxx
例子：python i_upscale_image.py --input=/Users/bytedance/ml-code/terraform-learn/final_work/process_image/photos/Dallas-Mavericks --output=/Users/bytedance/ml-code/terraform-learn/final_work/process_image/upscale_photos/Dallas-Maverick





git pull 是拉取最新的代码